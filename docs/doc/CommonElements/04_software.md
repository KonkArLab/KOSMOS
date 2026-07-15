# Kosmos Software

## Fonctionnement général du KOSMOS

On présente dans cette section, la façon dont fonctionne le système KOSMOS d'un point de vue de son logiciel embarqué. Il est basé sur une succession d'*états* s'enchainant automatiquement ou suivant l'intervention de l'opérateur et correspondant à des opérations différentes. 5 états du KOSMOS existent :
 - **STARTING** : kosmos est en train de démarrer, c'est un temps d'initialisation des différents modules 
 - **STANDBY** : kosmos est en attente d'instructions 
 - **WORKING** : kosmos enregistre
 - **STOPPING** : kosmos termine l'enregistrement 
 - **SHUTDOWN** : kosmos passe à l'arrêt total
   
Seuls les états **STANDBY** et **WORKING** permettent d'interagir avec le système.

### Mode STAVIRO et mode MICADO

Il existe deux modes de fonctionnement du système suivant les objectifs d'observation. Le mode **STAVIRO** (pour STAtion VIdeo ROtative) vise à réaliser de nombreuses stations à des emplacements différents durant une journée de campagne. Il faudra donc pouvoir mettre en route puis stopper l'enregistrement à chaque pose/dépose du système. L'opérateur *pilote* donc l'instrument dans ce mode **STAVIRO**. 

Le second mode **MICADO** correspond à un besoin d'observation longue durée en point fixe. Autrement dit, la caméra est fixée sur le fond de l'eau pour une longue durée et réalise de façon autonome des vidéos à intervalles réguliers. Dans ce mode, les états du KOSMOS s'enchainent, l'opérateur n'a pas à intervenir pour lancer la vidéo. 

Les deux graphiques qui suivent résument ces deux modes de fonctionnement. 

<img src="./pictures/04_Software/ModeStaviro.png" height="500"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <img src="./pictures/04_Software/ModeMicado.png" height="500"> 

- Les flèches noires en ligne continue correspondent à un processus automatique (soit immédiat, soit avec un temporisation via les paramètres `03_tps_fonctionnement` ou `04_tps_veille`), aucune action de l'opérateur n'est nécessaire pour que le système *avance* d'un état à l'autre.
- Les flèches noires en pointillés nécessitent l'intervention d'un opérateur via un *bouton* (`Start` `Stop` ou `Shutdown`) de l'interface Web (dont on reparlera plus bas).
- À l'intérieur d'un état, plusieurs issues sont parfois possibles suivant l'action de l'opérateur ou le passé des opérations du système. Les flèches grises témoignent de ces possibilités : 

<img src="./pictures/04_Software/Instruction.png" height="200"> 

À noter que dans le mode **MICADO**, un état supplémentaire existe : celui de **VEILLE**. Dans cet état, la Raspberry Pi est quasiment éteinte à ceci près qu'elle a été programmée pour se redémarrer à un instant donné pour reprendre une vidéo. Dans l'état de **VEILLE**, la communication avec la RPi est impossible car elle ne génère aucun WiFi. La seule façon pour recommuniquer avec le système consiste à couper le courant avec le Switch puis à le remettre pour redémarrer la RPi.  

## Mode d'emploi de l'interface web

Une IHM (Interface Homme Machine) a été développée pour commander Kosmos depuis un téléphone ou un ordinateur portable. Elle complète les commandes historiques à réaliser avec des aimants sur les contacteurs magnétiques. (À noter que le pilotage avec les aimants reste opérationnel sur les systèmes où il y a des ILS.)

Sur un téléphone ou un ordinateur portable:
 - Se connecter au réseau  WiFi de la raspberry qui a été créé dans les étapes précédentes typiquement `KosmosWeb`.  
 - Dans un navigateur web, générer une fenêtre de navigation privée et entrer l'adresse `10.42.0.1` pour accéder à l'interface de commande du KOSMOS. 
La fenêtre suivante apparaît :

<img src="./pictures/04_Software/Capture3.PNG" width="300">

