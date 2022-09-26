#!/usr/bin/python
# coding: utf-8
from datetime import datetime

from threading import Thread
from threading import Event

import logging
import os
import ms5837  # librairie du catpeur de pression et temperature

from kosmos_config import *


class kosmosCSV(Thread):
    """Classe dérivée de Thread qui gère l'enregistrement du CSV"""

    def __init__(self, aConf: KosmosConfig):
        """Constructeur de la classe kosmosCSV
        Parameters :
            aConf : la classe qui lit le fichier de configuration

        Sont lus dans le fichier de configuration :
            - SETT_CSV_STEP_TIME la période échtillonage
            - SETT_CSV_FILE_NAME la base du nom du fichier CSV
        """
        Thread.__init__(self)
        # Evénement pour commander l'arrêt du Thread
        self._stopevent = Event()

        self._time_step = aConf.get_val_int("SETT_CSV_STEP_TIME")
        self._file_name = aConf.get_val("SETT_CSV_FILE_NAME") + "_" + aConf.get_date() + ".csv"
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        os.chdir("media")
        os.chdir("pi")
        os.chdir("00clef")
        os.chdir("CSV")
        self._cvs_file = open(self._file_name, 'w')
        ligne = "heure ; pression (mb); température °C ; profondeur (m)"
        logging.debug(f"Ecriture CSV : {ligne}")
        self._cvs_file.write(ligne + '\n')
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        os.chdir("home")
        os.chdir("pi")
        os.chdir("kospython")

        self._press_sensor_ok = False
        try:
            # capteur T et P Default I2C bus is 1 (Raspberry Pi 3)
            self.pressure_sensor = ms5837.MS5837_30BA()
            if self.pressure_sensor.init():
                self._press_sensor_ok = True
            logging.info("Capteur de pression OK")
        except:
            logging.error("Erreur d'initialisation du capteur de pression")
        self.stop = False

    def run(self):
        """Ecriture des données sur le fichier CSV
        Corps du thread; s'arrête lorque le self.stop est vrai (appeler stop_thread())
        https://python.developpez.com/faq/index.php?page=Thread """
        while self.stop is False:
            pressStr = ""
            tempStr = ""
            if self._press_sensor_ok:
                if self.pressure_sensor.read():
                    press = self.pressure_sensor.pressure()  # Default is mbar (no arguments)
                    pressStr = f'{press:.1f}'
                    temp = self.pressure_sensor.temperature()  # Default is degrees C (no arguments)
                    tempStr = f'{temp:.2f}'
                    prof=(press-1000)/100
                    profStr=f'{prof:2f}'
            vDate = datetime.now()
            # vHeure = str(vDate.hour) + ':' + str(vDate.minute) + ':' + str(vDate.second)
            date = datetime.now()
            vHeure = date.strftime("%H:%M:%S")
            ligne = f'{vHeure} ; {pressStr} ; {tempStr} ; {profStr}'
            logging.debug(f"Ecriture CSV : {ligne}")
            self._cvs_file.write(ligne + '\n')

            # Attendre le prochain enregistrement ou l'évènement d'arrêt.
            self._stopevent.wait(self._time_step)

        self._cvs_file.close()
        return 0

    def get_file_name(self) -> str:
        """ retourne le nom du fichier CSV généré"""
        return self._file_name

    def stop_thread(self):
        """positionne l'évènement qui va provoquer l'arrêt du thread"""
        self.stop = True
        self._stopevent.set()
