# Procédure de récupération des données 

## Configuration du PC windows

Étape 1 : Accéder aux Propriétés Réseau
- Faire un clique droit sur l'cône réseau de la barre de tâches puis `Ouvrir les paramètres réseau et Internet`

<img src="./pictures/05_Procedures/Image1.png" width="300">

- Dans `Paramètres réseau avancés` cliquer sur `Modifier les options d'adaptateur`

<img src="./pictures/05_Procedures/Capture.PNG" width="400">

- Localisez votre adaptateur Ethernet, faire un clique droit dessus, puis `Propriétés`.

<img src="./pictures/05_Procedures/Image2.png" width="300">

- Double-cliquer sur `Protocole Internet version 4 (TCP/IPv4)`

<img src="./pictures/05_Procedures/Image3.png" width="300">
  
- Changez le mode d'attribution d'IP Automatique (DHCP) vers pour la définir manuellement.
- Remplissez le champ `Adresse IP` avec 192.168.10.1
- Remplissez le champ `Masque de sous-réseau` (Subnet mask) avec 255.255.255.0
- Passerelle (Gateway) : laisser vide
- DNS préféré (Preferred DNS) : laisser vide
- Cliquez sur `OK`

<img src="./pictures/05_Procedures/Capture3.PNG" width="300">

## Téléchargement à partir du logiciel KOSMOS