4 onglets sont disponibles à partir de cette page :

 - `Campaign` qui permet de renseigner les informations liées à la campagne journalière.
 - `Configuration` qui permet de configurer le système
 - `Camera` qui permet de lancer l'enregistrement des vidéos, de tester si la caméra fonctionne correctement et d'éteindre le système
 - `Records` qui permet de voir les vidéos enregistrées et leur lieu de stockage
   
A noter que l'adresse `10.42.0.1` renvoie directement vers la page `Camera`.

### Page `Camera`

Sur la page `Camera`, on peut tout d'abord lire l'état du KOSMOS. Sur l'image précédente, on lit en effet **`K4v2 state is STANDBY`**. (K4v2 est le nom du système et **STANDBY** son état.)  

Seuls les états **STANDBY** et **WORKING** permettent d'interagir avec le systèmes. Les boutons autorisés sont alors en noir. (Gris, ils sont désactivés.)

#### Etat **STANDBY**
Dans cet état , le système est en attente. Il est donc possible :
- de lancer un enregistrement (via le bouton `Start` de la section `Buttons to record`)
- d'éteindre le système (via le bouton `Shutdown`)
- de faire un test caméra avec le live vidéo (via le bouton `Start` de la section `Live video`)

Lorsque `Live video` est activé, des images basse résolution de la caméra sont visibles. Elles permettent de vérifier que tout est ok d'un point de vue optique (netteté, horizontalité du champ de vue, etc.). Il faut nécessairement stopper le live pour pouvoir lancer un enregistrement ou éteindre la caméra.  

<img src="./pictures/04_Software/Capture11.PNG" width="300">

On note aussi la présence d'une ligne `GPS position`. Elle permet de vérifier que le système capte bien le GPS. Auquel cas, il n'est pas nécessaire de prendre cette information via un autre instrument (application de positionnement, GPS de poche). Ces positions seront en effet directement enregistrées dans les métadonnées. Si la ligne `GPS position` indique `ERR ERR`, c'est qu'il y a un problème avec le GPS. Il faut donc noter à la main la position GPS sur la feuille terrain.

Quelques précisions quant au bouton `Shutdown`. Tout d'abord, il ne peut être activé que dans l'état **STANDBY**. Ceci dit, il ne doit pas être activé trop tôt après l'arrêt d'une prise de vue car un petit temps est nécessaire pour convertir la vidéo `.h264` (format natif de la Picam) en `.mp4` (format standard pouvant être lu facilementsur VLC par exemple). C'est la raison pour laquelle une ligne précise juste au dessus du bouton `SHUTDOWN` si une conversion est en cours. Quand `Conversion en cours` est présent, il ne faut pas éteindre le système. Si par hasard, le bouton est tout de même pressé, un message d'erreur apparaîtra demandant d'attendre la fin de la conversion.

<img src="./pictures/04_Software/Capture5554.PNG" width="300"> <img src="./pictures/04_Software/Capture654654.PNG" width="300">

#### Etat **WORKING**
Dans l'état **WORKING**, le système est en train d'enregistrer une vidéo. Le seul bouton autorisé est celui d'arrêt de la prise de vue (via le bouton `Stop` de la section `Buttons to record`).

<img src="./pictures/04_Software/Capture4.PNG" width="300">

### Page `Campaign`

Lors de la première tentative pour lancer un enregistrement avec le bouton `Start` de la section `Buttons to record` de la page `Camera`, un message d'erreur apparaît. 

<img src="./pictures/04_Software/Capture232.PNG" width="300">

Il signale qu'il faut au préalable renseigner les informations de la campagne. Cette précaution évite la perte de métadonnées. Il faut donc cliquer sur l'onglet `Campaign` en haut de la page. On arrive sur la page suivante :

<img src="./pictures/04_Software/Capture1.PNG" width="300">

Remplir chacune des lignes du tableau :
- `Date`: Date de la campagne journalière
- `Campaign`: Grand zone maritime dans laquelle s'effectue la campagne. Typiquement `ATL` pour Océan Atlantique, `MED` pour mer Méditerrannée, etc.
- `Zone`: Précision sur la zone de déploiement. Typiquement `BR` pour Brest, `CC`pour Concarneau, etc.
- `Location`: Lieudit du déploiement
- `Protection`: Statut de protection de la zone de déploiement. Mettre `Aucune` si il n'en existe pas.
- `Boat`: Moyen de déploiement
- `Pilot`: Nom du pilote
- `Crew`: Noms des membres de l'équipage
- `Partners`: Noms des entreprises/laboratoires/associations participant au déploiement
  
