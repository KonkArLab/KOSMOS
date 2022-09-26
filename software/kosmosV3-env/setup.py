# cx_freeze
# Installation 
# pip3 install cx_Freeze
# Utilisation
# python3 setup.py build


import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "kosmos_cam",
        version = "0.1.2",
        description = "Kosmos programme",
        # options = {"build_exe": build_exe_options},
        executables = [Executable("kosmos_main.py", base=base), Executable("tu_moteur.py", base=base)])
