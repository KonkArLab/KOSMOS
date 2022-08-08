# Traitement des vidéos issues du système KOSMOS <img width="50" alt="image kosmos" src="https://user-images.githubusercontent.com/108416242/182578775-55f881ab-6064-4b50-8c58-42cfca3f6113.PNG">


Le but de ces algorithmes est d'améliorer les vidéos sous-marines en traitant la turbidité et en corrigeant les couleurs (en python) 

## Prérequis 

Python : 
  Libraries: 
    - OpenCV
    - Numpy
    - Math
    - moviepy
    - Pathlib
    - Imageio 
    - OS
    - multiprocessing & concurrent.futures
 
## Lancer l'algorithme 

L'arborescence de fichier doit se présenter comme celui-ci : ![fichier](https://user-images.githubusercontent.com/108416242/182579384-d89315d0-6ace-4c36-b664-69f7bbeefd04.PNG)

Avec les vidéos à traitées dans le dossier "Vidéos" et les vidéos traitées dans le dossier "Vidéos traitées". Le dossier "Frames" contiendra toutes les images
des videos et ces images seront traitées directement dans ce dossier. ⚠️ Pensez à vérifier que les chemins de dossier, présents dans le code, sont exacts.

- Dehaze_HE.py : contient le code qui va traiter une vidéo/image avec les méthodes d’égalisation d’histogramme et de débrumage.
- Dehaze_retinex.py : contient le code qui va traiter une vidéo/image avec les méthodes rétinex et débrumage.

Dans chacun des deux fichiers python il y a une partie pour modifier certains paramètres : 

``` 
### PARAMETRES A RENSEIGNER ### 
filename_video = './Vidéos/kosmos_2022-07-19-19-09-16.mp4'

db_min = 13
db_s =44

fin_min = 13
fin_s= 54

filename_video_a_traiter = "./Vidéos/video.mp4"
###############################
```
C'est ici que l'on rentre la durée (db_min, db_s, fin_min, fin_s) de la vidéo que l'on souhaite traiter avec un temps de début et de fin. 
Il est également possible de ne traiter qu'une frames en définissant fin_min et fin_s à 0. 

## Exemples d'une image traitée avec les 2 codes 
<center>
<img src="./exemples/image_originale.png"  height = "400" alt="Image originale" />
<img src="./exemples/image_HE.png"  height = "400" alt="Image traitée avec HE et le débrumage" />
<img src="./exemples/image_retinex.png"   height = "400" alt="Image traitée avec le rétinex" />
</center>


## Algorithmes/articles utilisés :
- Single Image Haze Removal Using Dark Channel Prior, Kaiming He, Jian Sun, and Xiaoou Tang", in CVPR 2009 
- Guided Image Filtering, Kaiming He, Jian Sun, and Xiaoou Tang", in ECCV 2010.
- Properties and Performance of a Center/Surround Retinex, Daniel J. Jobson, Zia-ur Rahman, 1997 
- A Retinex-Based Enhancing Approach for Single Underwater Image, Xueyang Fu, Peixian Zhuang, Yue Huang, Yinghao Liao, Xiao-Ping Zhang, Xinghao Ding, 2014 


## Auteur 

***Zoë DAHERON*** - *stage technique* - IFREMER


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

