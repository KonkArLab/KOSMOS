#!/usr/bin/env python3 -- coding: utf-8 --
""" Programme principal du KOSMOS en mode rotation Utilse une machine d'états D Hanon 12 décembre 2020 """

import logging
import time
from threading import Event
from enum import Enum, unique
import RPi.GPIO as GPIO
import os


import kosmos_config as KConf
import kosmos_csv as KCsv
import kosmos_led as KLed
import kosmos_cam as KCam
import kosmos_esc_motor as KMotor
import sys

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s : %(message)s',
                    datefmt='%d/%m %I:%M:%S',
                    filename='kosmos.log')


@unique
class KState(Enum):
    """Etats du kosmos"""
    STARTING = 0
    STANDBY = 1
    WORKING = 2
    STOPPING = 3
    SHUTDOWN = 4


class kosmos_main():

    def __init__(self):
        # Lecture du fichier de configuration
        self._conf = KConf.KosmosConfig()
        self.state = KState.STARTING

        # LEDs
        self._ledB = KLed.kosmos_led(self._conf.get_val_int("SETT_LED_B"))
        self._ledR = KLed.kosmos_led(self._conf.get_val_int("SETT_LED_R"))
        self._ledB.start()
        self._ledR.set_off()

        # évènements
        self.button_event = Event()  # un ILS a été activé
        self.record_event = Event()  # l'ILS start or stop record été activé
        self.stop_event = Event()    # l'ILS du shutdown or stop record activé
        self.motor_event = Event()  # l'ILS du moteur activé

        # Boutons
        self.STOP_BUTTON_GPIO = self._conf.get_val_int("SETT_STOP_BUTTON_GPIO")
        self.RECORD_BUTTON_GPIO = self._conf.get_val_int("SETT_RECORD_BUTTON_GPIO")
        self.MOTOR_BUTTON_GPIO = self._conf.get_val_int("SETT_MOTOR_BUTTON_GPIO")
        GPIO.setmode(GPIO.BCM)  # on utilise les n° de GPIO et pas les broches
        GPIO.setup(self.STOP_BUTTON_GPIO, GPIO.IN)
        GPIO.setup(self.RECORD_BUTTON_GPIO, GPIO.IN)
        GPIO.setup(self.MOTOR_BUTTON_GPIO, GPIO.IN)
        self.tps_POSE=self._conf.get_val_int("SETT_MOTOR_STOP_TIME")
        self.tps_ROTATION60=self._conf.get_val_int("SETT_MOTOR_RUN_TIME")
        self.vitesse_moteur=self._conf.get_val_int("SETT_ESC_MOTOR_FAVORITE_VAL")
        self.MODE=self._conf.get_val_int("SETT_MODE") # à mettre dans le ini
        self.tps_record=self._conf.get_val_int("SETT_RECORD_TIME")
        self.motorThread = KMotor.komosEscMotor(self._conf)
        self.thread_camera = KCam.KosmosCam(self._conf)
        
    def clear_events(self):
        """Mise à 0 des evenements attachés aux boutons"""
        self.record_event.clear()
        self.button_event.clear()
        self.stop_event.clear()
        self.motor_event.clear()

    def starting(self):
        """Le kosmos est en train de démarrer"""
        logging.info("ETAT : Kosmos en train de démarrer")
        self.motorThread.autoArm()  # Arment du moteur
        self.thread_csv = KCsv.kosmosCSV(self._conf)
        self.thread_csv.start()
        self._ledB.pause()
        if (self.MODE == 1) :
            self.state = KState.STANDBY
        else :
            self.state = KState.WORKING

    def standby(self):
        """Le kosmos est en attente du lancement de l'enregistrement"""
        logging.info("ETAT : Kosmos prêt")
        self._ledB.set_on()
        self.button_event.wait()
        if myMain.stop_event.isSet():
            self.state = KState.SHUTDOWN
        else:
            if myMain.record_event.isSet():
                self.state = KState.WORKING
        self._ledB.set_off()
      
    def working(self):
        logging.info("ETAT : Kosmos en enregistrement")
        self._ledB.set_off()
        vitesse_mot=self.vitesse_moteur
        self.thread_camera.restart()
        self.motorThread.set_speed(vitesse_mot)
        temps_pose=self.tps_POSE
        temps_rotation60=self.tps_ROTATION60
        arret=0;
        past=int(time.time()) #prise du time de départ pour le mode MIKADO
        if (self.MODE==1): #Mode staviro   
            while True :
                self.clear_events()
                self.button_event.wait(temps_rotation60)
                if myMain.record_event.isSet():
                    print('break')
                    self.motorThread.set_speed(0)
                    self.motor_event.clear()
                    break
                else:
                    if myMain.motor_event.isSet():
                        print('moteuuur')
                        self.motorThread.set_speed(0)
                        i=0
                        while i!=temps_pose:
                            if myMain.record_event.isSet():
                                arret=1  #on met l'arret à 1. Cela permet de savoir qu'on a break la première boucle while
                                break
                            else :
                                time.sleep(1)
                                i=i+1
                        if (arret==1): # si on a break la première boucle while il faut sortir de la boucle while globale
                            arret=0 #on remet l'arret à 0 au cas où on relancerai après le STANDBY
                            print('break')
                            self.motorThread.set_speed(0)
                            self.motor_event.clear()
                            break #on sort le boucle while globale
                        self.motorThread.set_speed(vitesse_mot)
                        time.sleep(4)
                        self.motor_event.clear()
                    else:
                        print('pass')
                        self.motorThread.set_speed(0)
                        self.motor_event.clear()
                        i=0
                        while i!=temps_pose:
                            if myMain.record_event.isSet():
                                arret=1  #on met l'arret à 1. Cela permet de savoir qu'on a break la première boucle while
                                break
                            else :
                                time.sleep(3)
                                i=i+1
                        if (arret==1): # si on a break la première boucle while il faut sortir de la boucle while globale
                            arret=0 #on remet l'arret à 0 au cas où on relancerai après le STANDBY
                            self.motorThread.set_speed(0)
                            self.motor_event.clear()
                            break #on sort le boucle while globale
                        self.motorThread.set_speed(vitesse_mot)
                #sortie de boucle while 
            # self.record_event.wait(self.thread_camera.getRecordTime())
            self.state =KState.STOPPING
            
        else:#Mode MIKADO
            while True :
                self.clear_events()
                print('tout en haut')
                self.button_event.wait(temps_rotation60)
                print('nouvelle boucle')
                now=int(time.time())
                temps_consigne=self.tps_record
                temps=now-past
                if (temps>=temps_consigne): #quand on fait 15 minutes ( 900 secondes ) on arrête
                    temps=0
                    print('break')
                    self.motorThread.set_speed(0)
                    self.motor_event.clear()
                    break
                else:
                    if myMain.motor_event.isSet():
                        print('moteuuur')
                        self.motorThread.set_speed(0)
                        time.sleep(temps_pose)
                        self.motorThread.set_speed(vitesse_mot)
                        time.sleep(2)
                        self.motor_event.clear()
                    else:
                        print('pass')
                        self.motorThread.set_speed(0)
                        self.motor_event.clear()
                        time.sleep(temps_pose)
                        self.motorThread.set_speed(vitesse_mot)
                #sortie de boucle while 
            self.state = KState.STOPPING
    
    def stopping(self):
        logging.info("ETAT : Kosmos termine son enregistrement")
        self._ledR.startAgain()
        self.motorThread.pause()
        # Demander la fin de l'enregistrement
        self.thread_camera.stopCam()
        logging.info("thread caméra terminé")
        self._ledR.pause()
        if (self.MODE == 1 ):
            # prochain état : stopping
            self.state = KState.STANDBY
        else:
            self.state = KState.SHUTDOWN

    def shutdown(self):
        logging.info("ETAT : Kosmos passe à l'arrêt total")

        self.motorThread.stop_thread()  # Stop moteur
        self.thread_camera.closeCam()   # Stop caméra

        self.thread_csv.stop_thread()  # Arrêt de l'écriture du CVS
        self.thread_csv.join()
        logging.info("Thread csv terminé.")

        if self.thread_camera.is_alive():
            self.thread_camera.join()   # Caméra stoppée

        if self.motorThread.is_alive():
            self.motorThread.join()
        self.motorThread.power_off()

        if self._ledB.is_alive():
            self._ledB.stop()
            self._ledB.join()
            self._ledB.set_off()    # Led bleue stoppée
        if self._ledR.is_alive():
            self._ledR.stop()
            self._ledR.join()   # Led rouge stoppée
        self._ledR.set_on()
        logging.shutdown()

        # Commande de stop au choix arrêt du programme ou du PC
        if self._conf.get_val_int("SETT_SHUTDOWN") != 0 :
            os.system("sudo shutdown -h now")
        else :
            sys.exit(0)

    def modeRotatif(self):
        """programme principal du mode rotatif"""
        while True:
            if self.state == KState.STARTING:
                self.starting()
                time.sleep(1)
                self.clear_events()

            if self.state == KState.STANDBY:
                self.standby()
                time.sleep(0.5)
                self.clear_events()

            if self.state == KState.WORKING:
                self.working()
                time.sleep(0.5)
                self.clear_events()

            if self.state == KState.STOPPING:
                self.stopping()
                time.sleep(0.5)
                self.clear_events()

            if self.state == KState.SHUTDOWN:
                self.shutdown()

# Fin de la classe kosmos_main

def stop_cb(channel):
    """Callback du bp shutdown"""
    if not myMain.stop_event.isSet():
        logging.debug("bp shutdown pressé")
        myMain.stop_event.set()
        myMain.button_event.set()


def record_cb(channel):
    """Callback du bp start/stop record"""
    if not myMain.record_event.isSet():
        logging.debug("bp start/stop record pressé")
        myMain.record_event.set()
        myMain.button_event.set()

def motor_cb(channel):
    """Callback du bp stop moteur"""
    if not myMain.motor_event.isSet():
        logging.debug("bp stop moteur pressé")
        myMain.motor_event.set()
        myMain.button_event.set()

myMain = kosmos_main()

# Liens entre les boutons et les fonction de callback
GPIO.add_event_detect(myMain.STOP_BUTTON_GPIO, GPIO.FALLING, callback=stop_cb, bouncetime=500)
GPIO.add_event_detect(myMain.RECORD_BUTTON_GPIO, GPIO.FALLING, callback=record_cb, bouncetime=500)
GPIO.add_event_detect(myMain.MOTOR_BUTTON_GPIO, GPIO.FALLING, callback=motor_cb, bouncetime=500)

# Debut prog principal :
myMain.modeRotatif()
