#!/usr/bin/python
import datetime
import os
import subprocess
import time
import tkinter
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import pandas as pd
import RPi.GPIO as GPIO

LED1 = 36
LED2 = 38
stringa_finale = ""

root = tkinter.Tk()


def floatERR(stringa):
    ritorno = None
    try:
        ritorno = float(stringa)
    except:
        ritorno = None
    return ritorno


def closeWindow():
    messagebox.showinfo(
        title="confirmation",
        message="Important! you will need to restart the AQP if you want sending data to the ESA webserver",
    )
    root.destroy()


def temperatura():
    x = subprocess.getoutput("sudo python3 /home/pi/AirPlatform/testTemperatura.py")
    if (x.find("Temperature=") != -1) & (x.find("Humidity=") != -1):
        # messagebox.showinfo("test temperature ",x)
        # firstLabelT.destroy()

        firstLabelT = tkinter.Label(btnFrame, text="Test passed: " + x)
        firstLabelT.grid(row=1, column=1, padx=30, pady=2)

    else:
        # firstLabelT.destroy()
        # firstLabelT = tkinter.Label(btnFrame, text="                                                                  ")
        # firstLabelT.grid(row=1, column=1, padx=30, pady=2)

        firstLabelT = tkinter.Label(
            btnFrame,
            text="Test not passed                                                                                                     ",
        )
        firstLabelT.grid(row=1, column=1, padx=30, pady=2)
        # firstLabelT.config(text="Test not passed")


def arduino():
    x = subprocess.getoutput("sudo python /home/pi/AirPlatform/testArduino2.py")

    if (
        (x.find("CO=") != -1)
        & (x.find("NH3=") != -1)
        & (x.find("NO2") != -1)
        & (x.find("CO2=") != -1)
    ):
        appostringa = x.split(",")

        firstLabelA = tkinter.Label(btnFrame, text="Test passed: " + appostringa[0])
        firstLabelA.grid(row=2, column=1, padx=30, pady=2)
        firstLabelA = tkinter.Label(btnFrame, text=appostringa[1])
        firstLabelA.grid(row=3, column=1, padx=30, pady=2)
        firstLabelA = tkinter.Label(btnFrame, text=appostringa[2])
        firstLabelA.grid(row=4, column=1, padx=30, pady=2)
        firstLabelA = tkinter.Label(btnFrame, text=appostringa[3])
        firstLabelA.grid(row=5, column=1, padx=30, pady=2)
    else:
        firstLabelA = tkinter.Label(btnFrame, text="Test not passed")
        firstLabelA.grid(row=2, column=1, padx=30, pady=2)


def pm():

    x = subprocess.getoutput("sudo python /home/pi/AirPlatform/aqiMax.py")
    if (x.find("PM2.5:") != -1) & (x.find("PM10:") != -1):
        firstLabelP = tkinter.Label(btnFrame, text="Test passed: " + x)
        firstLabelP.grid(row=6, column=1, padx=30, pady=2)
    else:
        firstLabelP = tkinter.Label(btnFrame, text="Test not passed")
        firstLabelP.grid(row=6, column=1, padx=30, pady=2)


def gps():
    x = subprocess.getoutput("sudo python /home/pi/AirPlatform/gpsok.py")
    if (x.find("LAT=") != -1) & (x.find("LONG=") != -1):
        firstLabelG = tkinter.Label(btnFrame, text="Test passed: " + x)
        firstLabelG.grid(row=7, column=1, padx=30, pady=2)
    else:
        firstLabelG = tkinter.Label(btnFrame, text="Test not passed")
        firstLabelG.grid(row=7, column=1, padx=30, pady=2)


def led():
    firstLabelL = tkinter.Label(btnFrame, text="Check the AQP led")
    firstLabelL.grid(row=8, column=1, padx=30, pady=2)
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


def internet():
    x = subprocess.getoutput("ping -c 1 -w 1 www.google.it")

    if x.find("0% packet loss") != -1:
        firstLabelI = tkinter.Label(
            btnFrame, text="Test passed: internet connection OK"
        )
        firstLabelI.grid(row=9, column=1, padx=30, pady=2)
    else:
        firstLabelI = tkinter.Label(btnFrame, text="Test not passed")
        firstLabelI.grid(row=9, column=1, padx=30, pady=2)