Cliquer enfin sur le bouton `Save`. À noter que tous les champs sont obligatoires.

<img src="./pictures/04_Software/Capture23.PNG" width="300">

Telle que l'interface Web est construite, ces informations Campagne sont enregistrées dans la mémoire locale du smartphone/ordinateur portable tant que la fenêtre de navigation privée du navigateur n'est pas fermée. Il faut donc la laisser ouverte tout le long de la journée de déploiement. On pourra la fermer dès la dernière station réalisée. 

Une fois les données Campagne complétées, on peut revenir sur la page `Camera` pour lancer un enregistrement. 

Cependant, il peut arriver que l'on veuille auparavant configurer le système. Pour cela, il faut aller dans la page `Configuration`.

### Page `Configuration`

<img src="./pictures/04_Software/Capture2.PNG" width="300"> <img src="./pictures/04_Software/Capture33.PNG" width="298"> 

La page `Configuration` permet de régler les paramètres du KOSMOS. Pour effectuer la modification d'un paramètre, il faut
- cliquer sur le bouton `Modify` (qui devient alors un bouton `Save`),
- taper la nouvelle valeur du paramètre
- cliquer sur le bouton `Save`
- (éventuellement refaire cette opération pour un autre paramètre)
- cliquer sur le bouton `Reboot`
- attendre que l'état du système redevienne **STANDBY**
   
Le système est alors prêt pour l'enregistrement.

Quelques précisions quant à la configuration du KOSMOS. Les paramètres visibles dans l'interface Web sont stockés dans un fichier de configuration nommé `kosmos_config.ini`. Il est contenu soit dans la clé USB, soit dans `/home/kosmos/kosmos_local_sd` suivant que l'on choisisse l'un ou l'autre de ces solutions de stockage. 

Ce fichier `kosmos_config.ini`est découpé en deux sections permettant de distinguer des paramètres que l'on peut changer durant la campagne soit lors d'un débug. Les premiers paramètres sont modifiables via l'interface web, tandis que les seconds doivent être modifiés directement dans le fichier `.ini`. On reparlera du sens de ces paramètres dans la section **Paramètres de configuration**.

### Page `Records`

Quand une station a été réalisée, il est possible de voir si la vidéo a bel et bien été enregistrée. Pour cela il faut aller sur la page `Records`.

<img src="./pictures/04_Software/Capture5.PNG" width="300"> 

Cette page précise d'abord où sont stockées les enregistrements, c'est-à-dire en local ou sur la clé USB. (Sur la figure précédente, on peut voir qu'elles sont sur la clé USB).
Le tableau référence ensuite les vidéos présentes en précisant leur nom `increment.mp4`, leur taille ainsi que la date et l'heure de leur création dans l'horloge de la Rpi (qui peut être différente de l'heure vraie sur la v3 car cette version du KOSMOS n'a pas de Real Time Clock).

Le tableau n'affiche que les fichiers vidéo (c'est-à-dire les extensions `.h264` et `.mp4`). Il ne faut donc pas s'inquiéter si les fichiers de métadonnées n'apparaissent pas. 

Autre point : lorsque l'on démarre un enregistrement, la vidéo a pour extension `.h264`. Ce fichier voit sa taille augmenter à mesure que le temps passe ; on s'en aperçoit en rafraichissant la page `Records`. Lorsque l'on arrête la vidéo avec le bouton `Stop` de la section `Buttons to record` de la page `Camera`, le fichier `.h264` est converti en `.mp4`. Cette conversion prend un peu de temps si bien que l'on voit pendant quelques instants un fichier `.h264` et un autre`.mp4` avec le même nom sur la page `Records`. Quand la conversion est finie, le `.h264` est supprimé. Il ne reste alors que le `.mp4`. En général, le temps de navigation entre deux stations permet largement à la conversion de se réaliser, il est toutefois conseillé de vérifier qu'elle est terminée (c'est-à-dire qu'il n'y a plus de `.h264`) avant de relancer une nouvelle vidéo.

