import math
import time
import urllib

import commands
import serial


def floatERR(stringa):
    ritorno = None
    try:
        ritorno = float(stringa)
    except:
        ritorno = None
    return ritorno


f = open("/home/pi/AirPlatform/tensione.txt", "r")
appo_stringa = f.read()
f.close()
print(appo_stringa)
