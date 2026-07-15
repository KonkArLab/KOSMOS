# 1. Réalisation de la carte électronique

<ins>Compétences nécessaires
- Soudure électronique
- Sertissage de connecteurs JST (crimp des broches)
- Impression 3D

<ins>Outillage</ins>
- Matériel de soudure (Fer à souder, étain, flux)
- Pince à dénuder
- Pince coupante
- Pince à sertir JST
- Pince à sertir ferrule
- Pince à sertir RJ45
- Pistolet à colle
- Outil KNIPEX
- Clés 14 16 et 17

## 1.1 Préparation des capteurs

### 1.1.1 GPS

<ins>Matériel</ins>
- Puce GPS BDS Beidou Dual Module 
- Broches mâles 5 pins

<img src="pictures/V4_Video/IMG_2090.JPG" height=300>

<ins>Etapes</ins>
- Souder 5 broches sur le capteur GPS (pattes courtes du côté de la pile).   

### 1.1.2 Luxmètre

<ins>Matériel</ins>
- Luxmètre ISL29125
- 1x Connecteur JST droit à souder 5 broches + 2x connecteurs JST femelle 5 pins et les cosses à sertir associées
- 4 fils (RouDge, Vert, Blanc, Noir) d'environ 7cm

<ins>Etapes</ins>
- Souder le connecteur JST 5 broches sur le luxmètre. Les soudures doivent être du côté du capteur lumineux et les encoches du connecteur JST vers l'extérieur du capteur.
  
- Réaliser ensuite la rallonge qui permettra de relier le luxmètre à la carte électronique. Respecter le cablage ci-dessous.
 
<img src="pictures/V4_Video/RallongeLux.PNG" height=300>

<!--
### 1.1.3 Magnétomètre

- Souder 4 broches les pins VCC GND SCL SDA du magnétomètre. Les soudures doivent être du côté du capteur magnétique. Les autres pins sont inutiles.
-->
## 1.2 Soudure de la carte électronique

<ins>Matériel</ins>
- Carte électronique KOSMOS + puce GPS 
- Connecteurs JST droits à souder (2x 2 broches, 4x 4 broches, 1x 5 broches) +
- Bornier à vis
- Bornier 2x20 broches 
- Résistances (1x 0 Ω, 2x 47 Ω, 2x 10 kΩ) 
- 2 LEDs (verte et rouge)

<ins>Etapes</ins>

<img src="pictures/V4_Video/CarteElec.PNG" height=300>

- Se munir du bornier 2x20 broches et de broches dont on se servira pour maintenir le bornier dans sa bonne position.
- Effectuer les soudures puis retirer les broches. 
  
<img src="pictures/V4_Video/IMG_1598.JPG" height=300> 
<img src="pictures/V4_Video/IMG_1599.JPG" height=300> 
<img src="pictures/V4_Video/IMG_1600.JPG" height=300>

- Souder ensuite le bornier en plaçant les accès vers l'intérieur de la carte.
- Souder ensite la résistance 0 ohm puis la résistance 10k ohm.

<img src="pictures/V4_Video/IMG_1601.JPG" height=300> <img src="pictures/V4_Video/IMG_1603.JPG" height=300> <img src="pictures/V4_Video/IMG_1604.JPG" height=300>

- Souder le connecteur JST 2 broches qui recevra le connecteur magnétique avant. L'encoche du JST doit être vers l'intérieur de la carte.
- Souder ensuite la résistance 47 ohm puis la LED verte. (Attention à la polarité de la LED, patte courte sur la masse.)

<img src="pictures/V4_Video/IMG_1605.JPG" height=250> <img src="pictures/V4_Video/IMG_1606.JPG" height=250> <img src="pictures/V4_Video/IMG_1607.JPG" height=250>

- Souder la seconde résistance 10 kohm puis le connecteur JST 2 pin pour l'éclairage. L'encoche doit être vers l'extérieur de la carte.
- Souder ensuite la seconde LED rouge. (Attention à la polarité de la LED, patte courte sur la masse.)

<img src="pictures/V4_Video/IMG_1608.JPG" height=250> <img src="pictures/V4_Video/IMG_1609.JPG" height=250> <img src="pictures/V4_Video/IMG_1610.JPG" height=250>

- Souder les 4 connecteurs JST avec l'encoche vers le bornier bleu.
- Souder la puce GPS.

