import datetime as dt
import json
import os
import string
import time
import urllib
from os.path import exists

import Adafruit_DHT as dht
import commands
import requests
import RPi.GPIO as GPIO
import serial

# import RPi GPIO as gpio


def floatERR(stringa):
    ritorno = None
    try:
        ritorno = float(stringa)
    except:
        ritorno = None
    return ritorno


# verifica la lunghezza file log
nome_file = "log.txt"
x = commands.getoutput("du " + nome_file)
# print (x)

posizione = x.find(nome_file)
# valore=x[:posizione-1]
valore = x[: posizione - 1]
# print(posizione)
file_size = floatERR(valore)
print("file log size " + str(file_size))
if file_size > 300000:
    print("LOG moved")
    if exists("log.bck"):
        os.remove("log.bck")
    os.rename("log.txt", "log.bck")
