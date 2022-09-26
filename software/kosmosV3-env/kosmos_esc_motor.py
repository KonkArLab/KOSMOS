#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Controle du moteur ESC
Utilise la lib pigpio

- Modif du 20 janvier pour remettre la calibration.
- Modif du 1 février : changement de la méthode d'armement.
- Modif du 26 février 2021 : ajout du relai d'alimentation et utilisation pour calibrer et armer
"""
import logging
import RPi.GPIO as GPIO  # Importe la bibliotheque pour contrôler les GPIOs
import time
import pigpio  # importing GPIO library
from threading import Thread
from threading import Event

from kosmos_config import *
import subprocess


class komosEscMotor(Thread):

    def __init__(self, aConf: KosmosConfig):
        Thread.__init__(self)
        # os.system ("sudo pigpiod") #Launching GPIO library
        result = subprocess.run(["sudo", "pigpiod"], capture_output=True) 
        time.sleep(0)  # FIXME attendre que la lib soit chargée ?
        # vérif avec sudo killall pigpiod
        if result.returncode == 0:
            logging.info(f"Moteur : libairie pigpiod chargée.")
        else:
            logging.error(f"Problème avec libairie pigpiod {result.stdout.decode()}")

        self.gpio_port = aConf.get_val_int("SETT_ESC_MOTOR_GPIO")
        self.gpio_power_port = aConf.get_val_int("SETT_POWER_MOTOR_GPIO")
        logging.info(f"Moteurs sur GPIO {self.gpio_port}.")
        self._gpio = pigpio.pi()
        GPIO.setup(self.gpio_power_port, GPIO.OUT)  # Active le controle du GPIO
        self._gpio.set_servo_pulsewidth(self.gpio_port, 0)
        self.max_value = aConf.get_val_int("SETT_ESC_MOTOR_MAX_VAL")
        self.min_value = aConf.get_val_int("SETT_ESC_MOTOR_MIN_VAL")
        self.fav_value = aConf.get_val_int("SETT_ESC_MOTOR_FAVORITE_VAL")

        # temps d'attente entre deux arrêts
        self._wait_time = aConf.get_val_int("SETT_MOTOR_STOP_TIME")
        # temps de fonctionnement (à ajuster pour avoir 60°)
        self._run_time = aConf.get_val_int("SETT_MOTOR_RUN_TIME")

        # Evénement pour commander l'arrêt du Thread
        self._pause_event = Event()
        self._continue_event = Event()
        self._t_stop = False
    
    def power_on(self):
        """Commande le relai d'alimentation de l'ESC"""
        GPIO.output(self.gpio_power_port, GPIO.HIGH) # Coupure du relai

    def power_off(self):
        """Commande le relai d'alimentation de l'ESC"""
        GPIO.output(self.gpio_power_port, GPIO.LOW) # Coupure du relai

    def set_speed(self, aSpeed):
        """Lancement à la vitesse passée en paramètre
        1000 < vitesse < 2100 """
        self._gpio.set_servo_pulsewidth(self.gpio_port, aSpeed)
        logging.debug(f"Moteur vitesse {aSpeed}.")
    
    def moove(self, aSpeed, aTime):
        """Lancement à la vitesse et temps passés en paramètre
        0 < vitesse < 2100 """
        self._gpio.set_servo_pulsewidth(self.gpio_port, aSpeed)
        logging.debug(f"Moteur vitesse {aSpeed}. {aTime} secondes")
        time.sleep(aTime)
    
    def calibrate(self):
        """Procedure de calibration de l'esc"""
        self.set_speed(0)
        print("Déconnectez la batterie de l\'ESC et appuyez sur Enter")
        inp = input()
        if inp == '':
            self.set_speed(self.max_value)
            print(f'Moteur sur port {self.gpio_port} vitesse max : {self.max_value}')
            print("Connectez la batterie maintenant")
            print("Vous allez entendre 2 bips, puis quand ...")
            print("vous entendrez une tonnalité descendante, appuyez sur Entrer")
            inp = input()
            if inp == '':
                self.set_speed(self.min_value)
                print("... Tonalité spéciale")
                time.sleep(7)
                print("On attend toujours.")
                time.sleep(5)
                print("et on continue d\'attendre.")
                print(f'Moteur sur port {self.gpio_port} vitesse min : {self.min_value}')
                self.set_speed(self.min_value)
                time.sleep(2)
                print("ESC prêt")
                self.set_speed(self.min_value)
                time.sleep(1)
                print("Calibatrion terminée.")
                print(f'Moteur sur port {self.gpio_port} vitesse : {0}')
                self.set_speed(0)
            else:
                print("Calibratrion abandonnée.")
                return -1
        else:
            print("Calibratrion abandonnée.")
            return -1
        logging.info('Calibatrion moteur et ESC OK.')
        return 0
    
    def autoCal(self):
        """Procedure de calibration de l'esc"""
        
        self.set_speed(0)        
        self.power_off() # Coupure du relai
        logging.debug("Coupure relai moteur 5 secondes.")
        time.sleep(5)
        
        self.set_speed(self.max_value)
        self.power_on()
        self.moove(self.max_value, 5) #5s vitesse max
        
        self.moove(self.min_value, 10) #10s vitesse min
        
        self.set_speed(0)
        
        logging.info('Calibatrion moteur et ESC OK.')
        return 0

    def arm(self):
        """This is the arming procedure of an ESC"""
        logging.debug('Armement moteur !')
        self.moove(self.min_value, 10) #10s vitesse min
        #self.moove(self.fav_value, self._run_time) #tourner temps d'un cycle
        #self.moove(self.min_value, 1) #10s vitesse min
        self.moove(self.fav_value, 1) #tourner temps d'un cycle

        self.set_speed(0)
        logging.info('Moteur et ESC prêts !')

    def autoArm(self): 
        self.power_on()
        self.arm()
      
    def arret_complet(self):
        """This will stop every action your Pi is performing for ESC ofcourse."""
        self.set_speed(0)
        self._gpio.stop()
        logging.info('Moteur arrêt total')

    def run(self):
        """ Corps du thread; s'arrête lorque le stopevent est vrai
        https://python.developpez.com/faq/index.php?page=Thread """
        logging.info('Debut du thread moteur ESC.')

        while not self._t_stop:
            self.set_speed(0)
            logging.debug(f'Thred moteur arrêt : attente {self._wait_time} secondes.')
            self._pause_event.wait(self._wait_time)
            if not self._pause_event.isSet():
                # Si on n'est pas en pause on continue
                self.set_speed(self.fav_value)
                logging.debug(f'Thred moteur tourne : attente {self._run_time} secondes.')
                # Ne pas stopper le moteur en vol autrement on met la croix de malte HS ...
                if not self._t_stop:
                    time.sleep(self._run_time)
            else:
                # Si on est pas en pause on attend la reprise.
                logging.debug(f'Moteur attente reprise')
                self._continue_event.wait()
        # End While
        self.set_speed(0)
        self.arret_complet()
        logging.info('Fin du thread moteur ESC.')

    def stop_thread(self):
        """positionne l'évènement qui va provoquer l'arrêt du thread"""
        self._t_stop = True
        self._continue_event.set()
        self._pause_event.set()

    def pause(self):
        """suspend le thread pour pouvoir le redémarrer."""
        self._continue_event.clear()
        self._pause_event.set()

    def restart(self):
        """Relance le thread"""
        if self.is_alive():
            self._pause_event.clear()
            self._continue_event.set()
        else:
            self.start()