Enfin, il est bon de noter qu'un fichier d'une quinzaine de minutes à 24 fps fait entre 300 Mo et 1 Go suivant les conditions d'observations. Il faut s'inquièter si la vidéo issue d'une station a une taille inférieure...  

## Paramètres de configuration du KOSMOS

### Paramètres modifiables sur le terrain via l'interface Web

 - **`00_STAVIRO_MICADO`** permet de permuter entre les modes de fonctionnement du KOSMOS.
   * **`1`** permet d'opter pour le mode STAVIRO, c'est-à-dire un fonctionnement de pose puis relevé rapide du système.
   * **`2`** correspond au mode MICADO qui correspond à une version pose longue autonome du système.
 - **`01_CAM_TIMELAPSE`** permet de permuter entre les modes vidéo ou photo.
   * **`1`** génére des vidéos
   * **`2`** génère des photos prises en rafale.
 - **`02_TEMPS_ENRGISTREMENT` (en secondes)** correspond au temps d'enregistement en secondes des séquences vidéos ou rafale de photos. Si le système doit filmer plus longtemps que ce temps d'enregistrement, la vidéo sera découpée en plusieurs séquences. Ceci permet d'éviter la perte de données si un arrêt brutal se produit. 
 - **`03_TPS_FONCTIONNEMENT` (en secondes)** règle le temps en secondes avant l'extinction automatique (mode STAVIRO) ou de la mise en veille (mode MICADO) du système.
 - **`04_TPS_VEILLE` (en secondes)** règle le temps de veille en mode MICADO. 
 - **`05_MOTEUR`** déclenche **`1`** ou non **`0`** le fonctionnement du moteur et donc de la rotation.
 - **`06_SHUTDOWN`**  permet d'éteindre ou non la Rpi lorsque le bouton arrêt est pressé. 
    * si **`0`**, le `shutdown` provoque l'arrêt du programme mais la Rpi reste allumée. On peut utiliser ce réglage pour le debug ou le développement software.
    * si **`1`**, le `shutdown` provoque l'arrêt du programme et de la Rpi. Privilégier ce mode sur le terrain.
 - **`07_HYDROPHONE`** déclenche **`1`** ou non **`0`** le fonctionnement de l'hydrophone. (Attention, l'hydrophone perturbe la prise de vidéos... Ce bug reste à corriger.)
 - **`08_STEREO`**  déclenche **`1`** ou non **`0`** la capture STEREO. A noter que le mode `1` n'est opérationnel que si deux caméras identiques sont détectées.
 - **`09_BUZZER`** déclenche **`1`** ou non **`0`** le buzzer (disponible seulement pour la v4).
 - **`38_picam_timestamp`** incruste ou non une horloge dans l'image
    * si **`0`** pas d'incrustation
    * si **`1`** incrustation
      
Pour le **Kosmos V3**, il est possible de régler les paramètres du moteur : 

 - `13_MOTOR_vitesse_min = 1000` vitesse minimale du moteur utilisée lors de son armement (peut-être inutile...)
 - `14_MOTOR_vitesse_favorite = 1350` vitesse nominale du moteur. A régler avant le départ en mission. Typiquement entre 1200 & 1600.
 - `15_MOTOR_pause_time = 27`  temps de pause en secondes entre les rotations (typiquement 27 secondes pour le protocole STAVIRO)
 - `16_MOTOR_inertie_time = 1000` temps en ms qui permet de décaler l'aimant d'asservissement du moteur suffisamment loin de l'ILS afin d'éviter son activation fortuite. A régler avant le départ en mission. Typiquement entre 500 et 2000.
 - `17_MOTOR_timeout = 5` temps de sécurité en s d'arrêt du moteur s'il n'a pas détecté l'ILS d'asservissement. A régler avant le départ en mission. Typiquement entre 5 et 10.
 - `18_motor_pressORrelease = 1`
 - `19_motor_shift_time = 2000`

Pour le **Kosmos V4**, ces paramètres sont différents :
- `10_motor_revolutions = 5`
- `11_motor_vitesse = 50`
- `12_motor_acceleration = 100`
- `13_motor_pause_time = 30`
- `14_motor_step_mode = 4`
- `15_motor_i2c_communication_period = 1`

