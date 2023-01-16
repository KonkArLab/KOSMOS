# Appropriation des modèles 3D pour modifications

Cette documentation détail l'usage desmodèles 3D modifiables partagés dans ce GitHub. Ce dossier se trouve au bout du chemin suivant : hardware/3Dmodels_editable. 
Les présents dossiers contiennent tous les fichiers nécéssaires pour modifier le dessin 3D du KOSMOS. Il est indispensable pour les modifier d'utiliser le logiciel [Autodesk Fusion 360, une licence gratuite pour usage personnelle suffira](https://www.autodesk.fr/products/fusion-360/personal-form).

Les fichiers Modifiables portent l’extension ".f3D". Tandis que les assemblages portent l'extension ".f3z".


## 1/ Hiérarchisation des dossiers
Le dossier d'archive (3D_KOSMOS) est organisé selon 4 sous-dossiers :
 - **Assemblages :** Contient les fichiers ".f3z" d'assemblages. Les fichhiers d'assemblages nécéssitent que tout les fichiers pièces compris dans l'assemblage soient déjà importés sur Fusion. 
 - **Intérieur :** Contient les fichiers 3D des pièces structurant les composants contenu dans le caisson. 
 - **Réducteur :** Contient l'ensemble des pièces servant à construire le réducteur
 - **Autres :** Contient les petites pièces qui ont été utiles au projets mais qui ne servent pas au KOSMOS directement. 
 
 
## 2/ Détails des fichiers 

### 2.1. Assemblages
 - **Assemblage_Axe_primaire_KOSMOS3-0.f3z :** Sous assemblage de l'arbre primaire celui contenant la croix de Malte. 
 - **Assemblage_ber_KOSMOS3-0.f3z :** Sous assemblage du ber_dessus et ber_dessous permettant de solidariser le réducteur au caisson. 
 - **Assemblage_croix_de_malte_KOSMOS3-0.f3z :** Sous assemblage, contenant la croix de malte seule. 
 - **Assemblage_Engrenage_KOSMOS3-0.f3z :** Sous assemblage d'un engrenage (petit et grend pignons).
 - **Assemblage_moteur_KOSMOS3-0.f3z : ** Sous assemblage, du moteur vissé sur son support et son pignon d'entrainement. 
 - **Assemblage_Reducteur_KOSMOS3-0.f3z :** Assemblage final du réducteur. 

*Notes : Il n'existe plus d'assemblage à jour de la structure interne et de son caisson.*


### 2.2. Intérieur
Les pièces de l'intérieur du caissons sont nommés "structures" pour les pièces cylindrique épousant l'intérieur du caisson.

 - **Structure_batterie_KOSMOS3-0.f3d :** Anneau permettant de lier le structure de la Raspberry avec le  support de batterie et PCB. 
 - **Structure_camera_KOSMOS3-0.f3d :** Pièce permettant de positionner la caméra. Elle recevra également le support de batterie. 
 - **Structure_hublot_KOSMOS3-0.f3d :** Anneau qui sera solidaridé à la flange du Hublot. Elle est un guide pour insérer l'intérieur du tube dans le bon sens. 
 - **Structure_raspberry_KOSMOS3-0.f3d :**  Pièce permettant de positionner le support de Raspberry dans le tube. 
 - **Support_batteries_PCB_KOSMOS3-0.f3d :** Plaque supportant les batteries et le PCB.
 - **Support_raspberry_KOSMOS3-0.f3d :** Plaque supportant la raspberry. Elle est vissé sur la structure correspondante.



