import datetime as dt
import os
import string
import sys
import time
import urllib

import Adafruit_DHT as dht
import commands
import pynmea2
import serial


def appendi_file(stringa):

    f = open("gpslog.txt", "a")
    f.write(stringa)
    f.close()


def floatERR(stringa):
    ritorno = None
    try:
        ritorno = float(stringa)
    except:
        ritorno = None
    return ritorno


port = "/dev/ttyAMA0"

# create a serial object
ser = serial.Serial(port, baudrate=9600, timeout=3)


contatore_cicli = 0
# ser = serial.Serial(port)

while 1:
    contatore_cicli = contatore_cicli + 1
    if contatore_cicli > 100:
        # print("error")
        # appendi_file("error"+"\n")

        break

    data = ser.readline()
        print(data)
             
