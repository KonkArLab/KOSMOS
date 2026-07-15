# Vue générale du caisson batterie

<img src="pictures/V4_Batterie/VueGenerale.PNG" height=400>

<img src="pictures/V4_Batterie/CablageBatterie.PNG" height=400> 

# Réalisation de la batterie

On suivra le [tutoriel dédié](../../CommonElements/doc/01_batterie.md) à la fabrication de batterie. Il faudra néanmoins opérer deux modifications mineures :

- ne pas souder le connecteur XT60 sur les cables masse et 12V sortant du BMS
- souder ces deux cables avec un angle de 45 degrés comme la photo qui suit :

<img src="pictures/V4_Batterie/IMG_0926.JPG" height=400> 

- Ces cables doivent mesurer une dizaine de centimètres. On les dénudera sur 7mm. ATTENTION, LES CABLES PROVENANT DE LA BATTERIE NE DOIVENT JAMAIS SE TOUCHER.

# Assemblage des tapes

## Tape avant 

- Assembler le "end cap" sans trou avec son "flange" en suivant le [tutoriel dédié](../../CommonElements/doc/02_flanges.md).

<img src="pictures/V4_Batterie/IMG_1773.jpg" height=200> <img src="pictures/V4_Batterie/IMG_1772.jpg" height=200> 
 <img src="pictures/V4_Batterie/IMG_1774.jpg" height=200> 
 
## Tape arrière

### Assemblage du bouchon 4 trous

<img src="pictures/V4_Batterie/TapeArriere.PNG" height=400> 

- Fixer les deux connecteurs COB-1130, le connecteur COB-1140 et la purge sur le "end cap" 4 trous sur suivant le [tutoriel dédié](../../CommonElements/doc/03_etancheitedivers.md). On respectera l'emplacement de chaque élément de la figure suivante.
- Couper les fils rouge, jaune, noir des deux COB-1130 pour qu'ils mesurent 3 cm et les dénuder sur 7 mm.
- Couper les fils blancs et vert du COB-1140 pour qu'ils mesurent 3 cm et les dénuder sur 7 mm.
- Couper le fil rouge du COB-1140 pourqu'il mesure 7 cm et le dénuder sur 7 mm.
- Couper le fil noir du COB-1140 pourqu'il mesure 5 cm et les dénuder sur 7 mm.

<img src="pictures/V4_Batterie/IMG_1455.JPG" height=400> 


### Connectiques 5V
AVANT DE REALISER LES ETAPES SUIVANTES, S'ASSURER QUE LES CONNECTEURS SONT BIEN PASSES PAR LES TROUS DU BOUCHON.

- Souquer les fils jaunes des COB-1130 et le fil blanc du COB-1140 dans un domino. 
- Plaquer le domino et les fils au plus proche du "end cap".

<img src="pictures/V4_Batterie/IMG_1457.JPG" height=400> 


### Connectiques masse

- Sur une chute de fil noir, couper un fil de 5 cm et la dénuder des deux côtés sur 7 mm.
- Souquer ce fil noir et les deux fils noirs des COB-1130 dans un domino. 
- Plaquer le domino et les fils au plus proche du "end cap".
- Sur l'extrémité restante, sertir une ferrule en prenant soin de choisir le diamètre adapté.

<img src="pictures/V4_Batterie/IMG_1459.JPG" height=400> 


### Connectiques 12V

- Sur une chute de fil rouge, couper un fil de 7 cm et la dénuder des deux côtés sur 7 mm.
- Souquer ce fil rouge, les deux fils rouges des COB-1130 et le fil vert du COB-1140 dans un domino. 
- Plaquer le domino et les fils au plus proche du "end cap".
- Sur les extrémités restantes du fil rouge et du fil noir, sertir une ferrule en prenant soin de choisir le diamètre adapté.


<img src="pictures/V4_Batterie/IMG_1461.JPG" height=400> 

### Un dernier cable noir entre la batterie et le convertisseur 

- Dénuder sur 7 mm les deux côtés d'un fil noir de 7 cm.
- Sertir une ferrule sur une de ses extrémités.

### Assemblage 

- Assembler le "end cap" 4 trous avec son "flange" en suivant le [tutoriel dédié](../../CommonElements/doc/02_flanges.md). Faire en sorte que la vis de purge soit le plus possible aligné avec le détrompeur de la tape.