def calibra():
    risposta = messagebox.askyesno(
        "Yes|No", "Do you want to proceed to correct the sensors error in Clean air?"
    )

    if risposta == True:
        x = subprocess.getoutput("sudo python /home/pi/AirPlatform/Calibra.py")
        firstLabelI = tkinter.Label(btnFrame, text=x)
        firstLabelI.grid(row=13, column=1, padx=30, pady=2)


def gps_info():
    x = subprocess.getoutput("sudo python /home/pi/AirPlatform/dammi_info_gps.py")
    messagebox.showinfo("gps info", x)


def reboot():
    risposta = messagebox.askyesno("Yes|No", "Do you want to reboot the AQP?")

    if risposta == True:
        x = subprocess.getoutput("sudo reboot -h now")
        # print(x)


def position():
    risposta = messagebox.askyesno(
        "Yes|No", "Do you want to proceed to set latitude and longitude?"
    )

    if risposta == True:
        lat = floatERR(userInputLAT.get())
        long = floatERR(userInputLONG.get())
        # print(lat,long)

        intero = int(lat)
        # print(intero)
        latitudine = round((lat - intero), 8)
        latitudine = round(latitudine * 0.6 + intero, 8)
        # print(latitudine)
        latitudine = round(latitudine * 100, 8)
        # print(latitudine)
        f = open("/home/pi/AirPlatform/latitudeLast.txt", "w")
        f.write(str(latitudine))
        f.close()

        intero = int(long)
        # print(intero)
        longitudine = round((long - intero), 8)
        longitudine = round(longitudine * 0.6 + intero, 8)
        # print(longitudine)
        longitudine = round(longitudine * 100, 8)
        # print(longitudine)
        f = open("/home/pi/AirPlatform/longitudeLast.txt", "w")
        f.write(str(longitudine))
        f.close()
    else:

        appo_float = floatERR(latitudeLast)
        gradi = int(appo_float / 100)
        # print(gradi)
        dec = float(appo_float - gradi * 100)
        # print(dec)
        gra = dec * 100 / 60
        # print(gra)
        conversione = round(gradi + gra / 100, 10)
        # print(conversione)
        latitude = round(conversione, 10)

        userInputLAT.delete(0, END)
        userInputLAT.insert(0, str(latitude))

        appo_float = floatERR(longitudeLast)
        gradi = int(appo_float / 100)
        # print(gradi)
        dec = float(appo_float - gradi * 100)
        # print(dec)
        gra = dec * 100 / 60
        # print(gra)
        conversione = round(gradi + gra / 100, 10)
        # print(conversione)
        longitude = round(conversione, 10)

        userInputLONG.delete(0, END)
        userInputLONG.insert(0, str(longitude))


x = subprocess.getoutput("sudo python /home/pi/AirPlatform/killManager.py")
messagebox.showinfo(
    "Sensor Test ",
    "This program stops the sending data to the webserver \nTo restart sending data to the Webserver please reboot the Platform \n",
)
n0 = str(datetime.datetime.now())
data1 = n0[0:10]
f = open("/home/pi/AirPlatform/latitudeLast.txt", "r")
latitudeLast = f.read()
f.close()


f = open("/home/pi/AirPlatform/longitudeLast.txt", "r")
longitudeLast = f.read()
f.close()

root.geometry("950x520".format(10, 10))

root.wm_title("AQP sensors test ")  # Makes the title that will appear in the top left


root.protocol("WM_DELETE_WINDOW", closeWindow)  # root is your root window

# root.config(background="#FFFFFF")  # sets background color to white

myFont = tkFont.Font(family="Helvetica", size=36, weight="bold")
# Right Frame and its contents
rightFrame = tkinter.Frame(root, width=950, height=460)
rightFrame.grid(row=3, column=1, padx=10, pady=2)

btnFrame = tkinter.Frame(rightFrame, width=950, height=460)
btnFrame.grid(row=0, column=0, padx=10, pady=2)


firstLabel = tkinter.Label(btnFrame, text="AQP sensors test")
firstLabel.grid(row=0, column=0, padx=10, pady=2)


yellowBtn = tkinter.Button(btnFrame, text="Temp. & Hum. test ", command=temperatura)
yellowBtn.grid(row=1, column=0, padx=10, pady=2)