### Paramètres non modifiables sur le terrain

Pour jouer sur ces paramètres, il faut ouvrir le fichier `kosmos_config.ini` et les modifier directement. Ceci dit, ces paramètres n'ont pas à être changés sauf modifications hardware du système.
Des paramètres sont communs aux version 3 et 4 :
 - `33_PICAM_preview = 0` Affiche ce que voit la caméra pendant qu'elle enregistre
    * si `0` pas d'aperçu (CHOISIR IMPERATIVEMENT CE MODE SUR LE TERRAIN)
    * si `1` affiche un aperçu de ce qu'observe la caméra sur l'écran (utile pour le développement et le débug car ne fonctionne qu'avec un lancement de kosmos_main.py via la terminal)
 - `34_PICAM_framerate = 24` nombre d'images enregistrées par seconde (typiquement 24)
 - `36_PICAM_conversion_mp4 = 1`  
    * si `0` ne convertit pas les fichiers vidéos en `.mp4` et les laisse en `.h264`.
    * si `1` convertit les fichiers vidéos en `.mp4` et supprime le `.h264` dans la foulée.
 - `37_PICAM_awb = 2` permet de définir le mode de fonctionnement de l'Automatic White Balance (le mode `2` est préconisé)
 - `20_CSV_step_time = 5` temps d'échantillonnage en secondes des données CSV (heure, pression, T°, postion GPS, etc.)

D'autres dépendent de la version du système. Pour le **Kosmos V3**, ces paramètres sont :
 
 - `01_SYSTEM_record_button_gpio = 17` adresse gpio du bouton début/arrêt de l'enregistrement 
 - `02_SYSTEM_stop_button_gpio = 23` adresse gpio du bouton d'arrêt du système
 - `03_SYSTEM_led_b = 4` adresse gpio de la LED verte
 - `04_SYSTEM_led_r = 18` adresse gpio de la LED rouge
 - `10_MOTOR_esc_gpio = 22` adresse gpio de l'esc qui pilote le moteur (c'est un signal PWM)
 - `11_MOTOR_power_gpio = 27` adresse gpio du relai qui alimente le moteur
 - `12_MOTOR_button_gpio = 21` adresse gpio de l'ILS qui permet d'asservir la croix de Malte

Pour la **Kosmos V4** :

- `01_system_record_button_gpio = 27` adresse gpio du bouton début/arrêt de l'enregistrement 
- `02_system_stop_button_gpio = 13` adresse gpio du bouton d'arrêt du système
- `03_system_led_b = 17` adresse gpio de la LED verte
- `04_system_led_r = 6` adresse gpio de la LED rouge
- `08_system_buzzer = 5` adresse gpio du buzzer
- `09_system_wake_up_motor = 4` adresse gpio du moteur

### Exemples de configuration

Voici quelques exemples de configuration du système KOSMOS en commençant par le mode **vidéo**, c'est-à-dire `01_CAM_TIMELAPSE = 1`.

#### Protocole historique STAVIRO
Ce mode de déploiement correspond à la configuration historique du KOSMOS. L'objectif est de réaliser plusieurs stations durant une campagne journalière. Le système est démarré en début de mission et est éteint en fin de sortie. Entretemps, des enregistrements d'une quinzaine de minutes s'enchainent à diverses endroits de la zone étudiées. 

Dans cette configuration, c'est l'opérateur qui déclenche la prise de vue (via le bouton `Start` de la section `Buttons to record` de la page `Camera`) ainsi que son arrêt (via le bouton `Stop`). La durée d'une vidéo dépend donc théoriquement de ces deux actions `Start` puis `Stop`. Néanmoins, afin de sécuriser les données et d'éviter un déchargement inutile de la batterie, deux paramètres temporels sont disponibles au cas où un système resterait en immersion durant une durée bien plus longue que prévue :
- `02_tps_enregistrement` qui définit la durée maximale d'une vidéo avant de la convertir en `.mp4` (et ainsi de la sécuriser) et de recommencer à filmer.    
- `03_tps_fonctionnement` qui définit la durée maximale de fonctionnement du système avant qu'il ne s'éteigne (pour ne pas vider la batterie).

