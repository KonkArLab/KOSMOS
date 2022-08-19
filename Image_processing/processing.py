# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:13:31 2022

@author: zdaheron
"""

import moviepy.editor
import cv2
import math 
from math import floor
import numpy as np
import shutil
import imageio
import pathlib
import os
import time
import concurrent.futures
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import multiprocessing
from multiprocessing import freeze_support
import concurrent.futures


############### Fonctions pour les vidéos #####################################

def dossier_vide():
#Fonction qui verifie que le dossier est vide si ce n'est pas le cas il est vidé 
    repertoire = "./Frames"
    if len(os.listdir(repertoire)) != 0: #Vérifie que le dossier qui va contenir les images est vide 
         for filename in os.listdir(repertoire) :
            print(repertoire + "/" + filename)
            os.remove(repertoire + "/" + filename) #Si le dossier n'est pas vide, suppression des fichiers 


def Video2Images (filename): 
#Découpe d'un vidéo en images 
    reader = imageio.get_reader(filename)#Récupération de la vidéo 
    for frame_number, im in enumerate(reader): 
        if frame_number % 3 == 0 : #%3 pour avoir 8 frames/s au lieu de %1 soit 25 frames/s
            imageio.imwrite('./Frames/{:03d}'.format(int(frame_number/3)) + '.png', im) # Ecriture des images dans le dossier Frames
            

def decoup_video(a,b,filename, filename2):
#Fonction qui va en fonction du temps rentré en paramètre récupérer une partie de la vidéo 
    #Calcul du nombre de secondes 
    
    clip = moviepy.editor.VideoFileClip(filename_video)
    if fin_min == 0 and fin_s == 0:
        clip.save_frame("./Frames/000.png", t = a ) # Récupération que d'une image 
    else:
        #Sinon récupération d'un morceau de film entre a et b seconde 
        ffmpeg_extract_subclip(filename, a, b, targetname=filename2)
        Video2Images(filename2) #Appel de la fonction pour décomposer le film en images

def generate_video(image_folder, method):
#Génération de la vidéo à partir d'images
    if method == "retinex" :  
        video_name = 'video_retinex.mp4'
    elif method == "HE" :
        video_name = 'video_HE.mp4'
    else :
        video_name = 'video_UDCP.mp4'
    os.chdir("./") 
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
    shutil.move('./'+ video_name, './Videos_traitees/'+video_name)

###############################################################################


#################### Dark Channel Prior #######################################
# Basé sur les études suivantes : Single Image Haze Removal Using Dark Channel Prior, Kaiming He, Jian Sun, and Xiaoou Tang", in CVPR 2009 
# et Guided Image Filtering, Kaiming He, Jian Sun, and Xiaoou Tang", in ECCV 2010.

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

def process_image_dehaze(img_names):
#Fonction qui appelle toutes les fonctions pour réaliser le débrumage en multiprocessing
    im = cv2.imread(img_names)
    II = im.astype('float64')/255
    srcc= Float2BGR(II)
    dark = DarkChannel(II,15)
    A = AtmLight(II,dark)
    te = TransmissionEstimate(II,A,15)
    t = TransmissionRefine(srcc,te)
    III = Recover(II,t,A,0.1) 
    cv2.imwrite(img_names,III*255) 
###############################################################################    


######################### Egalisation d'histogrammes (HE) #####################

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

    
def Det_Coef(I): 
    #Coefficient bleu
    if AnalyseHisto(I)[0][0] >= 0.20 :
        coefB = 2 
    else:
        coefB = 3
    #Coefficient vert 
    if  AnalyseHisto(I)[0][1] > 0.6 :
        coefG = 3
    elif 0.3 < AnalyseHisto(I)[0][1] < 0.6 :
        coefG = 2
    else : 
        coefG = 4
    #coefficient rouge
    if 0.1 < AnalyseHisto(I)[0][2] < 0.2 and AnalyseHisto(I)[1][2] < 0.1:
        coefR = 3
        
    elif  0.1 < AnalyseHisto(I)[0][2] < 0.3 and AnalyseHisto(I)[1][2] > 0.1:
        coefR =2
    elif 0.2 < AnalyseHisto(I)[0][2] < 0.3  :
        coefR = 3
    
    elif  AnalyseHisto(I)[0][2] < 0.07:
        coefR =0
    else:
        coefR = 4
    return coefB, coefG, coefR

def process_image1(img_names):
#Fonction qui permet d'appliquer la méthode He et le débrumage  plus rapidement (plusieurs processus fonctionnent en même temps)
    Dehaze(img_names)#Débrumage 
    img = cv2.imread(img_names)# Lecture de l'image 

    I = img.astype('float64')/255 #
    II=np.zeros(I.shape)
    
    #Récupération des coefficients 
    R =Det_Coef(I)[2]
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

###############################################################################


############################ Rétinex ##########################################

def process_image(img_names):
#Fonction qui permet d'appliquer la méthode rétinex plus rapidement (plusieurs processus fonctionnent en même temps)  
    img =cv2.imread(img_names) #Lecture de l'image
    img = np.float64(img) + 1.0
    variance=400
    img_retinex =np.log10(img) - np.log10(cv2.GaussianBlur(img, (0, 0), variance)) #formule du retinex 
    for i in range(img_retinex.shape[2]):
        unique, count = np.unique(np.int32(img_retinex[:, :, i] * 100), return_counts=True)#Retourne un tableau du nombre de chaque valeur unique 
        #unique contient toute les valeurs uniques et count contient le nombre d'apparition de ces valeurs
        
        #Boucles pour trouver la valeur minimale et maximale (toujours de chaque canal)
        for u, c in zip(unique, count):
            if u == 0:
                zero_count = c
                break            
        low_val = unique[0] / 100.0
        high_val = unique[-1] / 100.0
        for u, c in zip(unique, count):
            if u < 0 and c < zero_count * 0.1:
                low_val = u / 100.0
            if u > 0 and c < zero_count * 0.1:
                high_val = u / 100.0
                break    
     
        img_retinex[:, :, i] = np.maximum(np.minimum(img_retinex[:, :, i], high_val), low_val)
        #formule dans étude de X. Fu 
        img_retinex[:, :, i] = (img_retinex[:, :, i] - np.min(img_retinex[:, :, i])) / \
                                (np.max(img_retinex[:, :, i]) - np.min(img_retinex[:, :, i])) \
                                * 255
    img_retinex = np.uint8(img_retinex)        
    cv2.imwrite(img_names, img_retinex)#Ecriture de l'image   
    
###############################################################################

################### Temps de traitement estimé ################################
            
def temps (method, a, b):
#Fonction qui calcul le temps de traitement estimé en fonction de la méthode utilisé 
#et qui l'affiche dans la console 
    duree = b-a
    if method == "retinex":
        temps = 8.3*duree*16+(duree*23/60)
        print(f"Le temps de traitement est estimé à {floor(temps/60)}min et {floor(temps%60)}s")
    elif method == "HE" :
        temps = 8.3*duree*5+(duree*23/60)
        print(f"Le temps de traitement est estimé à {floor(temps/60)}min et {floor(temps%60)}s")
    else :
        temps = 8.3*duree*4+(duree*23/60)
        print(f"Le temps de traitement est estimé à {floor(temps/60)}min et {floor(temps%60)}s")

#%%

################## PARAMETRES A RENSEIGNER ###############################

filename_video = './Videos/MOV_0008.mp4' 

db_min = 0
db_s =0

# Pour ne traiter qu'une frame il est possible de définir fin_min et fin_s à 0
fin_min = 0
fin_s= 4

#variable pour choisir la méthode de traitement : "retinex" / "HE" / "UDCP" 
method = "UDCP"

filename_video2 = "./Videos/video.mp4"

#########################################################################

if __name__ == '__main__':
    #Calcul du nombre de secondes
    a = 60*db_min + db_s #début 
    b = 60*fin_min + fin_s #fin 
  
    temps(method, a, b)
    
    dossier_vide()
   
    decoup_video(a,b, filename_video,filename_video2) #Appel de la fonction qui découpe une partie de la vidéo et la divise en frames 
     
    image_folder = './Frames'
    
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
        if method == "HE":
            executor.map(process_image1,img_names)#Application de la méthode (He+ débrumage) en multitraitement aux frames dans la liste img_names
        elif method == "retinex" : 
            executor.map(process_image,img_names)#Application de la méthode (retinex+ débrumage) en multitraitement aux frames dans la liste img_names
        else :
            executor.map(process_image_dehaze,img_names)#Application de la méthode de déburmage (UDCP) en multitraitement aux frames dans la liste img_names
    generate_video(image_folder, method)# Génération de la vidéo 
  

