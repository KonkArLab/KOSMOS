icon:material/video-vintage
## 1/ Extraire les vidéos du KOSMOS. 

Toutes les données du KOSMOS sont stockés sur l'unique clé USB cnnecté à la Raspberry pi. On prendra soint de n'extraire cette clé que lorsque le KOSMOS est hors tension. A défaut cela pourait entrainer des problèmes de montage de la clé sur la raspberry et par conséquent entrainer une perte de données.

 - Pour accéder à la clés USB, ouvrir la flange côté cablage en dévissant le bouchon vent (appel d'air).
 - Extraire la clés USB puis l'insérer dans un ordinateur.
 - Se diriger dans le dossier vidéos de la clés USB. Copier tous les fichiers qui y sont stockés. Les archiver dans un dossier locale au choix.
 - Ces fichiers en ".h264" doivent rester Archivés dans un dossier différent de celui que l'on utilisera pour la manipulation. Attention les manipulations suivantes si elles conduisent à une erreur peuvent entrainer la perte de données. 
 - Une fois les données sauvés on pourra suprimer celles présentent dans la clés USB pour libérer le stokage du KOSMOS et ainsi éviter de mauvaises surprises au retour de campagnes en mer. 
 

## 2/ Transformation des viéos au format MP4
le format h264 des vidéos est exploitable, mais présente la difficulté de ne pas être borné ce qui rend difficile d'avancer la vidéos ou de revenir en arrière. Il est également impossible avec ce format de noter des times codes. Pour faciliter la lecture des nos vidéos nous allons donc les convertir en MP4. 
Pour y parvenir on utilisera une simple invit de commande linux. 
 - Ouvrir un terminal de commandes,
 - Se diriger dans le dossier où se trouvent les vidéos que l'on souhaite transformer en utilisant par exemple la commande : <pre>cd /Chemin/du/dossier</pre>
 - Utiliser la commande suivantes pour chaque fichier en remplaçant "input" et "output" par le nom du fichier en question. Veiller à bien conserver cependant les bonnes extentions à savoir ".h264" poyur l'input et ".mp4" pour l'output : <pre>ffmpeg -framerate 24 -i input.h264 -c copy output.mp4</pre>
 - Pour éviter de mélanger dans le même dossier les h264 et mp4 on pourra aussi créer un dossier différent pour l'entrée et la sortie. Dans ce cas spécifier le chemin directement à la commande ffmpeg vue ci-dessus. 



## Liens connexes
 - [Forum d'où vien la ligne de commande capable de faire la transformation H264 en MP4](https://askubuntu.com/questions/690015/how-can-i-convert-264-file-to-mp4)