Dans le protocole STAVIRO, une vidéo *normale* dure en général 15 minutes. On a donc fixé les paramètres de la façon suivante :
| Paramètres | Valeurs | Commentaires | 
|-------|-----------|-----------|
|`00_STAVIRO_MICADO`|1|Mode STAVIRO|
|`01_CAM_TIMELAPSE`**|1|Mode Vidéo|
|`02_TEMPS_ENRGISTREMENT`|1200|20 minutes de prise de vue|
|`03_TPS_FONCTIONNEMENT`|1800|30 minutes de fonctionnement|
|`04_TPS_VEILLE `|600| non utilisé en mode STAVIRO|

Autrement dit, si un système reste plus de 20 minutes dans l'eau, l'enregistrement vidéo va stopper momentanément pour que la vidéo `.h264` soit convertie en `.mp4` puis reprendre. Il sera soit stoppé par l'opérateur soit s'achever 10 minutes plus tard. La nouvelle vidéo sera convertie puis le système s'arrêtera. Lors de sa récupération, il sera en conséquent impossible de se connecter au Wifi puisque la Raspberry sera éteinte. Il faudra donc dévisser le switch puis le revisser pour rédémarrer le système.

#### Vidéo continue
Dans cette configuration, on pose le système sur une station fixe et on filme en continu le plus longtemps possible ou jusqu'à la récupération du système. On utilise encore les paramètres `02_tps_enregistrement` et `03_tps_fonctionnement` pour limiter la perte de données et éviter un déchargement complet des batteries.

| Paramètres | Valeurs | Commentaires | 
|-------|-----------|-----------|
|`00_STAVIRO_MICADO`|1|Mode STAVIRO|
|`01_CAM_TIMELAPSE`|1|Mode Vidéo|
|`02_TEMPS_ENRGISTREMENT`|600| La vidéo sera coupée en séquences de 10 minutes|
|`03_TPS_FONCTIONNEMENT`|64800|Le système s'arrêtera au bout de 18h, correspondant à l'autonomie de la batterie|
|`04_TPS_VEILLE `|600| non utilisé en mode STAVIRO|


#### Mode MICADO
Une fois de plus, le système est installé à une station fixe. Cependant, au lieu de filmer en continu, le système alterne des phases d'enregistrement et de veilles profondes, et ce, en vue d'augmenter au maximum son autonomie. Pour utiliser ce mode MICADO, il faut changer le paramètre `00_staviro_micado` en lui donnant la valeur `2` (il valait `1` en mode STAVIRO). Les paramètres temporels sont :
| Paramètres | Valeurs | Commentaires | 
|-------|-----------|-----------|
|`00_STAVIRO_MICADO`|2|Mode MICADO|
|`01_CAM_TIMELAPSE`|1|Mode Vidéo|
|`02_TEMPS_ENRGISTREMENT`|1000| Paramètre qui n'est pas vraiment pertinent sauf si le temps de fonctionnement est vraiment long et qu'on veut sectionner les vidéos pour les sécuriser. Mais dans le cas classique, il faut juste s'assurer que `02_tps_enregistrement` > `03_tps_fonctionnement`|
|`03_TPS_FONCTIONNEMENT`|900|Pour 15 minutes, comme dans le protocole STAVIRO|
|`04_TPS_VEILLE `|7200|2 heures de veilles profondes entre les vidéos|

#### Un dernier exemple en timelapse
On présente enfin une configuration permettant de capturer une rafale d'images à intervalles réguliers.
| Paramètres | Valeurs | Commentaires | 
|-------|-----------|-----------|
|`00_STAVIRO_MICADO`|2|Mode MICADO|
|`01_CAM_TIMELAPSE`|2|Mode Rafale|
|`02_TEMPS_ENRGISTREMENT`|1000| Paramètre non utilisé en mode Rafale|
|`03_TPS_FONCTIONNEMENT`|60|Les rafales durent une minute|
|`04_TPS_VEILLE `|7200|2 heures de veilles profondes entre les vidéos|

## Structuration des données

### Lieu de stockage

