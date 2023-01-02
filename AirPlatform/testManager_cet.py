import datetime as dt
import json
import string
import time
import urllib

import Adafruit_DHT as dht
import commands
import requests
import RPi.GPIO as GPIO
import serial

LED1 = 36
LED2 = 38

precedente_lat_grad = 41.827753
precedente_long_grad = 12.6750968333


def appendi_file(stringa):

    f = open("log.txt", "a")
    f.write(stringa)
    f.close()


def floatERR(stringa):
    ritorno = None
    try:
        ritorno = float(stringa)
    except:
        ritorno = None
    return ritorno


GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)


f = open("PlatformID.txt")
appo_stringa = f.read()
Device = int(appo_stringa)
print("Air quality Platform " + str(Device))
f.close()
# trova arduino
x = commands.getoutput("sudo python trovaArduino.py")
print("Trova Arduino")
print(x)

time.sleep(60)
n0 = str(dt.datetime.now())
appo_stringa = n0[0:19]
appendi_file("\n" + appo_stringa + " ********************START******************* \n")

while 1:
    x = commands.getoutput("ping -c 1 -w 1 www.google.it")

    if x.find("0% packet loss") != -1:
        print("CONNESSIONE INTERNET OK")
        GPIO.output(LED2, 1)
    else:
        print("NO CONNESSIONE INTERNET ")
        GPIO.output(LED2, 0)

    GPIO.output(LED1, 1)
    x = commands.getoutput("sudo python3 testTemperatura.py")
    print(x)
    appendi_file(" * " + x)
    if (x.find("Temperature=") != -1) & (x.find("Humidity=") != -1):
        posizione = x.find("Temperature=")
        posizione2 = x.find("*C")
        valoreSensore = x[posizione + 12 : posizione2]
        valore = floatERR(valoreSensore)
        temperature = valore
        print("Temperature " + str(valore))
        # Humidity=40.1%
        posizione = x.find("Humidity=")
        posizione2 = x.find("%")
        valoreSensore = x[posizione + 9 : posizione2]
        valore = floatERR(valoreSensore)
        umidita = valore
        print("Humidity " + str(umidita))
    else:
        umidita = None
        temperature = None
    # if umidita>100:

    # umidita=None
    # temperature=None

    GPIO.output(LED1, 0)
    x = commands.getoutput("sudo python testArduino2.py")
    print(x)
    appendi_file(x)
    if (
        (x.find("CO=") != -1)
        & (x.find("NH3=") != -1)
        & (x.find("NO2") != -1)
        & (x.find("CO2=") != -1)
    ):
        posizione = x.find("CO=")
        posizione2 = x.find("ppm")
        valoreSensore = x[posizione + 3 : posizione2]
        valore = floatERR(valoreSensore)
        CO = valore
        print("CO " + str(CO))
        x = x[posizione2 + 3 :]

        posizione = x.find("NH3=")
        posizione2 = x.find("ppm")
        valoreSensore = x[posizione + 4 : posizione2]

        valore = floatERR(valoreSensore)
        NH3 = valore
        print("NH3 " + str(NH3))
        x = x[posizione2 + 3 :]

        posizione = x.find("NO2=")
        posizione2 = x.find("ppm")
        valoreSensore = x[posizione + 4 : posizione2]
        # print(valoreSensore)
        valore = floatERR(valoreSensore)
        NO2 = valore
        print("NO2 " + str(NO2))
        x = x[posizione2 + 3 :]

        posizione = x.find("CO2=")
        posizione2 = x.find("ppm")
        valoreSensore = x[posizione + 4 : posizione2]

        valore = floatERR(valoreSensore)
        CO2 = valore
        print("CO2 " + str(CO2))
    else:
        CO2 = None
        NO2 = None
        NH3 = None
        CO = None
    GPIO.output(LED1, 1)
    x = commands.getoutput("sudo python aqiMax.py")
    print(x)
    appendi_file(x)
    if (x.find("PM2.5:") != -1) & (x.find("PM10:") != -1):

        posizione = x.find("PM2.5:")
        posizione2 = x.find("ppm")
        valoreSensore = x[posizione + 6 : posizione2]
        valore = floatERR(valoreSensore)
        PM25 = valore
        print("PM2.5 " + str(PM25))
        x = x[posizione2 + 3 :]

        posizione = x.find("PM10:")
        posizione2 = x.find("ppm")
        valoreSensore = x[posizione + 5 : posizione2]

        valore = floatERR(valoreSensore)
        PM10 = valore
        print("PM10 " + str(PM10))
    else:
        PM10 = None
        PM25 = None

    GPIO.output(LED1, 0)

    x = commands.getoutput("sudo python gpsok.py")
    print(x)
    appendi_file(x)
    if (x.find("LAT=") != -1) & (x.find("LONG=") != -1):

        posizione = x.find("LAT=")
        posizione2 = x.find(",")
        valoreSensore = x[posizione + 4 : posizione2]
        valore = floatERR(valoreSensore)
        LAT = valore
        precedente_lat_grad = LAT
        print("LAT " + str(LAT))
        x = x[posizione2 + 2 :]

        posizione = x.find("LONG=")
        posizione2 = x.find(",")
        valoreSensore = x[posizione + 5 : posizione2]
        valore = floatERR(valoreSensore)
        LONG = valore
        precedente_long_grad = LONG
        print("LONG " + str(LONG))

        if x.find("Last Known Point") != -1:
            GPS_precision = 0
            LONG = precedente_long_grad
            LAT = precedente_lat_grad
        else:
            GPS_precision = 1
        print("GPS precision " + str(GPS_precision))
    else:
        LONG = precedente_long_grad
        LAT = precedente_lat_grad
        GPS_precision = 2

    x = commands.getoutput("sudo python tensioneArduino.py")
    print(x)
    sensor4 = x
    appendi_file(x)

    GPIO.output(LED1, 1)
    n0 = str(dt.datetime.now())
    appo_stringa = n0[0:19]

    giorno = appo_stringa

    valori = {
        "device_id": Device,
        "acquisition_date": giorno,
        "latitude": LAT,
        "longitude": LONG,
        "gps_precision": GPS_precision,
        "pm25": PM25,
        "pm10": PM10,
        "humidity": umidita,
        "temperature": temperature,
        "no2": NO2,
        "co2": CO2,
        "nh3": NH3,
        "co": CO,
        "sensor1": 10.0,
        "sensor2": 10.0,
        "sensor3": 10.0,
        "sensor4": sensor4,
        "sensor5": "add info",
    }

    payload_json = json.dumps(valori)
    f = open("valori.dat", "w")
    f.write(payload_json)
    f.close()

    x = commands.getoutput("sudo python sendWebServer.py")
    print(x)
    appendi_file(x)

    x = commands.getoutput("ping -c 1 -w 1 www.google.it")
    # print (x)
    if x.find("0% packet loss") != -1:
        print("CONNESSIONE INTERNET OK")
        connessione = " CONNESSIONE INTERNET OK"
        GPIO.output(LED2, 1)
    else:
        print("NO CONNESSIONE INTERNET ")
        GPIO.output(LED2, 0)
        connessione = " CONNESSIONE INTERNET OK"

    x = commands.getoutput("sudo python log.py")
    print(x)
    appendi_file(x + connessione + "\n")

    for count in range(1, 55):

        GPIO.output(LED1, 0)
        time.sleep(0.5)
        GPIO.output(LED1, 1)
        time.sleep(0.5)
