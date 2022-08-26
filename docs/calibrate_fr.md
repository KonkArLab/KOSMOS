# Calibration du temps de pause

## 1/ Introduction
Cette notice permet de résumer la calibration du KOSMOS de manière à paramétrer la pause d’observation de 30 secondes par secteurs. 

La réalisation de la calibration du KOSMOS doit être effectuée **dans l’air, puis dans l’eau.**
La première calibration dans l’air permet de vérifier la cohérence du protocole d’observation :
Démarrage du moteur, passage d’un cran dans la croix de Malte, arrêt du moteur par l’ILS, et durée de la pause d’observation.
La seconde calibration dans l’eau permet d’obtenir une durée précise de la pause d’observation. En effet, dû à une importante différence de densité entre l’air et l’eau, le système de réduction ne se comportera pas de la même façon et le temps de calibration sera différent.


**Note :** Influence de l’eau sur le temps de rotation du kosmos

La présence de l’eau va considérablement contribuer à la perte de puissance du système de réduction. Cette résistance entre un fluide qui s’oppose au corps de l’engrenage s’appelle une perte par ventilation. L’expression du coefficient de perte par ventilation est ainsi directement fonction de la densité du fluide (rhô).
Par exemple la densité de l’air à Concarneau est d’environ rhô=1,195 kg/m3 (à  20° et 90% d’humidité). Tandis que la densité de l’eau à 10m est d’environ rhô=1 025,556 kg/m3 (avec 17,2°C, 35,2 psu et 2 bar). Nous avons donc un facteur 10 puissance 3.

![NoticeDeCalibrationDuKosmosParametrerLa_Capture_dcran_de_20220825_160251_20220825161301_20220825161301](https://user-images.githubusercontent.com/107851441/186863103-32fa5c35-f159-4b01-b506-4a4165b7b9b4.jpg)

avec S une aire de référence, oméga la vitesse de rotation de l’engrenage, R le rayon de l'engrenage et C l’expression du coefficient de couple adimensionné déduit de l’équation de quantité de mouvement de Navier-Stokes.//""</center>""




## 2/ Paramétrage de la pause

La pause d’observation dépend de trois paramètres.
Ces paramètres sont modifiables par le réglage de trois variables présentes dans le code  :

 - **La durée de la pause**
La variable paramétrant la durée de la pause est présente dans le fichier **//kosmos_config.ini//** présent dans la clé de sauvegarde vidéo. 
Modifier la valeur **//SETT_MOTOR_STOP_TIME//** (ligne 12) pour changer le temps de pause, en secondes.
Il ne suffit pas de renseigner 30 secondes pour avoir un arrêt sur secteur de 30 secondes. Il faudra également déduire le temps nécessaire pour entraîner mécaniquement la caméra sur le secteur suivant. Ce temps à déduire est d’autant plus long que la vitesse de rotation du moteur est petite.
La variable **//SETT_MOTOR_STOP_TIME//** désigne donc le temps entre deux ordre de démarrage du moteur. 

 - **La durée de fonctionnement du moteur**
La variable paramétrant la durée de fonctionnement du moteur est également présente dans le fichier kosmos_config.ini présent dans la clé de sauvegarde vidéo. 
Modifier la valeur **//SETT_MOTOR_RUN_TIME//** (ligne 60) pour changer le temps de rotation du moteur.
Cette valeur désigne donc le temps nécessaire pour entraîner le kosmos sur son prochain cran de la croix de malte. Il peut varier de 6 à 20 secondes suivant la vitesse de rotation du moteur.
Cette valeur peut être surévaluée car le stop d’arrêt viendra empêcher le système de tourner de plus d’un cran.  

 - **L’arrêt de la rotation (Top d’arrêt ILS)**
La variable paramétrant l’arrêt de la rotation est présente dans le fichier **//kosmos_main.py//**
L’arrêt de la rotation se fera par le passage régulier d’un aimant dans le champ de détection du capteur ILS top d’arrêt.
Seulement, le champ de détection de l’aimant peut être plus ou moins important suivant les composants,  il est donc important de paramétrer la durée de détection de l’aimant par l’ILS. Si cette durée est trop longue, l’aimant risque d’être détecté deux fois, et le système marquera deux pauses sur le même secteur. 
Dans la procédure **//working()//** (ligne 103)
Une fonction **//time.sleep()//** est renseignée trois fois. 
Dans les parenthèses du **second appel de la fonction** (ligne 141), renseigner le temps pendant lequel l’ILS ne devra pas être détecté. Plus le temps renseigné est long, plus l’aimant aura une chance de sortir du champ de détection sans être détecté une nouvelle fois. Une durée de 4 secondes semble raisonnable. Renseigner alors **//time.sleep(4).//**
Attention à ne pas mettre un temps trop élevé de manière à éviter que le kosmos ne tourne de plusieurs crans.  



## 3/ Procédure :

 - Dans un premier temps, calibrer la durée de fonctionnement du moteur et l’arrêt de la rotation de manière à ce que le KOSMOS tourne et s’arrête secteurs par secteurs. (faire varier SETT_MOTOR_RUN_TIME et time.sleep).

 - Faire ensuite varier la durée de la pause de manière à obtenir 30 secondes de plan fixe par secteurs. (faire varier SETT_MOTOR_STOP_TIME). Il faudra prendre en compte le temps pris par le système de réduction entre le démarrage du moteur et l'entraînement du KOSMOS sur le prochain cran.

 - Ajuster les paramètres de manière à obtenir un système respectant les pauses de 30 secondes dans l'air. Faire ensuite le test dans l'eau et observer la différence de temps d'observation sur la vidéo enregistrée. Réduire le temps exédant en diminuant la variable SETT_MOTOR_STOP_TIME. 

On peut ainsi évaluer **SETT_MOTOR_STOP_TIME + SETT_MOTOR_RUN_TIME ≃ 30**



## Paramétrage de nos KOSMOS

**KOSMOS 1** :
``` 
SETT_MOTOR_STOP_TIME = 14
SETT_MOTOR_RUN_TIME = 20
time.sleep(4)
```
