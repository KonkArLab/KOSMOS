
## Caisson Moteur

### Vue générale

<img src="pictures/V4_Moteur/VueGenerale.PNG" height=400>

### Réalisation de la carte électronique du moteur

<img src="pictures/V4_Moteur/5.jpeg" height=400> <img src="pictures/V4_Moteur/4.jpeg" height=400>

### Cablage moteur

- Raccourcir les cables du moteur pour qu'ils mesurent 10 cm.
- Dénuder les fils sur 5 mm puis y sertir des cosses JST. Vérifier qu'elles tiennent fermement.
- Insérer les cosses dans les connecteurs JST en suivant le plan de cablage.

<img src="pictures/V4_Moteur/1.jpeg" height=200> <img src="pictures/V4_Moteur/2.jpeg" height=200>

<img src="pictures/V4_Moteur/TapeArriere.PNG" height=400>

### Réalisation du cable d'alimentation

- Avec une pince coupante, raccourcir le cable COB-1231 pour qu'il mesure 40 cm. Garder les fils noir, jaune et rouge. La gaine ne sera plus utilisée.
- Avec l'outil Knipex, enlever 20 cm de gaine noire. Attention à ne pas abimer les fils à l'intérieur. (Si c'était le cas glisser de la gaine thermoretractable au niveau de la coupure.)
- Couper le fil jaune à ras de la gaine pour ne conserver que le noir et le rouge. (On rappelle la convention : 5V Jaune et Noir. 12 V Rouge et Noir.)
- Dénuder les fils rouge et noir sur 7 mm.
- Y sertir des cosses dont on a vérifié qu'elles avaient le diamètre optimal.

### Réalisation du cable signal moteur

- Avec une pince coupante, raccourcir le cable COB-1241 pour qu'il mesure 40 cm. Garder les quatre fils et la gaine.
- Avec l'outil Knipex, enlever 20 cm de gaine noire. Attention à ne pas abimer les fils à l'intérieur. (Si c'était le cas glisser de la gaine thermoretractable au niveau de la coupure.)
- Couper le fil jaune à ras de la gaine pour ne conserver que le noir et le rouge. (On rappelle la convention : 5V Jaune et Noir. 12 V Rouge et Noir.)
- Dénuder les fils rouge et noir sur 7 mm.
- Y sertir des cosses dont on a vérifié qu'elles avaient le diamètre optimal.


https://bluerobotics.com/learn/wetlink-penetrator-installation-guide/

https://www.youtube.com/watch?v=vigY82tsfOI&t=2s&ab_channel=BlueRobotics


### Installation Soft Arduino Moteur

- Installer le logiciel Arduino depuis le site https://www.arduino.cc/en/software
- Télécharger control_motor.ino depuis le github [KonkArLAb/kosmos_software](https://github.com/KonkArLab/kosmos_software/tree/dev_stereo_merge_imt)
- Placer ce fichier .ino dans un dossier nommé control_motor
- Lancer l'IDE Arduino et ouvrir control_motor.ino
- Brancher l'Arduino Nano à l'ordinateur via le port USB
- Effectuer l'installation demandée par l'IDE Arduino
- Dans l'onglet Tools, sélectionner le port COM auquel est branché l'Arduino Nano
- Dans l'onglet Tools, sélectionner la board Arduino Nano
- Dans l'onglet Tools, Manage Librairie. Taper "AccelStepper". Installer la librairie associée.
- Vérifier le code.
- Téléverser.
- (Si un message d'erreur apparaît, aller dans l'onglet `Tools` puis `Processor: ATmega328P` et choisir `ATmega328P (Old BootLoader)`. Téléverser à nouveau.)





    