<img src="pictures/V4_Video/IMG_1612.JPG" height=250> <img src="pictures/V4_Video/IMG_1613.JPG" height=250> <img src="pictures/V4_Video/IMG_1614.JPG" height=250>

- Souder enfin un connecteur JST 5 pin pour le luxmètre. L'encoche doit être du côté du bornier bleu.

## 1.3 Fixation de l'antenne GPS

<ins>Etapes</ins>
- A l'aide d'un pistolet à colle, fixer l'antenne sur le bornier 2x20 broches.
- La brancher ensuite sur le capteur GPS présent sur la carte électronique.

# 2. Intégration mécanique

## 2.1 Impression de la structure 3D

<ins>Matériel</ins>
- PLA
- Fichier hardware/3Dprint_files/V4_CaissonPrincipal/video_stereo.stl

<ins>Etapes</ins>
- Imprimer la structure mécanique à l'aide d'une imprimante 3D filaire (matériau PLA suffisant, pas de nécéssité d'étanchéité pour cette pièce), taux de remplissage 100%.

<img src="pictures/V4_Video/Structure.PNG" height=300>

- A l'aide d'un boulon de diamètre 2.5 mm, tarauder les deux trous destinés à maintenir le luxmètre et les 4 trous destinés à maintenir la caméra. 

## 2.2 Fixation de la caméra

<ins>Matériel</ins>
- Caméra
- 4 vis et 4 écrous (diamètre 2.5 mm  et longueur 10 mm)

<ins>Etapes</ins>
- Pour un rendu de couleurs proche de celui de l'oeil humain, le capteur Picam HQ est équipé d'un filtre infra-rouge se matérialisant par une petite vitre bleue-verte devant le capteur. Ce filtre en plus de couper les infrarouges, atténue également une partie de la lumière rouge. Or celle-ci est déjà fortement atténuée par l'eau de mer. Afin d'éviter une telle perte inutile, le filtre IR du capteur Picam de KOSMOS doit être enlevé. 
- Pour ce faire, un excellent tutoriel existe sur le site officiel de raspberry :  

https://www.raspberrypi.com/documentation/accessories/camera.html#ir-filter

- A l'issue de cette opération, on obtient un capteur Picam HQ sans filtre IR (qui n'aura plus d'utilité par la suite). On en profitera également pour enlever le cache plastique si on utilise une caméra Picam HQ Global shutter (il faudra rajouter une petite rondelle ou un écrou pour compenser la perte d'épaisseur).

<img src="pictures/V4_Video/11.jpeg" height=200> <img src="pictures/V4_Video/9.jpeg" height=200> <img src="pictures/V4_Video/IMG_0904.JPG" height=200>

- Oter également le support de la vis caméra.

<img src="pictures/V4_Video/IMG_1326.JPG" height=200> 

- Fixer la capteur caméra sur la structure à l'aide de 4 vis (diamètre 2.5 mm  et longueur 10 mm). Attention à respecter l'orientation du capteur PICAM. Lorsque l'on regarde le support mécanique par le devant, avec le support de la RPI en bas, la nappe doit se brancher sur la droite.

<img src="pictures/V4_Video/OrientationNappe.PNG" height=200>

## 2.3 Fixation de la Raspberry Pi 

<ins>Matériel</ins>
- Carte Raspberry Pi
- Pile RTC
- Radiateurs
- 4x boulons (M2.5 10mm) + 8x écrous 2.5 + 2x entretoises M2.5 hauteur 20mm
- 4x boulons (M2.5 6mm)
- Nappe
- Luxmètre
- Clé USB (si stockage sur ce support)

<ins>Etapes</ins>
- Fixer les radiateurs sur la carte RPi.  Connecter ensuite le RTC à la RPi via le port BAT. Fixer la pile du RTC au dessus du port Ethernet avec le double face fourni avec le RTC. 

<img src="pictures/V4_Video/19_2.jpeg" height=200> <img src="pictures/V4_Video/19.jpeg" height=200> <img src="pictures/V4_Video/IMG_13300.JPG" height=200>

- Assembler 4 vis (diamètre 2.5 mm et longueur 10 mm) et 4 écrous sur chacun des trous de la RPi de la structure mécanique. Les écrous permettront de surélever légèrement la carte.

<img src="pictures/V4_Video/integration_meca_raspberry3.jpg" height=400>

