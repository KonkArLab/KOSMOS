# Réalisation de la batterie

On suivra le [tutoriel dédié](../../CommonElements/doc/01_batterie.md) à la fabrication de batterie. Il faudra néanmoins opérer deux modifications mineures :

- ne pas souder le connecteur XT60 sur les cables masse et 12V sortant du BMS
- souder ces deux cables avec un angle de 45 degrés comme la photo qui suit :

<img src="pictures/V4_Batterie/IMG_0926.JPG" height=400> 

- Ces cables doivent mesurer une dizaine de centimètres. On les dénudera sur 7mm. ATTENTION, LES CABLES PROVENANT DE LA BATTERIE NE DOIVENT JAMAIS SE TOUCHER.

### Installation de la batterie

ATTENTION, LES CABLES PROVENANT DE LA BATTERIE NE DOIVENT JAMAIS SE TOUCHER.
- Faire passer les fils de la batterie au dessur du convertisseur.
- Installer la batterie dans son compartiment puis la fixer avec un rilsan. L'élément de serrage doit être situé sur le dessus de la batterie.
 
<img src="pictures/V4_Batterie/caisson_batterie_cables_sortants.jpeg" height=400> 

- Connecter les deux cables masse grâce à un Wago ou un domino et tasser ces éléments sur un côté du convertisseur.
- De l'autre côté, connecter les deux cables 12V grâce à un Wago ou un domino et les tasser dans la structure pour qu'ils ne dépassent pas.

## Test du niveau de charge

- Brancher la partie 1 du cable de recharge sur un connecteur 3 pin du caisson batterie. (Au besoin déconnecter le moteur ou le caisson vidéo.)
- Brancher les deux connecteurs bananes de la partie 2 du cable de recharge sur un multimètre réglé en mesure de tension continue.

<img src="pictures/V4_Batterie/IMG_1409.JPG" height=400>

- Relier les connecteurs XT60 des deux parties du cable de recharge.
- Brancher le shunt de charge sur le connecteur 4 pin de la batterie.

 <img src="pictures/V4_Batterie/IMG_1408.JPG" height=400> 

- Observer la tension et recharger la batterie (paragraphe suivant) si la tension est inférieure à 11.5V

## Recharge de la batterie

- Brancher la partie 1 du cable de recharge sur un connecteur 3 pin du caisson batterie. (Au besoin déconnecter le moteur ou le caisson vidéo.)
- Brancher les deux connecteurs bananes de la partie 2 du cable de recharge sur une alimentation stabilisée dont on règlera la tension à 12.5V
- Mettre pour le moment le courant à 0 ampère.
- Relier les connecteurs XT60 des deux parties du cable de recharge.
- Brancher le shunt de charge sur le connecteur 4 pin de la batterie. La tension affichée est normalement maintenant inférieure à 12.5V Elle correspond à la tension de la batterie.
- Augmenter avec précaution le courant jusqu'à 3A. La batterie est en charge. 
- Attendre que la tension atteigne la consigne 12.5V (et le courant 0A). Cela peut prendre plusieurs heures.
- Redescendre le courant.
- Enlever le shunt de charge.
- Déconnecter les XT60.
- Déconnecter les bananes de l'alimentation stabilisée et l'éteindre.
- Déconnecter le cable de charge 3 pin du caisson batterie.