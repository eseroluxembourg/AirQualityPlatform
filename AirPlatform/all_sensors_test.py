import datetime as dt
import os
import time

import commands
import requests
import RPi.GPIO as GPIO


def appendi_file(stringa):
    PlatformId = read_file("/home/pi/AirPlatform/PlatformID.txt")
    f = open("FAT" + PlatformId + ".txt", "a")
    f.write(stringa + "\n")
    f.close()


def read_file(nomeFile):
    file = open(nomeFile, "r")
    appo = file.readline()
    file.close()
    return appo


LED1 = 36
LED2 = 38

PlatformId = read_file("/home/pi/AirPlatform/PlatformID.txt")
if os.path.exists("FAT" + PlatformId + ".txt") == True:
    os.remove("FAT" + PlatformId + ".txt")


stringa = "FAT of the AQP" + PlatformId
appendi_file(stringa)
appendi_file(" ")

x = commands.getoutput("sudo ifconfig")
posizione = x.find("ether")
# print(posizione)
x = x[posizione + 6 :]

posizione = x.find("ether")
# print(posizione)
x = x[posizione + 6 :]

posizione = x.find(" ")
x = x[:posizione]
# print(x)
appendi_file("MAC Address " + x)
appendi_file(" ")
# print("This program stops the sending data to the webserver \n"
# print("To restart sending data to the Webserver please reboot the Platform \n")

# valore=raw_input("Prem invio per procedere:")
# x = commands.getoutput("sudo python /home/pi/AirPlatform/killManager.py")
# print (x)

x = commands.getoutput("sudo python3 /home/pi/AirPlatform/testTemperatura.py")
x = x[20:]
appendi_file(x)
n0 = str(dt.datetime.utcnow())
giorno = n0[0:19]
if (x.find("Temperature=") != -1) & (x.find("Temperature=") != -1):
    print(x)

    stringa = giorno + " - Temperature sensor Test Passed"
else:
    stringa = giorno + " - Temperature sensor Test NOT Passed"
appendi_file(stringa)
print(" ")
appendi_file(" ")

n0 = str(dt.datetime.utcnow())
giorno = n0[0:19]
x = commands.getoutput("sudo python /home/pi/AirPlatform/testArduino2.py")
appendi_file(x)
if (
    (x.find("CO=") != -1)
    & (x.find("NH3=") != -1)
    & (x.find("NO2") != -1)
    & (x.find("CO2=") != -1)
):
    print(x)
    stringa = giorno + " - CO NH3 NO2 CO2 sensors Test Passed"
else:
    print(x)
    stringa = giorno + " - CO NH3 NO2 CO2 sensors Test NOT Passed"
appendi_file(stringa)
print(" ")
appendi_file(" ")

n0 = str(dt.datetime.utcnow())
giorno = n0[0:19]
x = commands.getoutput("sudo python /home/pi/AirPlatform/aqiMax.py")
appendi_file(x)
if (x.find("PM2.5:") != -1) & (x.find("PM10:") != -1):
    print(x)
    stringa = giorno + " - PM2.5, PM10 sensors Test Passed"
else:
    stringa = giorno + " - PM2.5, PM10 sensors Test NOT Passed"
appendi_file(stringa)
print(" ")
appendi_file(" ")

n0 = str(dt.datetime.utcnow())
giorno = n0[0:19]
x = commands.getoutput("sudo python /home/pi/AirPlatform/gpsok.py")
appendi_file(x)
if (x.find("LAT=") != -1) & (x.find("LONG=") != -1):
    print(x)
    stringa = giorno + " GPS sensor Test Passed"
else:
    stringa = giorno + " GPS sensor Test NOTPassed"
appendi_file(stringa)
appendi_file(" ")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED1, 1)
time.sleep(1)
GPIO.output(LED1, 0)
time.sleep(1)
GPIO.output(LED2, 1)
time.sleep(1)
GPIO.output(LED2, 0)
time.sleep(1)


print(" ")
n0 = str(dt.datetime.utcnow())
giorno = n0[0:19]
x = commands.getoutput("ping -c 1 -w 1 www.google.it")
# appendi_file(x)
# print (x)
if x.find("0% packet loss") != -1:
    stringa = giorno + " Internet Connection Test Passed"
else:
    stringa = giorno + " Internet Connection Test NOT Passed"
appendi_file(stringa)
# x = commands.getoutput("sudo reboot")
#            break
#        time.sleep(3)
       
