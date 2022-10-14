## 1/ Installation de raspbian 

### 1.1 Flasher l'image sur la carte SD

 - Sur votre PC (windows ou linux), installer le logiciel [Raspberry Imager](https://www.raspberrypi.com/software/) Ce logiciel est un imager il permet de flasher un périphérique avec une image OS. Dans notre cas un os spécialement conçus pour raspberry, rapbian. 
 - Insérer une carte micro SD d'une capacité minimale de 8Go dans un lecteur de carte sd. Attention, cette carte sera formaté. Elle devra donc être libre.
 - A l'aide du logiciel raspberry imager, commencer par sélectionner le bon OS. Préférer un OS tout en ligne de commande sans interface graphique. Ce dernier est plus léger. Si toutefois vous n'êtes pas à l'haise avec les commandes Unix, vous pouvez prendre raspbian avec une interface graphique mais il faudra probablement une SD de 16Go minimum. 
![IS1-1](pictures/install_software/IS1-1.JPG)
  
 - Sélectionner la carte SD (/!\ Risque de perte de données, veiller à ne pas vous tromper de disque). Flasher la carte SD. Pui lancer l'écriture, ce processus va durer quelques instants. 



### 1.2 Démarrage pour la première fois

 - Avant la mise en tention, veiller à connecter la Raspberry pi à un écran au moyen d'un câble HDMi. 
 - Au moyen d'une alimentation USB-c (3A minimum) brancher la Raspbery pi
 - Si rien ne s'affiche consulter le [lien ci attaché](https://kosmos.fish/wiki/?FormTechno&vue=consulter&action=voir_fiche&id_fiche=ResoluPasDAffichageHdmiAuDemarrageDeL&message=ajout_ok)
 - Si tout se passe bien, la raspberry va booter pour la première fois ;
 - /!\Attention pour les prochaines étapes le clavier est de base en Qwerty (Crédit image : cc-by Tomiĉo), veiller donc à écrire en intervertissant les lettres a-q ; m-, et en utilisant les chiffres situé au dessus du clavier sans activer la majuscule (Faire particulièrement attention au moment d'entrer un mot de passe. En effet on ne voit pas ce que l'on écrit).
![IS1-2](pictures/install_software/IS1-2.JPG)


 - Nommer l'utilisateur en fonction de vos besoins (exemple de nomenclature : kosmosINITIALSnuméro)(ici kosmos3) ;
 - Entrer un mot de passe simple, puis le confirmer ;
 - Passer le clavier en Azerty en suivant la [documentation ci jointe]([https://github.com/gheleguen/KOSMOS_tech](https://alain-michel.canoprof.fr/eleve/tutoriels/raspberry/premiers-pas-raspberrypi/activities/clavier-en-francais.html) ;

### 1.3 Connexion au wifi
La connexion au wifi bien que non nécessaire pour observer les poissons sera très utile au laboratoire pour piloter le KOSMOS en SSH sans y brancher d'écran, cela va permettre aussi de télécharger les paquets KOSMOS sur Github et de les mettre à jour par la suite.

 - Editer WPA supplicant : ```sudo nano /etc/wpa_supplicant/wpa_supplicant.conf```
 - Y écrire les lignes suivantes (en plaçant le SSID et le mot de passe du routeur wifi) : 
```ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=FR
 
network={
    ssid="ESSID"
    psk="Your_wifi_password"
}
```


### 1.4 Assignation d'une IP fixe
[Le tuto qui suit est librement inspiré](https://raspberry-pi.fr/ip-locale-fixe/)
Une adresse IP est un code de quatre nombres qui permet à un routeur de retrouver un objet connecté. Cette adresse peut changer à chaque redémarrage. Pour retrouver notre appareil à chaque fois il est donc nécessaire d'assigner à la Raspberry une IP fixe.

 - Sur la raspberry ou via ssh, entrer l'une des commandes suivantes :
 	- Si la raspberry pi est connectée à votre box en ethernet : ```ip route | grep eth0```
	
	- Sinon si la pi est connectée en wifi : ```ip route | grep wlan0```
 
 - Noter le retour de la commande qui doit être semblable à :
  ```default via 192.168.0.1 dev wlan0 src 192.168.0.101 metric 303 
192.168.0.0/24 dev wlan0 proto dhcp scope link src 192.168.0.101 metric 303
```

 - Ouvrir le fichier ""dhcpcd.conf" en utilisant la commande nano :```sudo nano /etc/dhcpcd.conf```

 - Remplacer le contenu par les lignes suivantes (wlan0 si wifi et eth0 si ethernet), changer les adresse IP et le /XX par les adresses renvoyés pas la commande précédente.
  ```interface wlan0
static ip_address=192.168.0.101/24
static routers=192.168.0.1
```

 - Quitter en enregistrant (ctrl+X puis Y et enter)
 - Redémarrez la raspberry : ```reboot```



### 1.5 se connecter au SSH
 - Activer le ssh en allant dans raspi-config : 
 ```sudo raspi-config```
 - Naviguer dans ""interfaces Options" ;
 - Puis ""ssh" et suivre les instructions pour l'activer. 




## 2/ Installation de l'environnement KOSMOS

 - Effectuer un update : ```sudo apt update```
 - Puis un upgrade : ```sudo apt upgrade```
 - rebooter : ```reboot```
 - Sur la raspberry, installer git : ```sudo apt install git```
 - Installer pip : ```sudo apt install python3-pip```
 - Installer virtual env : ```pip install virtualenv```
 - Sur la raspberry, créer un dossier vierge "kospython" sur le répertoire courant avec : ```mkdir kospython```
 - Se déplacer dans le dossier créé : ```cd kospython```
 - Depuis la raspberry cloner le dépot kosmos_software : ```git clone https://github.com/KonkArLab/kosmos_software.git```
 - Se déplacer dans kosmos_software : ```cd kosmos_software```
 - Activer l'environnement : ```source kosmosV3-env/bin/activate```
 - Installer les packages : ```pip install -r kosmosV3-env/requirements.txt```
 
 

### Notes
 - L'environnement kosmos ne fonctionnera que si Python est installé sur la bonne version. Soit la 2.7.16
 - Le gitignore permet lorsque l'on clone le git de ne pas copier un dossier spécifique. Dans notre cas les librairies qui seront installés par la raspberry pendant l'installation de KOSMOS. 
 