firstLabelT = tkinter.Label(btnFrame, text="Temperature")
firstLabelT.grid(row=1, column=1, padx=30, pady=2)

yellowBtnA = tkinter.Button(btnFrame, text="CO,NH3,NO2 Arduino test ", command=arduino)
yellowBtnA.grid(row=2, column=0, padx=10, pady=2)

firstLabelA = tkinter.Label(btnFrame, text="Arduino")
firstLabelA.grid(row=2, column=1, padx=30, pady=2)


yellowBtnP = tkinter.Button(btnFrame, text="PM test ", command=pm)
yellowBtnP.grid(row=6, column=0, padx=10, pady=2)

firstLabelP = tkinter.Label(btnFrame, text="PM")
firstLabelP.grid(row=6, column=1, padx=30, pady=2)

yellowBtnG = tkinter.Button(btnFrame, text="GPS test ", command=gps)
yellowBtnG.grid(row=7, column=0, padx=10, pady=2)

firstLabelG = tkinter.Label(btnFrame, text="GPS")
firstLabelG.grid(row=7, column=1, padx=30, pady=2)

yellowBtnL = tkinter.Button(btnFrame, text="LED ", command=led)
yellowBtnL.grid(row=8, column=0, padx=10, pady=2)

firstLabelL = tkinter.Label(btnFrame, text="led")
firstLabelL.grid(row=8, column=1, padx=30, pady=2)

yellowBtnI = tkinter.Button(btnFrame, text="Internet", command=internet)
yellowBtnI.grid(row=9, column=0, padx=10, pady=2)

firstLabelI = tkinter.Label(btnFrame, text="internet")
firstLabelI.grid(row=9, column=1, padx=30, pady=2)

yellowBtnI = tkinter.Button(btnFrame, text="Set AQP position", command=position)
yellowBtnI.grid(row=10, column=0, padx=10, pady=2)


firstLabelI = tkinter.Label(btnFrame, text="Latitude")
firstLabelI.grid(row=10, column=1, padx=30, pady=2)
firstLabelI = tkinter.Label(btnFrame, text="Longitude")
firstLabelI.grid(row=11, column=1, padx=30, pady=2)

userInputLAT = tkinter.Entry(
    btnFrame, width=12
)  # the width refers to the number of characters
userInputLAT.grid(row=10, column=2, padx=15, pady=2)


appo_float = floatERR(latitudeLast)
gradi = int(appo_float / 100)
# print(gradi)
dec = float(appo_float - gradi * 100)
# print(dec)
gra = dec * 100 / 60
# print(gra)
conversione = round(gradi + gra / 100, 10)
# print(conversione)
latitude = round(conversione, 10)


userInputLAT.insert(0, str(latitude))


userInputLONG = tkinter.Entry(
    btnFrame, width=12
)  # the width refers to the number of characters
userInputLONG.grid(row=11, column=2, padx=15, pady=2)


appo_float = floatERR(longitudeLast)
gradi = int(appo_float / 100)
# print(gradi)
dec = float(appo_float - gradi * 100)
# print(dec)
gra = dec * 100 / 60
# print(gra)
conversione = round(gradi + gra / 100, 10)
# print(conversione)
longitude = round(conversione, 10)


userInputLONG.insert(0, str(longitude))

yellowBtnI = tkinter.Button(btnFrame, text="Gps info", command=gps_info)
yellowBtnI.grid(row=12, column=0, padx=10, pady=2)

firstLabelI = tkinter.Label(btnFrame, text=" ")
firstLabelI.grid(row=12, column=1, padx=30, pady=2)


yellowBtnI = tkinter.Button(btnFrame, text="Sensors Error correction", command=calibra)
yellowBtnI.grid(row=13, column=0, padx=10, pady=2)

firstLabelI = tkinter.Label(btnFrame, text="Error correction")
firstLabelI.grid(row=13, column=1, padx=30, pady=2)


yellowBtnReb = tkinter.Button(btnFrame, text="AQP Reboot", command=reboot)
yellowBtnReb.grid(row=14, column=0, padx=10, pady=2)

firstLabelReb = tkinter.Label(btnFrame, text=" ")
firstLabelReb.grid(row=14, column=1, padx=30, pady=2)
root.mainloop()