- Positionner la carte RPi et la fixer avec deux écrous dans les coins avant droit et arrière gauche et avec deux entretoises  (diamètre 2.5 mm, hauteur 20 mm) dans les coins avant gauche et arrière droit.
<img src="pictures/V4_Video/IMG_1330.JPG" height=400>
<img src="pictures/V4_Video/integration_meca_raspberry2.jpg" height=400>
<img src="pictures/V4_Video/integration_meca_raspberry1.jpg" height=400>

- Connecter ensuite la nappe entre le capteur vidéo et la carte RPi.
- Insérer une rehausse 2x20 avec une épaisseur de plastique sur le bornier de la RPi.

<img src="pictures/V4_Video/IMG_1617.JPG" height=300> 

- Insérer la clé USB dans un des deux ports USB 3.0
- Insérer maintenant la carte électronique.
- Fixer enfin le luxmètre avec deux boulons de dimaètre 2.5 mm et de longueur 6 mm : ne pas utiliser d'écrou, il ne faut pas que les boulons dépassent de la structure (il faut donc visser le boulon dans la structure préalablement taraudée)
<img src="pictures/V4_Video/fixation_luxm.jpg" height=400>

- Relier le luxmètre et la carte électronique grâce à la rallonge réalisée plus haut.

<img src="pictures/V4_Video/jj.jpeg" height=400>

# 3. Réalisation du caisson étanche

<img src="pictures/V4_Video/VueGenerale.PNG" height=400>

## 3.1 Assemblage du hublot sphérique

### 3.1.1 Fixation du contacteur magnétique avant

<ins>Matériel</ins>
- 1x Contacteur magnétique
- Gaine thermorétractable
- 2x Connecteurs JST 2 pins
- Broche 2 pins

<ins>Etapes</ins>

- Raccourcir le cable du contacteur magnétique pour qu'il mesure 12 cm.

<img src="pictures/V4_Video/ILSavant.PNG" height=300>

- Dénuder les extrémités et souder une double broche. On pensera à mettre de la gaine thermorétractable pour sécuriser la soudure (possible de refermer la gaine avec la pointe du fer à souder).

<img src="pictures/V4_Video/detrompeur_gaine.jpg" height=200>
<img src="pictures/V4_Video/detrompeur_soudure.jpg" height=200>

- Avec un pistolet à colle chaude, coller le contacteur magnétique comme indiqué sur la photo suivante. Attention à la position du détrompeur (trou + relief de la pièce entourés en rouge).
  
<img src="pictures/V4_Video/IMG_1496.JPG" height=200> <img src="pictures/V4_Video/IMG_1495.JPG" height=200>

- Avec le bout de fil restant, réaliser une rallonge de 10 cm et sertir deux connecteurs JST 2 pins. Pour ce faire :
- Dénuder les cables sur quelques millimètres
- Séparer ensuite sur 1 ou 2 cm les deux câbles pour faciliter la manip
- Sertir enfin un connecteur JST 2 pins :
    - Sertir les extrémités des parties métalliques d'un JST 2 pins sur la partie non dénudée (cf photos) à l'aide de la pince à sertir
    - Assembler les parties métalliques et la partie blanche

<img src="pictures/V4_Video/Sertir_JST_2_pins_1.jpeg" height=200> <img src="pictures/V4_Video/Sertir_JST_2_pins_2.jpeg" height=200> <img src="pictures/V4_Video/Sertir_JST_2_pins_3.jpeg" height=200> 

<img src="pictures/V4_Video/rallonge_interupteur_magnetique.jpg" height=200>

### 3.1.2 Fixation du hublot
  
- Fixer ensuite le hublot sphérique sur le tape.

## 3.2 Assemblage du bouchon arrière

### 3.2.1 Fixation du contacteur magnétique arrière

<ins>Matériel</ins>
- 1x Contacteur magnétique
- 1 Connecteur JST 2 pins

<ins>Etapes</ins>
- Raccourcir le cable du contacteur magnétique pour qu'il mesure 7 cm et y sertir un connecteur JST 2 pin.

<img src="pictures/V4_Video/ILSArriere.PNG" height=300>

- Avec un pistolet à colle chaude, coller le contacteur magnétique comme indiqué sur la photo suivante. Attention à la position du détrompeur.

