icon:fontawesome/regular/hourglass-half
# Upgrade au mode Automatique

## 1/ Principe

Le principe du mode MICADO est de pouvoir laisser le KOSMOS en position pendant plusieurs jours. L'objectif n'est pas de le faire tourner pendant toute la durée d'immersion comme pour le mode STAVIRO. Le but du mode MICADO est d'activer le système sur des horaires bien précis rentré par l'utilisateur auparavant et de faire tourner le KOSMOS pendant une durée rentrée au préalable par l'utilisateur ( en général 15 minutes ).  Ce système permet de faire plusieurs prélèvements de vidéos au même endroit sur des plages horaires précises sans à avoir à remonter le KOSMOS entre chaque prise.
Pour réaliser ceci, nous utilisons une carte Adafruit Trinket 1501 reliée à un module RTC. Celle-ci permettra de contrôler l’alimentation du système grâce à un relais. Elle allumera la carte RaspBerry sur les plages horaires rentréesconso par l’utilisateur. Nous sommes obligé d'utiliser une carte auxiliaire car le mode veille de la carte Raspberry consomme énormément. Le gros avantage de cette carte est sa très faible consommation.
Un autre avantage de cette carte est sa toute petite taille : elle mesure 31mm x 15.5mm x 5mm. Elle dispose des ports I2C nécessaires pout être connectée au module RTC et d’une sortie GPIO permettant de contrôler le relais.
﻿

﻿
## 2/ Réalisation

Pour commencer, un relai brancher en série sur l'alimentation 5v de la raspberry. Ce relai sera piloté par l'arduino. 
Voici le montage entre le module RTC, l’Adafruit et le relais :

![MU2-1](/../doc/kosmos/pictures/micado_upgrade/MU2-1.png)

﻿
﻿
La carte Adafruit est assez particulière à programmer. Elle n'est pas 100% compatible avec l'IDE Arduino : Il faut donc opérer quelques astuces. Nous avons rencontré quelques difficultés pour la programmer ; programmer avec Arduino, lancer le téléversement. Vous retrouverez un TUTO très détaillé de ces étapes dans "docs/files/micado_upgrade/TUTO ADAFRUIT 1501.pdf" du git.

A l'emplacement "/docs/files/micado_upgrade" se trouve aussi le code Arduino expliqué permettant de programmer la carte Adafruit sur des plages horaires précises. Ces horaires devant être rentrer par l'utilisateur.

Une fois ces horaires rentrer, l'utilsateur n'a qu'à activer l'alimentation du KOSMOS et le poser au fond. Le KOSMOS va ainsi filmer pendant une période définie par l'utilisateur aux mêmes heures pendant quelques jours. Cela permettra d'avoir une analyse plus étendue d'un même endroit.


## 3/ Notes et pistes d'évolution
 - Cette documentation est une relique et date de l'été 2021. Il constitue une réflexion de base pour construire le mode MICADO final. 
 - Noter que ce système permet d'économiser de l'énergie. En effet, la raspberry même en veille peu consommer 500mA. 
 - Le mode MICADO est déjà activé au software KOSMOS. Il doit démarrer le process immédiatement après démarrage. Pour passer en mode MICADO modifier le variable correspondante dans le fichier "kosmos_config.ini" se trouvant sur la clé usb.