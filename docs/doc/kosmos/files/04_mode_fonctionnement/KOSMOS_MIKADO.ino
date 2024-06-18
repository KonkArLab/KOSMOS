//Rentrez le temps d'enregistrement correspondant au temps rentré dans le kosmos_config.ini
int temps_rec=15;
//La sécurité permet d'être sur de ne pas éteindre le KOSMOS avant le shutdown
int securite=3;
//Rentrez les horaires de lancement de l'enregistrer sous le format ( Heure1, Minute1, Heure2, Minute 2, ....)
byte const Heure_dep[]={8,30,10,30,13,37,14,57,15,50,16,43,17,1,20,20};
#include "RTClib.h" //on inclut la librairies pour utiliser l'horloge RTC
//on crée un Serial
#include <SoftwareSerial.h>
const int rx=3;
const int tx=4;
SoftwareSerial mySerial(rx,tx);
RTC_DS1307 rtc;
//On ajoute au temps d'enregistrement la sécurité pour éviter le problème mis en avant plus haut
int time=temps_rec+securite; 
void setup () {
  //Lancement du thread
  mySerial.begin(115200);
  pinMode(1,OUTPUT); // La broche 1 est définie en sortie GPIO
  // Attente de la connection serie avec l'Arduino
  while (!mySerial);
 
  // Lance le communication I2C avec le module RTC et attend que la connection soit operationelle
  while (! rtc.begin()) {
    mySerial.println("Attente du module RTC...");
    delay(1000);
  }
 
  // Mise à jour de l'horloge du module RTC avec la date et l'heure courante au moment de la compilation de ce croquis
  rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
 
  mySerial.println("Horloge du module RTC mise a jour");
}
 
void loop () {
    DateTime now = rtc.now();
    char heure[10];
 
    // Affiche l'heure courante retournee par le module RTC
    // Note : le %02d permet d'afficher les chiffres sur 2 digits (01, 02, ....)
    //sprintf(heure, "Il est %02d:%02d:%02d", now.hour(), now.minute(), now.second());
    //mySerial.println(heure);
    for (int i=0;i<24;i+=2){ // on vient tester les différentes valeur dans la liste d'heure rentrée au-dessus
      if ( now.hour()==Heure_dep[i] && now.minute()==Heure_dep[i+1]){ //Lorsque l'heure et la minute sont égales à une horraires rentrée plus haut on rentre dans une boucle infinie
        while(1){ 
          DateTime now = rtc.now(); //on réactualise l'heure
          if ((Heure_dep[i+1]+time)<60){ // C'est le cas général : on ne change pas d'heure en ajoutant "time"
            if (now.hour()==Heure_dep[i] && now.minute()==Heure_dep[i+1]+time){ 
              break; // si l'heure et la minute correspondent au temps de départ plus "time" on sort de la boucle while
            }
          }
          else{ // on gère l'exception du changement d'heure.
            int Heure_arr=Heure_dep[i]+1; // On passe à l'heure d'après
            int Minute_arr=(Heure_dep[i+1]+time)%60; // on garde les minutes restantes
            if (now.hour()==Heure_arr && now.minute()==Minute_arr){ 
              break; // si l'heure et la minute correspondent au temps de départ plus "time" on sort de la boucle while
            }
          }
          digitalWrite(1,HIGH); // Tant qu'on est dans la boucle infinie, on met la position du GPIO à "HIGH" -> on allume la raspberry
        }
      }
      digitalWrite(1,LOW); // Sinon on laisse éteint la raspberry
    }
}
