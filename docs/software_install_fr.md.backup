## 1/ Installation de raspbian 

### 1.1 Flasher l'image sur la carte SD

 - Sur votre PC (windows ou linux), installer le logiciel [Raspberry Imager](https://www.raspberrypi.com/software/) Ce logiciel est un imager il permet de flasher un périphérique avec une image OS. Dans notre cas un os spécialement conçus pour raspberry, rapbian. 
 - Insérer une carte micro SD d'une capacité minimale de 8Go dans un lecteur de carte sd. Attention, cette carte sera formaté. Elle devra donc être libre.
 - A l'aide du logiciel raspberry imager, commencer par sélectionner le bon OS. Préférer un OS tout en ligne de commande sans interface graphique. Ce dernier est plus léger. Si toutefois vous n'êtes pas à l'haise avec les commandes Unix, vous pouvez prendre raspbian avec une interface graphique mais il faudra probablement une SD de 16Go minimum. 

![IS1-1](pictures/install_software/IS1-1.JPG)
  
 - Sélectionner la carte SD (/!\ Risque de perte de données, veiller à ne pas vous tromper de disque). 
 - Avec la version 1.7 et postérieures il est possible de prérégler la raspberry. Ce qui évite un bon nombre de problèmes récurant et un démarrage plus rapide. Cliquer sur l'engrenage en bas à droite de la fenêtre. S'ouvre alors une fenêtre qu(il conviendra de régler comme suit.)
 - Nommer l'utilisateur en fonction de vos besoins (exemple de nomenclature : kosmosINITIALSnuméro)(ici kosmos3) ;
 - Entrer un mot de passe simple,

![IS1-1](pictures/install_software/IS1-2.png)

 - Flasher la carte SD. Puis lancer l'écriture, ce processus va durer quelques instants. 


### 1.2 Démarrage pour la première fois

 - Avant la mise en tension, veiller à connecter la Raspberry pi à un écran au moyen d'un câble HDMi. 
 - Au moyen d'une alimentation USB-c (3A minimum) brancher la Raspbery pi
 - Si rien ne s'affiche consulter le [lien ci attaché](https://kosmos.fish/wiki/?FormTechno&vue=consulter&action=voir_fiche&id_fiche=ResoluPasDAffichageHdmiAuDemarrageDeL&message=ajout_ok)
 - Si tout se passe bien, la raspberry va booter pour la première fois ;
 - Entrer le nom d'utilisateur puis le mot de passe. Lorsque l'on rentre un mot de passe sur linux, il est tout à fait normal que rien ne s'affiche. 
 - S'assurer que la connexion wifi est bonne : <pre>ping 8.8.8.8</pre> Le retour de cette commande doit ressembler à : <pre>64 bytes from 8.8.8.8 icmp...</pre> En cas de mauvaise connexion, se référer à la note 1 en bas de cette page.


## 2/ Installation de l'environnement KOSMOS

 - Effectuer un update : <pre>sudo apt update</pre>
 - Puis un upgrade : <pre>sudo apt upgrade</pre>
 - Redémarrer : <pre>reboot</pre>
 - Sur la raspberry, installer git : <pre>sudo apt install git</pre>
 - Depuis la raspberry et dans le répertoire courant (cd ~), cloner le dépot kosmos_software (pour le moment la branche de dev d'Amaury): <pre>git clone --branch developement-amaury https://github.com/KonkArLab/kosmos_software.git</pre>
 - Se déplacer dans kosmos_software : <pre>cd kosmos_software</pre>
 - Modifier les droits d'éditions : <pre>sudo a+wrx install.sh</pre>
 - Lancer l'installation du software KOSMOS : <pre>sudo ./install.sh</pre>


 

## Notes
 - L'environnement kosmos ne fonctionnera que si Python est installé sur la bonne version. Soit la 2.7.16
 - Le gitignore permet lorsque l'on clone le git de ne pas copier un dossier spécifique. Dans notre cas les librairies qui seront installés par la raspberry pendant l'installation de KOSMOS. 
 - Passer le clavier en Azerty en suivant la [documentation ci jointe](https://alain-michel.canoprof.fr/eleve/tutoriels/raspberry/premiers-pas-raspberrypi/activities/clavier-en-francais.html) ;


### Note/1 Connexion au wifi
La connexion au wifi bien que non nécessaire pour observer les poissons sera très utile au laboratoire pour piloter le KOSMOS en SSH sans y brancher d'écran, cela va permettre aussi de télécharger les paquets KOSMOS sur Github et de les mettre à jour par la suite.

 - Editer WPA supplicant : ```sudo nano /etc/wpa_supplicant/wpa_supplicant.conf```
 - Y écrire les lignes suivantes (en plaçant le SSID et le mot de passe du routeur wifi) : 

<pre>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=FR
 
network={
    ssid="ESSID"
    psk="Your_wifi_password"
}</pre>



### Note/2 Assignation d'une IP fixe
[Le tuto qui suit est librement inspiré](https://raspberry-pi.fr/ip-locale-fixe/)
Une adresse IP est un code de quatre nombres qui permet à un routeur de retrouver un objet connecté. Cette adresse peut changer à chaque redémarrage. Pour retrouver notre appareil à chaque fois il est donc nécessaire d'assigner à la Raspberry une IP fixe.

 - Sur la raspberry ou via ssh, entrer l'une des commandes suivantes :
 	- Si la raspberry pi est connectée à votre box en ethernet : <pre>ip route | grep eth0</pre>
	
	- Sinon si la pi est connectée en wifi : <pre>ip route | grep wlan0</pre>
 
 - Noter le retour de la commande qui doit être semblable à :
  <pre>default via 192.168.0.1 dev wlan0 src 192.168.0.101 metric 303 
192.168.0.0/24 dev wlan0 proto dhcp scope link src 192.168.0.101 metric 303</pre>

 - Ouvrir le fichier ""dhcpcd.conf" en utilisant la commande nano :<pre>sudo nano /etc/dhcpcd.conf</pre>

 - Remplacer le contenu par les lignes suivantes (wlan0 si wifi et eth0 si ethernet), changer les adresse IP et le /XX par les adresses renvoyés pas la commande précédente.
<pre>interface wlan0
static ip_address=192.168.0.101/24
static routers=192.168.0.1</pre>

 - Quitter en enregistrant (ctrl+X puis Y et enter)
 - Redémarrez la raspberry : <pre>reboot</pre>



