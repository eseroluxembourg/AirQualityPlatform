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


f = open("/home/pi/AirPlatform/latitudeLast.txt", "r")
latitudeLast = f.read()
f.close()


f = open("/home/pi/AirPlatform/longitudeLast.txt", "r")
longitudeLast = f.read()
f.close()

contatore_cicli = 0
# ser = serial.Serial(port)
while 1:
    contatore_cicli = contatore_cicli + 1
    if contatore_cicli > 50:
        print("error")
        break

    data = ser.readline()

    #
    # print(data)
    # if data[0:6] == '$GNRMC':
    if (data[0:6] == "$GNGGA") or (data[0:6] == "$GPGGA"):

        msg = pynmea2.parse(data)
        latval = msg.lat
        if msg.lat_dir == "S":
            latitude = latitude * (-1)
        latitude = str(latval)

        if floatERR(latitude) is not None:
            a = 1
        # print(2)
        # print(floatERR(latitude)+1)
        # if (floatERR(latitude)>4900) or (floatERR(latitude)<3300):
        # latitude=  ""

        if (floatERR(latitude) == None) or (msg.gps_qual == 0):
            latitude = ""

        if latitude == "":
            latitude = latitudeLast
            appostringa = " Last Known Point"
        else:

            latitudeLast = latitude

            f = open("/home/pi/AirPlatform/latitudeLast.txt", "w")
            f.write(latitude)
            f.close()
            appostringa = ""

        valore = float(latitude)

        appo_float = valore
        gradi = int(appo_float / 100)
        # print(gradi)
        dec = float(appo_float - gradi * 100)
        # print(dec)
        gra = dec * 100 / 60
        # print(gra)
        conversione = gradi + gra / 100
        # print(conversione)
        latitude = conversione

        longval = msg.lon
        if msg.lon_dir == "W":
            longval = longval * (-1)

        longitude = str(longval)

        # print(longitude) 8,20
        # print(floatERR(longitude))
        if floatERR(longitude) is not None:
            a = 1
            # if floatERR(longitude)<500 or floatERR(longitude)>2000:
            # longitude=  ""

        if (floatERR(longitude) == None) or (msg.gps_qual == 0):
            longitude = ""

        if longitude == "":
            longitude = longitudeLast
        else:
            longitudeLast = longitude
            f = open("/home/pi/AirPlatform/longitudeLast.txt", "w")
            f.write(longitude)
            f.close()
        valore = float(longitude)

        # converti in grad
        appo_float = valore
        gradi = int(appo_float / 100)
        # print(gradi)
        dec = float(appo_float - gradi * 100)
        # print(dec)
        gra = dec * 100 / 60
        # print(gra)
        conversione = gradi + gra / 100
        # print(conversione)
        longitude = conversione
        # inserisce il grado
        # longitude=longitude[:3] + "%C2%B0" + longitude[3:]
        # print(longitude)

        concatlong = "LAT= " + str(latitude) + ", LONG=" + str(longitude) + ", "
        # concatlong=concatlong.replace(' ', '|')

        print(concatlong + appostringa)

        break