### 2.3. Réducteur

 - **ber_dessous_KOSMOS3-0.f3d :** Le "ber" désigne traditionellement une pièce permettant de soutenir un bateau sur la terre et ainsi d'éviter qu'il ne se couche. Nous utilisons ce mot pour désigner la pièce qui permet de solidariser le tube du KOSMOS au réducteur. Elle se compose en 2 partie (dessus/dessous) et se comptent au nombre de 2 par système. 
 - **ber_dessus_KOSMOS3-0.f3d :** Il s'agit de la pièce complémentaire au be-dessous. 
 - **Bras_de_Malte_seul_KOSMOS3-0.f3d :** Le KOSMOS tourne sur lui même par 6 séquences de 60°. La croix de Malte est le mécanisme qui permet de transformer un mouvement de rotation continue en mouvement de rotation sacadé. Le Bras est la pièce menant la croix de Malte. 
 - **Carter_AvAr_KOSMOS3-0.f3d :** Cloison du réducteur avant et arrière. Elle n'a aucune utilité mécanique mais permet de fermer le réducteur et ainsi d'aviter l'intrusion de corps étranger. 
 - **carter_dessous_KOSMOS3-0.f3d :** Cloison du réducteur du dessous. Cette pièce est également une pièce structurant le réducteur.
 - **Carter_dessus_KOSMOS3-0.f3d :** Cloison du réducteur du dessus. Cette pièce est également une pièce structurant le réducteur. 
 - **Carter_GD_KOSMOS3-0.f3d :** Cloison du réducteur gauche et droite. Elle n'a aucune utilité mécanique mais permet de fermer le réducteur et ainsi d'aviter l'intrusion de corps étranger. 
 - **connecteur_ILS_KOSMOS3-0.f3d :** Les connecteurs sont des pièces à imprimer en 3D qui servent à placer des raccords de câbles électriques puis de les noyer dans la résine pour en garantir l'étanchéité. Celui-ci est destiné à faire les racords pour les câbles du capteur mgnétique.
 - **connecteur_moteur_KOSMOS3-0.f3d :** Comme la pièce précédente il s'agit d'un réceptacle pour une connexion électrique qui pourra être étanché au moyen de résine epoxy. A la différence que celui-ci est destiné aux câbles du moteur. 
 - **couvercle_connecteur_ILS_KOSMOS3-0.f3d et couvercle_connecteur_moteur_KOSMOS3-0.f3d : ** Il s'agit là de couvercles que l'on peut ytiliser pour fermer les connecteurs. Mais ils ne sont pas indispensables. 
 - **Croix_de_malte_seule_KOSMOS3-0.f3d :** Le KOSMOS tourne sur lui même par 6 séquences de 60°. La croix de Malte est le mécanisme qui permet de transformer un mouvement de rotation continue en mouvement de rotation sacadé. Il s'agit d'une pièce très importante. Pour en modifier les dimentions préférer le modèle "croix_malte_et_bras_parametrique_KOSMOS3-0.f3d" qui permettra de modifier les dimensions du bras d'un seul coup. En revanches les assemblages utilisent les fichiers du bras et de la croix seules.
 - **croix_malte_et_bras_parametrique_KOSMOS3-0.f3d :** Pour modifier les dimensions du bras et de la croix de Malte. 
 - **Entretoise_arbre_croix_de_malte_KOSMOS3-0.f3d :** Tube pour l'axe primaire. Ce modèle ne sert qu'à l'assemblage 3D. L'usiner dans un tube d'inox A4 de 10/8mm.
 - **Entretoise_arbre_secondaire_KOSMOS3-0.f3d :** Tube pour l'axe secondaire. Ce modèle ne sert qu'à l'assemblage 3D. L'usiner dans un tube d'inox A4 de 10/8mm.
 - **entretoise_dessus_arbre_secondaire_KOSMOS3-0.f3d :** Petite pièce à imprimer en 3D, elle sert à dissocier la rotation des engrenages de celle de la croix de Malte. (Arbre primaire pas secondaire)
 - **entretoise_moteur_KOSMOS3-0.f3d :** Pièce à imprimer en 3D, dont la hauteur précise permet d'aligner correctement le pignon du moteur avec le premier grand pignon. Il sert également à protéger le moteur de l'extérieur. 
 - **extrémité croix de malte_KOSMOS3-0.f3d :** Il s'agit d'une pièce importante elle sert à transmettre l'effort de la croix de Malte à la tige fileté permettant ainsi au KOSMOS de pivoter sur lui-même. Son diamètre doit-être ajusté pour limiter le jeu avec le carter du dessous sans empêcher la rotation de ces deux pièces l'ine par rapport à l'autre. Cette pièce gagnerai à être usiné dans une masse de plastique au tour par exemple. 
 - **extrémité croix de malte_KOSMOS3-0.f3d :** A ce jour nous n'avons jamais essayé de fabriquer cette dernière pièce à la fraiseuse. Cependant nous avions commencés à y réflaichir. Ce modèle est ce que nous avions fait. 
 - **GdPignon_bras_de_malte_KOSMOS3-0.f3d :** Pignon (engrenage) destiné à se visser avec le bras de Malte. 
 - **GdPignon_KOSMOS3-0.f3d :** Pignon (engrenage) de grand-diamètre donc il s'agit des pignons menées. 
 - **Moteur-F2838-350KV_KOSMOS3-0.f3d :** Moteur, pour assemblage uniquement. Cette pièce est à acheter. 
 - **Pignon_moteur_KOSMOS3-0.f3d :** Pignon à visser sur le moteur, c'est le pignon meneur. 
 - **Pt_Pignon_entretoise_KOSMOS3-0.f3d :** Sur KOSMOS 3.0, les engrenages sont constitués de 3 pignons vissés entre eux. 1 grand pignon dans lequel est logé la tte de vis, et deux petit. Dont un fait office de simple rondelle (la vis n'y fait que passer), la seconde sert d'écrou. 
 - **Pt_pignon_serrage_KOSMOS3-0.f3d :** Ce pignon à la différence du précédent à des trous de plus petit diamètre afin que les vis à méteaux taraude la plastique et maintienne les 3 pignon l'un contre l'autre. 
 - **Rondelle-rotation_arbre_croix_de_malte_KOSMOS3-0.f3d :** Une simple entretoise pour empêcher les pignons de coulisser sans les empêcher de tourner. 
 - **Support_capteur_ILS_KOSMOS3-0.f3d :** Cette pièce se visse sous le réducteur et permet de maintenir en place le capteur magnétique. 
 - **Support_moteur_KOSMOS3-0.f3d :** Cette pièce est un disque percé à usiner en plastique qui permet de solidariser le moteur au carter du réducteur. 
 

### 2.4. Autres
 - **Adaptateur_paralenz_caisson_moteur.f3d :** L'équipe en mer utilise encore parfois les vieux caissons moteur surmonté d'une caméra Paralenz. Ce modèle permet de raccorder le caisson moteur (vis de serrage) avec le support de la Paralenz. 
 - **Porte_aimant_KOSMOS3-0.f3d :** Petite pièce permettant de placer un aimant carré néodyme (que l'on trouve chez bureau vallée à côté du FabLab). Il permet une bonne prise en main en mer. 
 - **Presentation_pc_print_KOSMOS3-0.f3z :** Cet assemblage m'a permis de faire un visuel pour présenter toutes les pièce sà imprimer en 3D sur une seule image. Le rendu est visible dans l'étape de "Fabrication des pièces". 