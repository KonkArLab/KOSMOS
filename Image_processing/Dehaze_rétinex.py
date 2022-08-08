# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:35:27 2022

@author: zdaheron
"""

# -*- coding: utf-8 -*-

import cv2
import math
import numpy as np
import imageio
import pathlib
import os
import time
import moviepy.editor
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
    clip = moviepy.editor.VideoFileClip(filename)
  
    #Calcul du nombre de secondes 
    a = 60*db_min + db_s #début 
    b = 60*fin_min + fin_s #fin 
    
    
    if fin_min == 0 and fin_s == 0: 
        clip.save_frame("./Frames/000.png", t = a ) # Récupération que d'une image 
    else:
        # Sinon récupération d'un morceau de film entre a et b seconde 
        ffmpeg_extract_subclip(filename, a, b, targetname=filename2)
        Video2Images(filename2) #Appel de la fonction pour décomposer le film en frames

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

def Video2Images (filename): #Découpe d'un vidéo en images 
    reader = imageio.get_reader(filename)# recuperation de la vidéo  
    for frame_number, im in enumerate(reader): 
        if frame_number % 3 == 0 :
            imageio.imwrite('./Frames/{:03d}'.format(int(frame_number/3)) + '.png', im) # Ecriture des images dans le dossier Frames
            
def generate_video(image_folder):
      
    video_name = 'video_corrigee_retinex.mp4'
    os.chdir("./Vidéos_traitees") # chemin du dossier où va etre generer la video 
    images = [img for img in os.listdir(image_folder)] # recuperation des images dans une liste 

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape  
    video = cv2.VideoWriter(video_name, 0, 10, (width, height)) 
  
    #Ajout des images une par une 
    for image in images: 
        video.write(cv2.imread(os.path.join(image_folder, image))) 
      
    #Délocalisationde de la mémoire prise pour la création de fenetre 
    cv2.destroyAllWindows() 
    video.release()  # "libération" de la vidéo 

def Dehaze(fn):
    im = cv2.imread(fn)
    II = im.astype('float64')/255
    srcc= Float2BGR(II)
    dark = DarkChannel(II,15)#15
    A = AtmLight(II,dark)
    te = TransmissionEstimate(II,A,15)
    t = TransmissionRefine(srcc,te)
    III = Recover(II,t,A,0.1) #retrouver l'éclat 
    #print(AnalyseHisto(III)[0])
    cv2.imwrite(fn,III*255) 



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
        

    
    
    
#%%
t1 = time.perf_counter()
################## PARAMETRES A RENSEIGNER ###############################

filename_video = './Vidéos/kosmos_2022-07-19-20-17-23.mp4'

db_min = 13
db_s =34

fin_min = 13
fin_s= 44

filename_video_a_traiter = "./Vidéos/video.mp4"

#########################################################################

if __name__ == '__main__':
    
    dossier_vide() 
    
    decoup_video(db_min, db_s, fin_min, fin_s, filename_video,filename_video_a_traiter) #Appel de la fonction qui découpe une partie de la vidéo et la divise en frames 
    
    image_folder = 'C:\\Users\\zdaheron\\Desktop\\Test_pour_git\\Frames'
    
    nb_image = 0 
    for path in pathlib.Path(image_folder).iterdir(): #Récupération du nombre de frames/images
        if path.is_file():
            nb_image += 1
            
    img_names= []
    
    #Traitement des images une par une  
    for i in range (0,nb_image):
        fn= './Frames/'+ str(i).zfill(3) + '.png' 
        Dehaze(fn)
        img_names.append(fn)#Ajout du chemin des frames dans une liste 
       
    freeze_support()#Permet au programme de geler, créer et démarrer de nouveaux processus pour le multitraitement 
    #Le module concurrent.futures permet d'exécuter le code à l'aide de processus distincts
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image,img_names)#Application de la méthode (He+ débrumage) en multitraitement aux frames dans la liste img_names
        
    generate_video(image_folder)# Génération de la vidéo 
    
        
t2 = time.perf_counter()
print(f'Finished in {t2-t1} secondsS')



