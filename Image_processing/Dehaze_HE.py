# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:13:31 2022

@author: zdaheron
"""
import moviepy.editor
import cv2
import math
import numpy as np
import imageio
import pathlib
import os
import time
import concurrent.futures
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import multiprocessing
from multiprocessing import freeze_support
import concurrent.futures

def dossier_vide():
#Fonction qui verifie que le dossier est vide si ce n'est pas le cas il est vidé 
    repertoire = "C:\\Users\\zdaheron\\Desktop\\Test_pour_git\\Frames"
    if len(os.listdir(repertoire)) != 0: #Vérifie que le dossier qui va contenir les images est vide 
         for filename in os.listdir(repertoire) :
            print(repertoire + "/" + filename)
            os.remove(repertoire + "/" + filename) #Si le dossier n'est pas vide, suppression des fichiers 


def decoup_video(db_min, db_s,fin_min,fin_s,filename, filename2):
#Fonction qui va en fonction du temps rentré en paramètre récupérer une partie de la vidéo 
    #Calcul du nombre de secondes 
    a = 60*db_min + db_s #début 
    b = 60*fin_min + fin_s #fin 
    
    clip = moviepy.editor.VideoFileClip(filename_video)
    if fin_min == 0 and fin_s == 0:
        clip.save_frame("./Frames/000.png", t = a ) # Récupération que d'une image 
    else:
        #Sinon récupération d'un morceau de film entre a et b seconde 
        ffmpeg_extract_subclip(filename, a, b, targetname=filename2)
        Video2Images(filename2) #Appel de la fonction pour décomposer le film en images

def DarkChannel(im,sz):
#Determine le canal sombre de l'image 
    b,g, r= cv2.split(im)# Séparation des 3 canaux
    dc = cv2.min(cv2.min(b,g),b);#La couleur minimale entre le canal bleu et vert
    for ind in range(0,3):
        
        dc[:,ind] = np.median(dc[:,ind], axis=0) #Médiane (MDCP)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(sz,sz))#Elément structurant pour l'érosion
    dark = cv2.erode(dc,kernel) #Erosion de l'image en fonction de la couleur minimale 
    return dark
#L'érosion va omettre ou à amincir les limites de la zone claire de l'image

def AtmLight(im,dark):
#Estimation de la lumière atmosphérique 
    [h,w] = im.shape[:2]
    imsz = h*w
    numpx = int(max(math.floor(imsz/100),1))# Définition du nombre de valeurs à garder (0.1%) 
    darkvec = dark.reshape(imsz);#Façonne le tableau dark sans modification de données
    imvec = im.reshape(imsz,3);
    indices = darkvec.argsort();#Tri croissant des indices du tableau 
    indices = indices[imsz-numpx::]#Suppression des 12000 indices les plus faibles
    
    atmsum = np.zeros([1,3])#Initialisation du tableau (toutes les valeurs sont à 0)
    for ind in range(1,numpx):
       atmsum = atmsum + imvec[indices[ind]] #Somme des valeurs avec le + d'intensité 

    A = atmsum / numpx; #Divison de la somme par le nombre de valeurs des pixels (0.1%) 

    return A
# math.floor : arrondit à l'entier 

def TransmissionEstimate(im,A,sz):
    omega = 0.6;
    im3 = np.empty(im.shape,im.dtype);#Initalisation du tableau correspondant à la transmission
    
    for ind in range(0,3):
        im3[:,:,ind] = im[:,:,ind]/A[0,ind] # im3 = im/A (voir formule)
    transmission = 1 - omega*DarkChannel(im3,sz);#Formule pour trouver la transmission
    return transmission
#np.empty : renvoie un nouveau tableau de forme et de type donnés, sans initialiser les entrées

def Guidedfilter(im,p,r,eps):
#Filtre l'image d'entrée (p) sous la direction d'une autre image (im)
#Recherche les coefficients a et b qui minimisent la différence entre la sortie q et l'entrée p 

    #Moyennes et variances utiles pour le calcul de a et b 
    mean_I = cv2.boxFilter(im,cv2.CV_64F,(r,r));
    mean_p = cv2.boxFilter(p, cv2.CV_64F,(r,r));
    mean_Ip = cv2.boxFilter(im*p,cv2.CV_64F,(r,r));
    cov_Ip = mean_Ip - mean_I*mean_p;

    mean_II = cv2.boxFilter(im*im,cv2.CV_64F,(r,r));
    var_I   = mean_II - mean_I*mean_I;

    a = cov_Ip/(var_I + eps); #calcul de a selon la formule (voir doc)
    b = mean_p - a*mean_I; #calcul de b selon la formule (voir doc)
    
    mean_a = cv2.boxFilter(a,cv2.CV_64F,(r,r)); #moyenne de a
    mean_b = cv2.boxFilter(b,cv2.CV_64F,(r,r)); # moyenne de b 
   
    q = mean_a*im + mean_b; # transmission affinée 
    return q;

def TransmissionRefine(im,et): 
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY); #Image en teinte de gris 
    gray = np.float64(gray)/255; 
    r = 60;
    eps = 0.0001;
    t = Guidedfilter(gray,et,r,eps);
    return t;

def Float2BGR(I):
#Conversion d'un float (0 - 1) à nb sur 8 bits (0 - 255)
    erf=I*255
    src=erf.astype('uint8')
    return src

def Recover(im,t,A,tx =1.0):
#Fonction servant à retrouver l'éclat 
    res = np.empty(im.shape,im.dtype);#Initalisation du tableau correspondant à l'éclat
    tt=np.zeros((t.shape[0],t.shape[1],3))#Initialisation du tableau tt 
   
    #Calcul de max(t(x),t0) pour chaque canal de couleur
    tt[:,:,0]=cv2.max(t,tx)      #blue
    tt[:,:,1]=cv2.max(t,tx)      #green
    tt[:,:,2]=cv2.max(t,tx)      #red

    for ind in range(0,3):
        #Formule de J(x) = (I(x)-A/max(t(x),t0))+A
        res[:,:,ind] = (im[:,:,ind]-A[0,ind])/tt[:,:,ind] + A[0,ind]
    return res


def AnalyseHisto(I):
    #moyenne de chaque canal
    MeanB=np.mean(I[:,:,0])
    MeanG=np.mean(I[:,:,1])
    MeanR=np.mean(I[:,:,2])
    #Variance de chaque canal
    SquareB=np.sqrt(1/I[:,:,0].size*sum(sum((I[:,:,0]-MeanB)**2)))
    SquareG=np.sqrt(1/I[:,:,1].size*sum(sum((I[:,:,1]-MeanG)**2)))
    SquareR=np.sqrt(1/I[:,:,2].size*sum(sum((I[:,:,2]-MeanR)**2)))
    Mean=[MeanB,MeanG,MeanR]
    Square=[SquareB,SquareG,SquareR]
    return Mean,Square

def Video2Images (filename): 
#Découpe d'un vidéo en images 
    reader = imageio.get_reader(filename)#Récupération de la vidéo 
    for frame_number, im in enumerate(reader): 
        if frame_number % 3 == 0 : 
            imageio.imwrite('./Frames/{:03d}'.format(int(frame_number/3)) + '.png', im) # Ecriture des images dans le dossier Frames
            
def generate_video(image_folder):
#Génération de la vidéo à partir d'images 
    video_name = 'video_HE.mp4'
    os.chdir("./Vidéos_traitees") #Chemin du dossier où va être générer la video 
    images = [img for img in os.listdir(image_folder)] #Récupération des images dans une liste 

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape #Récupération de la taille des frames 
    video = cv2.VideoWriter(video_name, 0, 10, (width, height)) 
  
    #Ajout des images une par une 
    for image in images: 
        video.write(cv2.imread(os.path.join(image_folder, image))) 
      
    #Délocalisation de la mémoire prise pour la création de fenêtre 
    cv2.destroyAllWindows() 
    video.release()  # "Libération" de la vidéo 
    
def Det_Coef(I):
#Fonction qui determine les coefficients pour la correction des couleurs 
    if AnalyseHisto(I)[0][0] >= 0.35 or 0.20 < AnalyseHisto(I)[1][0] < 0.21 :
        coefB = 2 
    if AnalyseHisto(I)[0][0] >= 0.6 or 0.16 < AnalyseHisto(I)[1][0] < 0.19 :
        coefB = 2 
    else:
        coefB = 3
    #Coefficient vert 
    if  AnalyseHisto(I)[1][1] <= 0.25 :
        coefG = 3
    if  AnalyseHisto(I)[1][1] < 0.25 and 0.84< AnalyseHisto(I)[0][1] < 0.86:
        coefG = 4
    else : 
        coefG = 4
    #Coefficient rouge 
    if AnalyseHisto(I)[1][2] < 0.07  and  (AnalyseHisto(I)[0][2] < 0.2 or AnalyseHisto(I)[0][2] > 0.3) :
        coefR = 7
    if AnalyseHisto(I)[0][2] < 0.082  and  0.07 < AnalyseHisto(I)[1][2] < 0.1 :
        coefR = 7
    elif 0.07 < AnalyseHisto(I)[1][2] < 0.08 and  AnalyseHisto(I)[0][2] > 0.2: 
        coefR = 7 
    elif AnalyseHisto(I)[1][2] > 0.16 and  0.2 < AnalyseHisto(I)[0][2] < 0.3: #0.12
        coefR = 2
    else:
        coefR = 4
    return coefB, coefG, coefR

  
def Dehaze(fn):
#Fonction qui appelle toutes les fonctions pour réaliser le débrumage 
    im = cv2.imread(fn)
    II = im.astype('float64')/255
    srcc= Float2BGR(II)
    dark = DarkChannel(II,15)
    A = AtmLight(II,dark)
    te = TransmissionEstimate(II,A,15)
    t = TransmissionRefine(srcc,te)
    III = Recover(II,t,A,0.1) 
    cv2.imwrite(fn,III*255) 
    

def process_image(img_names):
#Fonction qui permet d'appliquer la méthode He et le débrumage  plus rapidement (plusieurs processus fonctionnent en même temps)
    Dehaze(img_names)#Débrumage 
    img = cv2.imread(img_names)# Lecture de l'image 

    I = img.astype('float64')/255 #
    II=np.zeros(I.shape)
    
    #Récupération des coefficients 
    R = Det_Coef(I)[2]
    G = Det_Coef(I)[1]
    B= Det_Coef(I)[0]
    
    #Moyenne de chaque canal de couleur
    MeanB=np.mean(I[:,:,0])
    MeanG=np.mean(I[:,:,1])
    MeanR=np.mean(I[:,:,2])
    #Variance de chaque canal
    SquareB=np.sqrt(1/I[:,:,0].size*sum(sum((I[:,:,0]-MeanB)**2)))
    SquareG=np.sqrt(1/I[:,:,1].size*sum(sum((I[:,:,1]-MeanG)**2)))
    SquareR=np.sqrt(1/I[:,:,2].size*sum(sum((I[:,:,2]-MeanR)**2)))
    #Correction des histogrammes avec la formule pour chaque canal: II = (I - Moyenne + coef*variance)/ 2*coef*variance (II étant la nouvelle image, I l'image à corrigée et
    #coef les coefficients récupéré plus haut)
    II[:,:,0]=(I[:,:,0]-MeanB+B*SquareB)/(2*B*SquareB)
    II[:,:,1]=(I[:,:,1]-MeanG+G*SquareG)/(2*G*SquareG)
    II[:,:,2]=(I[:,:,2]-MeanR+R*SquareR)/(2*R*SquareR)   
    
    cv2.imwrite(img_names, II*255)# Ecriture de l'image corrigée
  
        
#%%
t1 = time.perf_counter()
################## PARAMETRES A RENSEIGNER ###############################


filename_video = './Vidéos/kosmos_2022-07-19-19-09-16.mp4' 

db_min = 13
db_s =44

fin_min = 13
fin_s= 54
filename_video2 = "./Vidéos/video.mp4"

#########################################################################

if __name__ == '__main__':
    dossier_vide()
    
    decoup_video(db_min, db_s, fin_min, fin_s, filename_video,filename_video2) #Appel de la fonction qui découpe une partie de la vidéo et la divise en frames 
    
    image_folder = 'C:\\Users\\zdaheron\\Desktop\\Test_pour_git\\Frames'
    
    nb_image = 0 
    for path in pathlib.Path(image_folder).iterdir(): # Récupération du nombre de frames/images
        if path.is_file():
            nb_image += 1
    img_names= []
    #Traitement des images une par une  
    for i in range (0,nb_image):
        fn= './Frames/'+ str(i).zfill(3) + '.png' 
        
        img_names.append(fn)#Ajout du chemin des frames dans une liste 
    freeze_support()#Permet au programme de geler, créer et démarrer de nouveaux processus pour le multitraitement 
    with concurrent.futures.ProcessPoolExecutor() as executor:
    #Le module concurrent.futures permet d'exécuter le code à l'aide de processus distincts
        executor.map(process_image,img_names)#Application de la méthode (He+ débrumage) en multitraitement aux frames dans la liste img_names
      
    generate_video(image_folder)# Génération de la vidéo 
    
        
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')
