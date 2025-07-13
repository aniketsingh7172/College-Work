import sys
from cx_Freeze import setup, Executable

import os

PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)


include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll'))]

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable('calculator.py', base=base,icon=r"C:\Users\acer\Desktop\radhe\ck.ico",
                   shortcut_name="My Calculator",
                   shortcut_dir="DesktopFolder")]

setup(name='Rajput Aniket Calulator Test Installer',
      version='1.0',
      author="Rajput",
      description='My First Installer',
      options={'build_exe': {'include_files': include_files}},
      executables=executables)