# Imprimer la structure interne

<img src="pictures/V4_Batterie/StructureMeca.PNG" height=400> 

### Fixation du convertisseur 5V-12V

- Préparer les pas de vis des trous de fixation en vissant un boulon en métal de diamètre 2.5 mm dans les quatre trous qui servent à maintenir le convertisseur.
- Installer le convertisseur à sa place et visser les quatre boulons de diamètre 2.5 mm et de longueur 8 mm. Ces boulons ne doivent pas dépasser du côté de la batterie. Rajouter au pire des rondelles (ou des écrous).

### Connexion des connecteurs avec le convertisseur

Penser à se référer au schéma de a partie "Vue générale du caisson batterie"
- Présenter la structure mécanique en face de la tape de sorte à ce que le haut du convertisseur soit aligné avec le détrompeur de la tape.
- Fixer la ferule du cable noir "masse" sur la borne - du 5 V du convertisseur.
- Fixer la ferule rouge 12 V sur la borne + du 12 V du convertisseur.
- Fixer la ferule du cable noir "5V" (provenant du COB-1140) sur la borne + du 5V du convertisseur.
- Dégager le cable rouge 12V. Il sera raccordé en tout dernier lieu au 12 V rouge de la batterie avec un Wago ou un domino.  

<img src="pictures/V4_Batterie/caisson_batterie_connexions_cables.jpeg" height=400>  

- Fixer l'ensembe "end cap + flange" sur la structure interne imprimée en 3D grâce à trois boulons 3 mm.
- Fixer le dernier cable disponible sur la borne - du 12 V du convertisseur. Dégager l'autre extrémité de ce cable.  Il sera raccordé à la masse noire de la batterie avec un Wago ou un domino.

### Installation de la batterie

ATTENTION, LES CABLES PROVENANT DE LA BATTERIE NE DOIVENT JAMAIS SE TOUCHER.
- Faire passer les fils de la batterie au dessur du convertisseur.
- Installer la batterie dans son compartiment puis la fixer avec un rilsan. L'élément de serrage doit être situé sur le dessus de la batterie.
 
<img src="pictures/V4_Batterie/caisson_batterie_cables_sortants.jpeg" height=400> 

- Connecter les deux cables masse grâce à un Wago ou un domino et tasser ces éléments sur un côté du convertisseur.
- De l'autre côté, connecter les deux cables 12V grâce à un Wago ou un domino et les tasser dans la structure pour qu'ils ne dépassent pas.

## Shunt de fonctionnement

### Soudure

Pour réaliser cette clé de fonctionnement, vous aurez besoin d'un connecteur à sertir COB-3140 et de son outil de sertissage COB-3240.

- Préparer deux morceaux de fils de 1.5 cm et de 2 mm. Dénuder les quatre extrémités sur 3 mm.
  
<img src="pictures/V4_Batterie/IMG_1464.JPG" height=200> 

- Souder le fils le plus court sur le connecteur 4 pin en diagonal.
- Souder l'autre fil dans l'autre diagonale.

<img src="pictures/V4_Batterie/IMG_1465.JPG" height=200> 

- Maintenir la partie métallique du connecteur à sertir dans un étau en faisant attention de ne pas la déformer.
- Enfiler la partie correspondante de l'outil de sertissage (en noir sur la photo suivante) dans ce connecteur.
- Enfoncer l'élément où l'on vient de souder les fils dans l'autre partie de l'outil de sertissage (en bleu sur la photo suivante).

<img src="pictures/V4_Batterie/IMG_1474.JPG" height=300> 

- Superposer les deux éléments de l'outil de sertissage puis enfoncer la partie bleu à l'aide d'un maillet en caoutchouc.
  
<img src="pictures/V4_Batterie/IMG_1475.JPG" height=300> <img src="pictures/V4_Batterie/IMG_1477.JPG" height=300> 

- Une fois que les deux pièces sont en contact, on peut retirer la partie supérieure.

<img src="pictures/V4_Batterie/IMG_1476.JPG" height=300> 

- Déserrer l'étau et récupérer le connecteur et ses contacts maintenant insérés.

### Collage

- Imprimer le bouchon de la clé de fonctionnement en impression résine.

