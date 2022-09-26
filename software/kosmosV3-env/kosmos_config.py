#!/usr/bin/python
# coding: utf-8

import logging
import configparser
import os.path
import subprocess
from datetime import datetime


CONF_FILE = "kosmos_config.ini"
USB_ROOT_PATH = "/media/pi"
BASIC_SECTION = "KOSMOS"


class KosmosConfig:
    """
    Gestion des paramètres et leur lecture depuis le fichier .ini
    Ce fichier pouvant etre sur la clef ou dans le repertoire courant
    """

    def find_usb_path(self):
        """ cherche et retourne le repertoire de la clef usb"""
        logging.debug(f"Recherche clef usb lancement script : ./kosmos_find_usb.sh {USB_ROOT_PATH}")
        result = subprocess.run(["./kosmos_find_usb.sh",
                                 USB_ROOT_PATH],
                                capture_output=True)
        logging.debug(f"code retour recherche clef {result.returncode}")
        logging.debug(f"rech clef {result.stdout.decode()}")
        if result.returncode == 0:
            return result.stdout.decode()
        return ""

    def get_usb_path(self) -> str:
        """Retourne le repertoire de la clef usb.
        Il faut que la recherche ait déjà été lancée
        sinon la chaine est vide."""
        return self._usb_path

    def getCurentDir(self) -> str:
        return self._cur_dir

    def __init__(self):
        logging.debug("DEBUT INIT config")
        self.config = configparser.ConfigParser()
        self._usb_path = self.find_usb_path()
        self._cur_dir = os.getenv('PWD')  # Repertoire courant
        if self._usb_path != "" and os.path.isfile(self._usb_path + '/' + CONF_FILE):
            self.config.read(self._usb_path + '/' + CONF_FILE)
            logging.info(f"Fichier de configuration lu sur USB {self._usb_path}/{CONF_FILE}")
        else:
            logging.debug(f"Recherche fichier de configuration local {self._cur_dir}/{CONF_FILE}")
            if self._cur_dir is not None and os.path.isfile(self._cur_dir + '/' + CONF_FILE):
                self.config.read(self._cur_dir + '/' + CONF_FILE)
                logging.info(f"Fichier de configuration lu en local {self._cur_dir}/{CONF_FILE}")
            else:
                logging.error("Pas de fichier de configuration")
                exit(-1)

    def print_all(self):
        """Affiche le fichier de configuration (pour debug). """
        # Parcourt des sections
        for sec in self.config.sections():
            logging.info("section : {}".format(sec))
            # parcourir parametres et valeurs
            for name, value in self.config.items(sec):
                logging.info("{} = {}".format(name, value))

    def get_date(self) -> str:
        """Retourne la date formatée en string"""
        date = datetime.now()
        return date.strftime("%Y-%m-%d-%H-%M-%S")
    
    def get_val(self, aKey, aSection=BASIC_SECTION):
        """
        Retourne la valeur d'un paramètre dont le nom est passé en argument.
        Parameters:
            aKey (str): nom du paramètre de config recherché
            aSection (str) : section du fichier ini dans le quel on recherche
                    le paramètre de config.
        """
        return self.config.get(aSection, aKey)

    def get_val_int(self, aKey, aSection=BASIC_SECTION):
        """
        Retourne la valeur d'un paramètre dont le nom est passé en argument.
        Parameters:
            aKey (str): nom du paramètre de config recherché
            aSection (str) : section du fichier ini dans le quel on recherche
                    le paramètre de config.
        """
        return self.config.getint(aSection, aKey)

    def copy_file(self, aFileName: str) -> bool:
        """ copy le fichier vers la clef USB """
        logging.debug(f"cp {aFileName} {self._usb_path}")
        if self._usb_path != "":
            result = subprocess.run(["sudo", "cp", aFileName, self._usb_path],
                                    capture_output=True)
            if result.returncode == 0:
                return True
        return False

    def rm_file(self, aFileName: str) -> bool:
        """ Supprime le fichier dans le répertoire courant
        NE PAS OUBLIER DE LE COPIER la clef USB """
        logging.debug(f"rm {aFileName}")
        result = subprocess.run(["rm", aFileName],
                                capture_output=True)
        if result.returncode == 0:
            return True
        return False

    def moove_file(self, aFileName: str) -> bool:
        """ Déplacer le fichier après la copie la clef USB """
        if self.copy_file(aFileName) is True:
            if self.rm_file(aFileName):
                logging.info(f"Le fichier {aFileName} a bien été déplacé vers la clef USB.")
                return True
        logging.warning(f"Impossible de déplacer le {aFileName} vers la clef USB.")
        return False
    
    
