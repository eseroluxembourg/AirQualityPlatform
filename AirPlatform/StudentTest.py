import time

import commands
import requests
import RPi.GPIO as GPIO

LED1 = 36
LED2 = 38


print("This program stops the sending data to the webserver \n")
print("To restart sending data to the Webserver please reboot the Platform \n")

valore = raw_input("Prem invio per procedere:")
x = commands.getoutput("sudo python /home/pi/AirPlatform/killManager.py")
print(x)

while 1:
    # x = commands.getoutput("sudo clear")
    print(x)
    print("Premi ")
    print("1 Per test sensore umidita' e temperatura ")
    print("2 Per test Arduino (CO,NH3,NO2,CO2) ")
    print("3 Per test sensore Particolato ")
    print("4 Per test del GPS ")
    print("5 Per test del LED")
    print("6 Per test connessione wifi")
    print("7 Inserire Nome Instituto  ")
    print("8 Per uscire e fare il reboot della piattaforma ")
    valore = raw_input("Inserisci la scelta: ")
    if valore == "1":

        x = commands.getoutput("sudo python /home/pi/AirPlatform/testTemperatura.py")
        if (x.find("Temperature=") != -1) & (x.find("Temperature=") != -1):
            print(x)
            print("Test Sensore OK")
        else:
            print("Test Sensore Non Passato")

    if valore == "2":
        x = commands.getoutput("sudo python /home/pi/AirPlatform/testArduino2.py")
        if (
            (x.find("CO=") != -1)
            & (x.find("NH3=") != -1)
            & (x.find("NO2") != -1)
            & (x.find("CO2=") != -1)
        ):
            print(x)
            print("Test Sensore OK")
        else:
            print(x)
            print("Test Sensore Non Passato")

    if valore == "3":
        x = commands.getoutput("sudo python /home/pi/AirPlatform/aqiMax.py")
        if (x.find("PM2.5:") != -1) & (x.find("PM10:") != -1):
            print(x)
            print("Test Sensore OK")
        else:
            print("Test Sensore Non Passato")

    if valore == "4":
        x = commands.getoutput("sudo python /home/pi/AirPlatform/gpsok.py")
        if (x.find("LAT=") != -1) & (x.find("LONG=") != -1):
            print(x)
            print("Test Sensore OK")
        else:
            print("Test Sensore Non Passato")

    if valore == "5":

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

    if valore == "6":
        x = commands.getoutput("ping -c 1 -w 1 www.google.it")
        # print (x)
        if x.find("0% packet loss") != -1:
            print("CONNESSIONE INTERNET OK")
        else:
            print("NO CONNESSIONE INTERNET ")

    if valore == "7":
        nome_wifi = raw_input("Inserire Nome Instituto : ")

        f = open(
            "/home/pi/AirPlatform/istituto.dat", "w"
        )  # riapriamo il file in lettura
        f.write(nome_wifi)  # leggiamo tutto il contenuto del file
        print("Nome Instituto " + nome_wifi)
        f.close()  # chiudiamo il file

    if valore == "8":
        x = commands.getoutput("sudo reboot")
        break
    time.sleep(3)
       