- Installer le logiciel [Bitvise](https://bitvise.com/) puis le lancer.

<img src="./pictures/05_Procedures/Bitvise1.PNG" width="300">

- Rentrer `192.168.10.2` dans le champ `Host`, puis `kosmos` dans le champ `username`.  Cliquer sur `Log In`.

<img src="./pictures/05_Procedures/Bitvise2.PNG" width="300">

- Taper le mot de passe `kosmos` puis `Ok`.
- Cliquer ensuite sur l'icône `New SFTP Window`.

<img src="./pictures/05_Procedures/Bitvise3.PNG" width="100">

- Dans la fenêtre de droite taper l'adresse `/media/kosmos`. Le nom de votre clé USB devrait apparaître (ici Lexar 256).

<img src="./pictures/05_Procedures/Bitvise4.PNG" width="300">

- Double cliquer sur la clé usb puis clique droit sur le dossier à télécharger.

<img src="./pictures/05_Procedures/Bitvise5.PNG" width="300">

- Appuyer sur `Download` pour télécharger le dossier. Cela peut prendre quelques minutes.
- (Supprimer ensuite les vidéos après avoir vérifié que le téléchargement s'est bien déroulé.)


# Procédure de mise au point de la caméra 

Cette section a pour vocation d'expliciter la méthode pour faire la mise au point de la caméra, que ce soit juste après la réalisation du caisson ou lors d'une maintenance. Pour cette opération il faudra :
- un ordinateur portable avec RealVNC  
- la caisson caméra et le caisson batterie

## Fabrication de la mire

- Imprimer la mire à partir du [pdf](Mire.pdf)
  
<img src="./pictures/05_Procedures/Mire.PNG" width="400">

- Imprimer le support de mire à partir du fichier 3D

<img src="./pictures/05_Procedures/SupportMire.PNG" width="400">

- Couper la mire de sorte à ce qu'elle puisse être collée (scotch double face) sur la face intérieure du support.

## Nettoyage des optiques

- Oter le hublot sphérique
- Dévisser l'objectif Edmund et nettoyer toutes les surfaces avec un chiffon microfibre
- Regarder le capteur pour vérifier si des poussières sont présentes. Les chasser avec de l'air sec si certaines sont visibles. ATTENTION, ne pas toucher le capteur ! ni souffler dessus avec la bouche (risque de projections) !
- Remonter l'objectif Edmund sur le capteur.

## Démarrage de la RPi et connexion VNC

- Brancher la clé de fonctionnement sur le caisson batterie. Attendre que la RPi soit démarrée.
- Sur l'ordinateur portable, se connecter au WiFi généré par le KOSMOS. 
- Ouvrir un navigateur et taper `10.42.0.1` pour avoir accès à l'interface web.
- Modifier le paramètre `06_shutdown` pour le mettre à `0` et effectuer un `Reboot`.
- Aller ensuite dans la page `Camera` et arrêter le logiciel embarqué KOSMOS en appuyant sur `Shutdown`. (Cette manipulation permet d'arrêter le script KOSMOS sans éteindre la Rpi. La caméra peut ainsi être utilisée.)
- Sur l'ordinateur portable, ouvrir RealVNC et se connecter à l'adresse `10.42.0.1`.

<img src="./pictures/05_Procedures/VNC1.PNG" width="500">

- Cliquer sur `Continuer`  si un message d'erreur apparaît puis rentrer les identifiants de connexion. (Normalement id: `kosmos` et mdp: `kosmos`)

<img src="./pictures/05_Procedures/VNC2.PNG" width="500"> <img src="./pictures/05_Procedures/VNC3.PNG" width="500">

## Mise au point
- Ouvrir un terminal et taper :  
```
cd kosmos_software
python3 kosmosCamFocus.py
```
- Deux fenêtres apparaissent. Agrandir l'image qui correspond au champ de vue de la caméra.

<img src="./pictures/05_Procedures/VNC4.PNG" width="600">

- Placer la mire et son support à la place du hublot sphérique.
- Ouvrir à fond l'objectif, c'est-à-dire mettre le petit point blanc devant 1.8. (On a alors avoir une profondeur de champ minimale.)

<img src="./pictures/05_Procedures/IMG_1378.JPG" width="200">

- Sur la fenêtre de la caméra, cliquer pour tracer un trait de part et d'autre du damier. On pourra zoomer sur la mire grâce à la molette de la souris.
- Réaliser le focus sur la mire avec la bague en essayant d'avoir les bords les plus francs possible.

<img src="./pictures/05_Procedures/VNC5.PNG" width="400"> <img src="./pictures/05_Procedures/VNC6.PNG" width="400">

- Bloquer la bague de focus solidement à l'aide de la petite vis.
- Fermer enfin l'objectif à moitié (le petit point blanc sur 2.8) pour récupérer une meilleure profondeur de champ. Bloquer la bague d'ouverture dans cette position. Vérifier que le focus est toujours bon (le fait de serrer les bagues peut parfois les faire bouger.)

<img src="./pictures/05_Procedures/IMG_1379.JPG" width="200">

  
- (Effectuer éventuellement cette opération sur la deuxième caméra (mode stéréo), en basculantde vue grâce au curseur en bas de la fenêtre vidéo.)

## Fin de la procédure
- Quitter l'interface de mise au point en fermant la console.
- Redémarrer la Raspberry Pi. Le soft kosmos va se remettre en route.
- Se reconnecter au Wifi de la Rpi, aller à 10.42.0.1 et remettre le paramètre  `06_shutdown` sur 1. Effectuer un `Reboot` puis éteindre le système avec un `Shutdown`.
- La mise au point est effectuée. Remettre le hublot sphérique et le sécuriser avec la bride.

# Procédure de mise-à-jour du logiciel

Cette section décrit la procédure pour mettre à jour le logiciel KOSMOS. Pour ce faire, on aura besoin de :
- un cable de transfert de données
- un ordinateur portable avec RealVNC
  
On notera qu'il n'est pas nécessaire de démonter le système pour effectuer cette màj.

- Brancher le cable de récupération de données au caisson vidéo et à une prise internet.
- Démarrer le système Kosmos, en branchant le shunt de fonctionnement sur le caisson batterie.
- Sur l'ordinateur portable, se connecter au WiFi généré par le KOSMOS.
- Avec RealVNC, se connecter au `10.42.0.1`
- Ouvrir un terminal et taper :  
```
cd kosmos_software
sh InternetActif.sh
```
Cette opération a pour but de rétablir l'accès à Internet qui était désactivé pour le transfert de données via le port ethernet.
- Effectuer la mise à jour du logiciel en tapant dans le terminal :
```
git pull
```
- On peut désormais remettre en fonction le transfert de données. Pour ce faire, taper dans le terminal :
```
sh TransfertDonneesActif.sh
```
- Eteindre finalement la Raspberry.
