#!/usr/bin/env python3
# coding: utf-8

# D Hanon 20 octobre 2020

from threading import Thread, Event
import RPi.GPIO as GPIO  # Importe la bibliotheque pour contrôler les GPIOs
import time  # bibliotheque pour delay
import logging


class kosmos_led(Thread):

    def __init__(self, aGpioPort: int):
        Thread.__init__(self)
        GPIO.setmode(GPIO.BCM)  # on utilise bien les numero de GPIO et pas les numero de broches
        GPIO.setwarnings(False)  # On desactive les messages d'alerte
        self._GpioPort = aGpioPort
        GPIO.setup(self._GpioPort, GPIO.OUT)  # Active le controle du GPIO
        if not self.get_state():
            self.set_off()
        self._mstop = False
        self._isRunnig = False
        self._pause = False
        self._continue_event = Event()
        logging.info(f"Led sur GPIO {self._GpioPort} initialisée")

    def run(self):
        """Corps du thread; s'arrête lorque le self._mstop est vrai; appeler stop()"""
        logging.debug(f"Debut thread Led sur GPIO {self._GpioPort}")
        self._isRunnig = True
        time_step = 0.3
        while self._mstop is False:
            if not self.get_state():
                self.set_on()
            else:
                self.set_off()
            time.sleep(time_step)
            if self._pause:
                self.set_off()
                self._continue_event.wait()
                logging.debug(f"Reprise thread Led sur GPIO {self._GpioPort}")
                self._continue_event.clear()

        self.set_off()
        logging.debug(f"Fin thread Led sur GPIO {self._GpioPort}")

    def stop(self):
        """Arrête définitivement le thread (relance = plantage)"""
        self._mstop = True
        if self._pause:
            self._pause = False
            self._continue_event.set()

    def pause(self):
        """Mise en pause du tread"""
        self._pause = True
        logging.debug(f"Pause thread Led sur GPIO {self._GpioPort}")

    def startAgain(self):
        """Fin de la pause du tread"""
        if self._isRunnig:
            self._pause = False
            self._continue_event.set()
        else:
            self.start()

    def set_on(self):
        GPIO.output(self._GpioPort, GPIO.HIGH)

    def set_off(self):
        GPIO.output(self._GpioPort, GPIO.LOW)

    def get_state(self):
        return GPIO.input(self._GpioPort)