<img src="pictures/V4_Batterie/BouchonShunt.PNG" height=150>

- Préparer le connecteur serti avec sa bague de serrage et son bouchon vissé.

<img src="pictures/V4_Batterie/IMG_1625.JPG" height=200>

- Sous une sorbonne, rassembler de la colle Araldite, une coupelle plastique jetable, un bâton de mélange et une seringue dont on aura coupé le bout. On réalisera le reste de la manipulation avec des gants. 

<img src="pictures/V4_Batterie/IMG_1623.JPG" height=250> <img src="pictures/V4_Batterie/IMG_1490.JPG" height=250> 

- Mettre les deux composants de la colle dans la coupelle et mélanger vigoureusement. 

<img src="pictures/V4_Batterie/IMG_1626.JPG" height=200> 

- Quand le mélange est homogène, l'aspirer avec la seringue et le transvaser dans le connecteur. Remplir presqu'à ras bord.
- Insérer le bouchon en résine et l'enfoncer à fond. Avec le doigt enlever l'excédent de colle.
- Maintenir pendant deux heures dans un serre-joint.

<img src="pictures/V4_Batterie/IMG_1627.JPG" height=200> 

- Accrocher une garcette à la clé de fonctionnement.

<img src="pictures/V4_Batterie/IMG_1628.JPG" height=300> 

# Recharge de la batterie

## Elements pour la recharge

### Shunt de charge

- Raccourcir le cable COB-1241 pour qu'il mesure une vingtaine de centimètres.
- A l'aide du knipex, enlever 3 cm de gaine noire.
- Couper à ras de la gaine noire le fil noir. Couper également le fil blanc pour qu'il n'en reste que 1 cm.
- Enfin, comme ce cable ne servira qu'à terre, ôter son joint à l'aide de l'O-ring pick.
 
 <img src="pictures/V4_Batterie/IMG_1343.JPG" height=200>

- Mettre une gaine thermo-rétractable sur le fil blanc, de sorte à isoler ce contact.
- Dénuder les fils rouge et vert sur un demi-centimètre et les souder ensemble.

<img src="pictures/V4_Batterie/IMG_1345.JPG" height=200> <img src="pictures/V4_Batterie/IMG_1347.JPG" height=200> <img src="pictures/V4_Batterie/IMG_1349.JPG" height=200>

- Mettre une gaine thermo-rétractable sur tous les fils. On essaiera de la faire rentrer dans la gaine noire.
- Glisser enfin un gaine thermo-rétractable sur laquelle on aura écrit "SHUNT CHARGE" sur la gaine noire.

<img src="pictures/V4_Batterie/IMG_1350.JPG" height=200> <img src="pictures/V4_Batterie/IMG_1351.JPG" height=200>

### Cable de recharge (partie 1)

- Avec l'outil Knipex, enlever 4 cm de gaine noire sur le cable COB-1231. Attention à ne pas abimer les fils à l'intérieur. (Si c'était le cas, glisser de la gaine thermoretractable au niveau de la coupure.)
- Enfiler 5 cm de gaine thermoretractable sur la gaine noire
- Couper à ras de la gaine noire le fil jaune. Dénuder les fils rouge et noir sur 5 mm.
- Enfiler un morceau de gaine thermoretractable de 2 cm sur chacun de ces deux fils en choississant leur diamètre afin qu'il puisse recouvrir la cosse du connecteur XT60 femelle.
- Souder les fils rouge et noir sur le connecteur XT60 en respectant les polarités : + sur rouge et - sur noir.
- Faire glisser les gaines thermoretractables et les chauffer.
- Remonter la gaine thermorétractable et la chauffer. 

<img src="pictures/V4_Batterie/IMG_1371.JPG" height=400> 

- Comme ce cable n'a pas vocation à aller sous l'eau, on enlevera le joint de connecteur avec l'outil O-Ring Pick pour faciliter son insertion sur le caisson.

### Cable de recharge (partie 2) 

- Souder deux cables rouge et noir de 10 cm (récup', comme ceux des multimètres) sur un connecteur XT60 mâle en respectant la polarité.
- De l'autre côté, dénuder ces cables sur 3mmn, les étamer et les souquer dans le connecteur femelle fourni avec le chargeur. 

<img src="pictures/V4_Batterie/IMG_1372.JPG" height=400> 

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

