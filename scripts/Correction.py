# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:04:22 2022

@author: zdaheron
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

from Dehaze_git import Dehaze 


def AnalyseHisto (I):
    #Moyenne de chaque canal
    MeanB=np.mean(I[:,:,0])
    MeanG=np.mean(I[:,:,1])
    MeanR=np.mean(I[:,:,2])
    #Ecart-type de chaque canal
    SquareB=np.sqrt(1/I[:,:,0].size*sum(sum((I[:,:,0]-MeanB)**2)))
    SquareG=np.sqrt(1/I[:,:,1].size*sum(sum((I[:,:,1]-MeanG)**2)))
    SquareR=np.sqrt(1/I[:,:,2].size*sum(sum((I[:,:,2]-MeanR)**2)))
    Mean=[MeanB,MeanG,MeanR]
    Square=[SquareB,SquareG,SquareR]
    return Mean,Square
    
def CorrectionHisto( I,R,G,B): # correction des histogrammes
    II=np.zeros(I.shape)
    #Formule pour chaque canal I = (I - Moyenne + coef*variance)/ 2*coef*variance
    II[:,:,0]=(I[:,:,0]-AnalyseHisto(I)[0][0]+B*AnalyseHisto(I)[1][0])/(2*B*AnalyseHisto(I)[1][0])
    II[:,:,1]=(I[:,:,1]-AnalyseHisto(I)[0][1]+G*AnalyseHisto(I)[1][1])/(2*G*AnalyseHisto(I)[1][1])
    II[:,:,2]=(I[:,:,2]-AnalyseHisto(I)[0][2]+R*AnalyseHisto(I)[1][2])/(2*R*AnalyseHisto(I)[1][2])   
    return II
    

def Affichage_histo(im):#Affichage de l'histogramme avec les 3 canaux de couleur(r,g,b)
    image = im*255 #récupération de l'image 
    colors = ("red", "green", "blue")# tuple pour selectionner la couleur pour chaque canal
    channel_ids = (2,1,0)
    #création d'un histogramme avec 3 lignes, une pour chauque couleur
    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(image[:, :, channel_id], bins=256, range=(0, 256))
        plt.plot(bin_edges[0:-1], histogram, color=c)
    #légendes 
    plt.xlabel("Color value")
    plt.ylabel("Pixels")
    
    plt.show()
        
def Det_Coef(I):
    #Fonction qui determine à partir de la moyenne et de la vraiance de chaque canal les coéfficients 
    #à appliquer pour la correction 
    
    #Coefficient bleu
    if AnalyseHisto(I)[0][0] >= 0.35 or 0.20 <AnalyseHisto(I)[1][0] < 0.21 :
        coefB = 2 
    else:
        coefB = 3
    #Coefficient vert 
    if  AnalyseHisto(I)[1][1] <= 0.25 :
        coefG = 3
    else : 
        coefG = 4
    #Coefficient rouge 
    if AnalyseHisto(I)[1][2] < 0.07  and  (AnalyseHisto(I)[0][2] < 0.2 or AnalyseHisto(I)[0][2] > 0.3) :
        coefR = 7
    elif 0.07 < AnalyseHisto(I)[1][2] < 0.08 and  AnalyseHisto(I)[0][2] > 0.2: 
        coefR = 7 
    elif AnalyseHisto(I)[1][2] > 0.12 and  0.2 < AnalyseHisto(I)[0][2] < 0.3: 
        coefR = 2
    else:
        coefR = 4
    return coefB, coefG, coefR
    
def Correction_fond2(fn): #fonction qui va corriger le fond de l'image (si elle contient du sable) 
    Dehaze(fn) #Application du débrumage avant correction 
    im = cv2.imread(fn)
    I2 = im.astype('float64')/255
    II= CorrectionHisto(I2,10.,6.,6.)
    cv2.imwrite(fn,II*255) 
    #Application du débrumage après correction deux fois 
    Dehaze(fn)
    Dehaze(fn)
    
def Correction_fond(fn): #fonction qui va corriger le fond de l'image (si elle ne contient pas de sable)
    im = cv2.imread(fn)
    I2 = im.astype('float64')/255
    II= CorrectionHisto(I2,9.,2.,1.)
    cv2.imwrite(fn,II*255) 
       
    
def Correction_sable(fn):#fonction qui va corriger la couleur du sable 
    srcc= cv2.imread(fn)
    I2 = srcc.astype('float64')/255
    II= CorrectionHisto(I2,3.,3.,3.)
    cv2.imwrite(fn,II*255) 
    Dehaze(fn)
    Dehaze(fn)
        
def Correction_PP(fn,I):#fonction qui va corriger le premier plan (si elle ne contient pas de sable)
    Dehaze(fn)
    im = cv2.imread(fn)
    I2 = im.astype('float64')/255
    II= CorrectionHisto(I2,5.,4.,4.)
    cv2.imwrite(fn,II*255) 
    Dehaze(fn)
    
    if (AnalyseHisto(I)[0][2] < 90) or (AnalyseHisto(I)[0][0] < 112) : #Si les pixels de l'image ont une valeur moyenne
    #de rouge faible (inférieur à 90) ou une moyenne de bleu faible :
        Dehaze(fn) #Application du dehazing une seconde fois 
