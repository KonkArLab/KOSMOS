# Réalisation de la batterie
Guide pour fabriquer une batterie pour la caméra KOSMOS 3.5
Caracéristiques : 3S3P 12,6V 9,6Ah 120Wh

## Contenu du kit
- x9 accumulateurs Li-ion 3.6V 3500mAh
- x1 BMS Daly 3S 12V 15A + son câble d'équilibrage
- x2 supports de cellules imprimés en 3D
- x4 bandes de nickel 0.1mm x 4mm x 100mm
- x1 connecteur XT30 femelle
- fil rouge
- gaine thermorétractable diamètre 4mm
- rouleau de scotch électrique noir
- petit collier de serrage noir

## Outils et consommables nécessaires
- soudeuse par point
- fer à souder
- bobine d'étain
- pistolet à air chaud ou briquet
- voltmètre
- pince à dénuder de précision
- pince coupante
- paire de ciseaux
- gants et lunettes de protection

## Consignes de sécurité
ATTENTION, L'ESPACE DE TRAVAIL DOIT ETRE PROPRE ET SANS PARTIES METALIQUES AUX RISQUES DE PROVOQUER DES COURTS CIRCUITS

## Chapitre 1 : Assemblage des cellules
- vérifier avec le voltmètre que les cellules soient identiques et supérieurs à 3V
- ébavurer les supports imprimés en 3D pour faciliter l'insertion des cellules
- installer les 9 cellules dans le support selon la photo (le côté avec la pastille blanche est le pôle +)
- emboiter le 2ème support par dessus, retourner la batterie et marquer le 1er support en noir pour identifier le côté avec la masse de la batterie

## Chapitre 2 : Soudure des cellules
- couper 7 bandes de nickel à l'aide de la pince coupante selon les longueurs suivantes :
	- longueurs côté noir 85mm / 50mm / 25mm
	- longueurs autre côté 65mm / 45mm / 25mm / 25mm
- commencer d'abord par souder la face noire
- placer les bandes de nickel selon la photo puis les souder unes à unes en commencant aux extremités
- mettre le scotch de peinture sur les zones où l'on ne travail pas pour éviter les erreurs et les courts circuits

## Chapitre 3 : Assemblage du BMS sur le pack

### Préparation du BMS
- couper et dénuder le fil bleu B- du BMS à 28mm
- couper et dénuder le fil rouge à 135mm
- couper la gaine thermo pour la positionner sur B- et le fil rouge
- régler le fer à 350°C et souder le connecteur XT30 sur le fil bleu B- et sur le fil rouge
- positionner et faire fondre la gaine thermo
- étamer le fil noir P- et le fil rouge P+
- souder le connecteur XT30

### Préparation des câbles d'équilibrage
- couper et dénuder les fils du connecteur d'équilibrage selon les longueurs suivantes
	- fil noir : 145mm
	- fil rouge 1 : 50mm
	- fil rouge 2 : 135mm
	- fil rouge 3 : 60mm
	
### Soudure du pack
- étamer les bandes de nickel selon la photo suivante
- souder le BMS au pack en soudant le fil noir P- et le fil rouge
- souder les câbles d'équilibrage aux bandes de nickel selon la photo
- checker toutes les tensions sur le connecteur d'équilibrage par rapport à P- (on doit retrouver environ 0V,4V,8V,12V)
- brancher le connecteur d'équilibrage au BMS
- scotcher les câbles et la sonde de températures
- attacher les câbles bleu P- et rouges essembles à l'aide du collier de serrage

## Chapitre 4 : Test et recharge de la batterie
- Vérifier la tension de la batterie aux bornes du connecteur XT30
![controle_tension](../pictures/controle_tension.jpg){width="300"}
- Régler une alim de labo sur 12,6V 3A
- Brancher l'alim aux connecteur jaune XT30 de la batterie 
- Vérifier la recharge de la batterie en observant le courant
 ![batterie_finale](../pictures/batterie_finale.jpg){width="500"}