<img src="pictures/V4_Video/IMG_1494.JPG" height=200> <img src="pictures/V4_Video/IMG_1495.JPG" height=200>

### 3.2.2 Cable d'alimentation

<ins>Matériel</ins>
- Cable COB-1231
- Presse étoupe 6.5 mm HC
- Ferrules à sertir

<ins>Etapes</ins>
- Avec une pince coupante, raccourcir le cable COB-1231 pour qu'il mesure 35 cm. Garder les fils noir, jaune et rouge. 
- Avec l'outil Knipex, enlever de la gaine noire de sorte qu'il n'en reste que 19 cm . Attention à ne pas abimer les fils à l'intérieur.
- Suivre ensuite le tutoriel dont le lien est ci-dessous pour installer le presse étoupe, utiliser une clé de 14 et de 16 pour le serrer 

Tutoriel détaillé : https://bluerobotics.com/learn/wetlink-penetrator-installation-guide/

Tutoriel vidéo : https://www.youtube.com/watch?v=vigY82tsfOI&t=2s&ab_channel=BlueRobotics

<img src="pictures/V4_Video/AlimSimple.PNG" height=300>

- Raccourcir le fil rouge à 3 cm (il ne servira pas) et les fils jaune et noir à 14 cm.
- Dénuder les fils jaune et noir sur 7 mm.
- Sertir des ferrules (dont on a vérifié qu'elles avaient le diamètre optimal) sur les fils jaune et noir. Raccourcir les ferrules de 2 mm.

<img src="pictures/V4_Video/IMG_1421.JPG" height=300>

<!--
#### 3.2.2.2 Avec spot lumineux

<img src="pictures/V4_Video/AlimSpot.PNG" height=300> 

- Raccourcir les fils noir et rouge à 3 cm et le fil jaune à 14 cm.
- Dénuder les trois fils sur 7 mm.
- Sertir une ferrule dont on a vérifié qu'elle avait le diamètre optimal sur le fil jaune. Raccourcir la ferrule de 2 mm.
- Sertir une ferrule sur le fil rouge.

<img src="pictures/V4_Video/IMG_1501.JPG" height=300> 
-->

### 3.2.3 Assemblage de la tape connectique

<ins>Matériel</ins>
- Capteur Température Pression (aussi appelé bar sensor)
- 2x Bouchons
- Connecteur Ethernet - 8 pin
- Connecteur Signal moteur - 4 pin
- Alimentation via le presse étoupe 6.5mm HC (COB-1231 préparé à l'étape "Cable d'alimentation")

<ins>Etapes</ins>

<img src="pictures/V4_Video/TapeArriere.PNG" height=400>

- Graisser les joints de chaque éléments sur la bouchon 7 trous
- Serrer les pièces filetées de 10 mm (type M10) sur le bouchon en respectant les positions de chaque élement. On se servira de clés 16 & 17. ATTENTION à bien respecter la position des ergots sur le bouchon. On suivra l'ordre d'assemblage suivant :
1. Capteur TP
2. Bouchon n°1
3. Ethernet - 8 pin
4. Signal moteur - 4 pin
5. Alimentation - presse étoupe 6.5mm HC
6. Bouchon n°2
7. Purge

<img src="pictures/V4_Video/Purge_avant.png" height=400> <img src="pictures/V4_Video/Purge_arriere.png" height=400>


### 3.2.4 Connectiques 4 pin 8 pin et ethernet

<ins>Etapes</ins>
- Sur le connecteur 4 pin Power Bulkhead COB-1140, raccourcir les cables pour qu'ils mesurent 10 cm.
- Dénuder les fils sur 2 mm puis y sertir des cosses JST. Vérifier qu'elles tiennent fermement.
- De la même façon, couper les cables du capteur Température Pression pour qu'ils mesurent 7 cm.
- Dénuder les fils sur 2 mm puis y sertir les cosses.
- Re-écraser les mords à la pince plate pour que les cosses tiennent fermement. (Les fils du capteur TP sont un peu fins pour les cosses.) 
- Insérer les cosses dans les connecteurs JST en respectant le code couleur des schémas suivante.

<img src="pictures/V4_Video/COBmoteur.PNG" height=200>
<img src="pictures/V4_Video/COBtp.PNG" height=200>

- Sur le connecteur 8 pin Power Bulkhead COB-1180, raccourcir les câbles pour qu'ils mesurent 5 cm et sertir un connecteur ethernet en respectant le code couleur suivant.
ATTENTION : ne pas dénuder les câbles avant de les sertir !

<img src="pictures/V4_Video/COBrj45.PNG" height=300>

<img src="pictures/V4_Video/Ethernet.PNG" height=300>  <img src="pictures/V4_Video/IMG_1356.JPG" height=300>
<!--
### 3.2.5 Connexion Spot lumineux

/!\ Spot lumineux
- A faire uniquement si vous élaborez votre caméra avec celui-ci et que vous avez bien fait l'étape 3.2.2.2

<ins>Matériel</ins>
- Câble d'alimentation réalisé à l'étape 3.2.2.2
- Spot lumineux
- Connecteur JST 2 pins
- 2 Dominos
- Ferrules
- Câble fin noir de 11 cm

<ins>Outils</ins>
- Pince coupante
- Pince à dénuder
- Petit tournevis plat

<ins>Etapes</ins>
- Réaliser le cablage suivant :

<img src="pictures/V4_Video/CablageSpot.PNG" height=300> 

- Raccourcir tout d'abord les cables rouge et noir du spot à 3 cm.
- Raccourcir ensuite le cable signal jaune à 10 cm et y sertir un connecteur JST 2 pins. Insérer cette unique pin dans le connecteur JST 2 pins, attention à respecter le schéma de cablage. 

<img src="pictures/V4_Video/IMG_1503.JPG" height=300> 

- A l'aide d'un domino, relier les fils noir provenant de l'alimentation et du spot lumineux ainsi qu'un troisième mesurant 11 cm au bout duquel on aura serti une ferrule.
- Plaquer ce domino au plus près du bouchon.
- Sertir une ferrule sur le fil rouge raccourci du spot lumineux
  
<img src="pictures/V4_Video/IMG_1506.JPG" height=300>

- A l'aide d'un domino, relier les fils rouges (avec les ferrules) provenant de l'alimentation et du spot lumineux.
- Plaquer ce domino au plus près du bouchon.

<img src="pictures/V4_Video/IMG_1507.JPG" height=300>
-->
# 4. Assemblage final

## 4.1 Fixation du bouchon 7 trous sur la tape arrière

<ins>Etapes</ins>
- Graisser le joint de la gorge de la tape arrière et l'y placer.
- Présenter le bouchon 7 trous devant la tape arrière, de sorte à ce que la purge soit alignée avec le détrompeur de la tape.
- Fixer le bouchon sur la tape à l'aide des 6 vis (on les serrera en étoile).

<img src="pictures/V4_Video/IMG_1424.JPG" height=400>

## 4.2 Fixation de la tape arrière sur la structure interne

<ins>Matériel</ins>
- Tape arrière avec les câbles
- Structure interne mécanique
- 4x boulons (M3, longueur 10 mm)

<ins>Etapes</ins>
- Connecter l'ethernet à la Raspberry et faire passer tous les autres cables vers l'avant du caisson (notamment ceux du contacteur magnétique).
- Fixer la tape arrière sur la structure mécanique à l'aide de 4 boulons (diamètre 3 mm, longueur 10 mm). On placera le détrompeur de la tape du côté des ports USB. 

<img src="pictures/V4_Video/IMG_1511.JPG" height=400>

## 4.3 Branchement de la carte électronique

<ins>Etapes</ins>
- Connecter le capteur TP et le contrôle moteur sur la carte.
- Insérer les cosses de l'alimentation 5V dans le bornier et les souquer à l'aide d'un tournevis cruciforme.
- Connecter le contacteur magnétique arrière à la carte et la rallonge du contacteur avant. On fera ressortir l'autre côté de la rallonge vers l'avant, sous la caméra. 

<img src="pictures/V4_Video/Branchement_moteur.png" height=400>

# 5. Réalisation du cable de récupération des données

<ins>Etapes</ins>
- Sur le connecteur COB-1281, ôter le joint grâce à l'outil O-ring Pick. (Ce cable ne servant qu'à terre, le joint est inutile. L'enlever permettra d'insérer plus facilement le connecteur sur le caisson)
- Sertir ensuite un connecteur ethernet en respectant l'ordre de la figure qui suit.

<img src="pictures/V4_Video/Ethernet.PNG" height=300> <img src="pictures/V4_Video/IMG_1357.JPG" height=300>