Deux méthodes de stockage sont possibles : 
- en local sur la carte SD
- sur une clé USB.
Si une clé USB est branchée, elle sera prioritaire. Si aucune clé usb n'est branchée, les fichiers seront stockées dans `/home/kosmos/kosmos_local_sd` (qui se créera automatiquement au besoin). Il faudra dans ce cas veiller à ce que la carte SD ait une capacité appropriée (on préconise au moins 64 Go).

Il peut arriver que la clé USB (si ce système de stockage est choisi), contienne déjà des vidéos ainsi qu'un fichier de configuration `kosmos_config.ini`. Nous recommandons de renommer ce dernier fichier (en `kosmos_config_old.ini`) pour éviter des bugs de compatibilité entre les versions du soft. Par ailleurs, il faudra veiller à ce que la clé propose assez de places pour accueillir les nouvelles vidéos. Typiquement prévoir 10Go par journée de campagne. 
  
Lorsque l'on démarre le système avec une clé vierge, un dossier et un ficher texte vont s'y créer. Si aucune clé n'est branchée, ces éléments seront dans `/home/kosmos/kosmos_local_sd`.

<img src="./pictures/04_Software/Capture88.PNG" width="300">

### Données

Le fichier `kosmos_config.ini` contient les paramètres de configuration du système. Ces paramètres seront visibles et modifiables depuis l'interface web.

Le dossier contenant les données associées à une journée de campagne s'appelle normalement `date_nomdusystem`, typiquement `250403_KIMT`. Dans ce dossier, seront présents d'autres dossiers correspondant à chaque enregistrement. Ils auront pour nom l'`increment`, typiquement `0091`.

<img src="./pictures/04_Software/Capture99.PNG" width="200">

Chacun de ces dossiers contiennent une vidéo (voire deux si l'on filme en stéréo) et ses métadonnées. 
- Le fichier vidéo `increment.mp4` (et éventuellement increment_STEREO.mp4 si la stéréo est activée)
- Un fichier `increment.txt` qui stocke l'instant (ou timestamp en anglais) de chaque frame de la video.
- Un fichier `increment.csv` qui stocke des paramètres de la caméra ainsi que les données T,P, position et autres données fournies par les capteurs du système pendant la prise de vue.
- Un fichier `increment.json` qui stocke les métadonnées de la prise de vue.
- Un fichier `systemEvent.csv` qui stocke les évènements du sytème comme la rotation du moteur ou la mise à jour des gains de couleur AWB
- Un fichier `increment.wav` qui stocke l'enregistrement audio si l'hydrophone est activé.

<img src="./pictures/04_Software/Capture55.PNG" width="400">

#### Vidéo continue

Dans le cas d'une prise vidéo de longue durée (c'est-à-dire une vidéo qui ne serait pas stoppée avant le temps limite `02_tps_enregistrement`), les données auront une structure un peu différentes. En effet,  la vidéo et ses métadonnées seront découpées en plusieurs parties afin d'éviter des pertes de données éventuelles. Un increment supplémentaire apparaîtra pour signifier ce découpage. La première partie de vidéo enregistrée (et ses métadonnées) resteront :
- `increment.mp4` `increment.txt` `increment.csv` `increment.json`
  
La seconde partie se nommera :
- `increment_0001.mp4` `increment_0001.txt` `increment_0001.csv` `increment_0001.json`
  
et ainsi de suite :
- `increment_0002.mp4` `increment_0002.txt` `increment_0002.csv` `increment_0002.json`
- `increment_0003.mp4` `increment_0003.txt` `increment_0003.csv` `increment_0003.json`

Le fichier `systemEvent.csv` contiendra les heures de démarrage et d'arrêt de chacune de ses parties de vidéo. 

#### Rafale de photos

Dans le cas d'une rafale de photos, au lieu de générer une vidéo `.mp4`, un dossier nommé `increment` est créé (c'est le dossier `0016` dans l'image suivante). 

<img src="./pictures/04_Software/Capture5599.PNG" height="300">

Ce dossier contiendra la rafale de photos. Chaque image aura pour nom : `increment_numero2photo.jpg`  

<img src="./pictures/04_Software/Capture986598.PNG" height="250">

À noter qu'il n'y a pas (contrairement aux vidéos) de fichier `increment.txt`. Les timestamp des images capturées sont en effet directement dans `increment.csv` où chaque ligne correspond à une image.
