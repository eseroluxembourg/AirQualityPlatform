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


def reboot():
    risposta = messagebox.askyesno("Yes|No", "Do you want to reboot the AQP?")

    if risposta == True:
        x = subprocess.getoutput("sudo reboot -h now")
        # print(x)


def temp():
    offset = floatERR(userInputTempoffs.get())

    f = open("/home/pi/AirPlatform/OffsetTemp.txt", "w")
    f.write(str(offset))
    f.close()
    userInputTempoffs.delete(0, END)
    userInputTempoffs.insert(0, str(offset))

    Amplificazione = floatERR(userInputTempAmpl.get())

    f = open("/home/pi/AirPlatform/AmplTemp.txt", "w")
    f.write(str(Amplificazione))
    f.close()
    userInputTempAmpl.delete(0, END)
    userInputTempAmpl.insert(0, str(Amplificazione))


def hum():
    offset = floatERR(userInputHumoffs.get())

    f = open("/home/pi/AirPlatform/OffsetHum.txt", "w")
    f.write(str(offset))
    f.close()
    userInputHumoffs.delete(0, END)
    userInputHumoffs.insert(0, str(offset))

    Amplificazione = floatERR(userInputHumAmpl.get())

    f = open("/home/pi/AirPlatform/AmplHum.txt", "w")
    f.write(str(Amplificazione))
    f.close()
    userInputHumAmpl.delete(0, END)
    userInputHumAmpl.insert(0, str(Amplificazione))


def pm25():
    offset = floatERR(userInputPM25offs.get())

    f = open("/home/pi/AirPlatform/OffsetPM25.txt", "w")
    f.write(str(offset))
    f.close()
    userInputPM25offs.delete(0, END)
    userInputPM25offs.insert(0, str(offset))

    Amplificazione = floatERR(userInputPM25Ampl.get())

    f = open("/home/pi/AirPlatform/AmplPM25.txt", "w")
    f.write(str(Amplificazione))
    f.close()
    userInputPM25Ampl.delete(0, END)
    userInputPM25Ampl.insert(0, str(Amplificazione))


def pm10():
    offset = floatERR(userInputPM10offs.get())

    f = open("/home/pi/AirPlatform/OffsetPM10.txt", "w")
    f.write(str(offset))
    f.close()
    userInputPM10offs.delete(0, END)
    userInputPM10offs.insert(0, str(offset))

    Amplificazione = floatERR(userInputPM10Ampl.get())

    f = open("/home/pi/AirPlatform/AmplPM10.txt", "w")
    f.write(str(Amplificazione))
    f.close()
    userInputPM10Ampl.delete(0, END)
    userInputPM10Ampl.insert(0, str(Amplificazione))


def co():
    offset = floatERR(userInputCOoffs.get())

    f = open("/home/pi/AirPlatform/OffsetCO.txt", "w")
    f.write(str(offset))
    f.close()
    userInputCOoffs.delete(0, END)
    userInputCOoffs.insert(0, str(offset))

    Amplificazione = floatERR(userInputCOAmpl.get())

    f = open("/home/pi/AirPlatform/AmplCO.txt", "w")
    f.write(str(Amplificazione))
    f.close()
    userInputCOAmpl.delete(0, END)
    userInputCOAmpl.insert(0, str(Amplificazione))


def nh3():
    offset = floatERR(userInputNH3offs.get())

    f = open("/home/pi/AirPlatform/OffsetNH3.txt", "w")
    f.write(str(offset))
    f.close()
    userInputNH3offs.delete(0, END)
    userInputNH3offs.insert(0, str(offset))

    Amplificazione = floatERR(userInputNH3Ampl.get())

    f = open("/home/pi/AirPlatform/AmplNH3.txt", "w")
    f.write(str(Amplificazione))
    f.close()
    userInputNH3Ampl.delete(0, END)
    userInputNH3Ampl.insert(0, str(Amplificazione))


def no2():
    offset = floatERR(userInputNO2offs.get())

    f = open("/home/pi/AirPlatform/OffsetNO2.txt", "w")
    f.write(str(offset))
    f.close()
    userInputNO2offs.delete(0, END)
    userInputNO2offs.insert(0, str(offset))

    Amplificazione = floatERR(userInputNO2Ampl.get())

    f = open("/home/pi/AirPlatform/AmplNO2.txt", "w")
    f.write(str(Amplificazione))
    f.close()
    userInputNO2Ampl.delete(0, END)
    userInputNO2Ampl.insert(0, str(Amplificazione))


def co2():
    offset = floatERR(userInputCO2offs.get())

    f = open("/home/pi/AirPlatform/OffsetCO2.txt", "w")
    f.write(str(offset))
    f.close()
    userInputCO2offs.delete(0, END)
    userInputCO2offs.insert(0, str(offset))

    Amplificazione = floatERR(userInputCO2Ampl.get())

    f = open("/home/pi/AirPlatform/AmplCO2.txt", "w")
    f.write(str(Amplificazione))
    f.close()
    userInputCO2Ampl.delete(0, END)
    userInputCO2Ampl.insert(0, str(Amplificazione))


def deco():
    offset = floatERR(userInputDECO2.get())

    f = open("/home/pi/AirPlatform/DECO2.txt", "w")
    f.write(str(offset))
    f.close()
    userInputDECO2.delete(0, END)
    userInputDECO2.insert(0, str(offset))


def gps():
    a = a


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

root.geometry("850x400".format(10, 10))

root.wm_title(
    "AQP Sensors Error Correction  "
)  # Makes the title that will appear in the top left


root.protocol("WM_DELETE_WINDOW", closeWindow)  # root is your root window

# root.config(background="#FFFFFF")  # sets background color to white

myFont = tkFont.Font(family="Helvetica", size=36, weight="bold")
# Right Frame and its contents
rightFrame = tkinter.Frame(root, width=850, height=400)
rightFrame.grid(row=3, column=1, padx=10, pady=2)

btnFrame = tkinter.Frame(rightFrame, width=850, height=400)
btnFrame.grid(row=0, column=0, padx=10, pady=2)


firstLabel = tkinter.Label(btnFrame, text="AQP Sensors Error Correction")
firstLabel.grid(row=0, column=0, padx=10, pady=2)


riga = 1
firstLabelT = tkinter.Label(btnFrame, text="Temperature Offset")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)

userInputTempoffs = tkinter.Entry(btnFrame, width=12)
userInputTempoffs.grid(row=riga, column=1, padx=12, pady=2)

f = open("/home/pi/AirPlatform/OffsetTemp.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()
userInputTempoffs.insert(0, str(offset))


firstLabelT = tkinter.Label(btnFrame, text="Amplitude")
firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

userInputTempAmpl = tkinter.Entry(btnFrame, width=12)
userInputTempAmpl.grid(row=riga, column=3, padx=12, pady=2)

f = open("/home/pi/AirPlatform/AmplTemp.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
userInputTempAmpl.insert(0, str(Amplificazione))

yellowBtnP = tkinter.Button(btnFrame, text="Set Values ", command=temp)
yellowBtnP.grid(row=riga, column=4, padx=10, pady=2)

riga = riga + 1


firstLabelT = tkinter.Label(btnFrame, text="Humidity Offset")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)

userInputHumoffs = tkinter.Entry(btnFrame, width=12)
userInputHumoffs.grid(row=riga, column=1, padx=12, pady=2)

f = open("/home/pi/AirPlatform/OffsetHum.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()
userInputHumoffs.insert(0, str(offset))

firstLabelT = tkinter.Label(btnFrame, text="Amplitude")
firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

userInputHumAmpl = tkinter.Entry(btnFrame, width=12)
userInputHumAmpl.grid(row=riga, column=3, padx=12, pady=2)

f = open("/home/pi/AirPlatform/AmplHum.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
userInputHumAmpl.insert(0, str(Amplificazione))


yellowBtnP = tkinter.Button(btnFrame, text="Set Values ", command=hum)
yellowBtnP.grid(row=riga, column=4, padx=10, pady=2)

riga = riga + 1


firstLabelT = tkinter.Label(btnFrame, text="PM2.5 Offset")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)

userInputPM25offs = tkinter.Entry(btnFrame, width=12)
userInputPM25offs.grid(row=riga, column=1, padx=12, pady=2)

f = open("/home/pi/AirPlatform/OffsetPM25.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()
userInputPM25offs.insert(0, str(offset))


firstLabelT = tkinter.Label(btnFrame, text="Amplitude")
firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

userInputPM25Ampl = tkinter.Entry(btnFrame, width=12)
userInputPM25Ampl.grid(row=riga, column=3, padx=12, pady=2)


f = open("/home/pi/AirPlatform/AmplPM25.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
userInputPM25Ampl.insert(0, str(Amplificazione))


yellowBtnP = tkinter.Button(btnFrame, text="Set Values ", command=pm25)
yellowBtnP.grid(row=riga, column=4, padx=10, pady=2)

riga = riga + 1


firstLabelT = tkinter.Label(btnFrame, text="PM10 Offset")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)

userInputPM10offs = tkinter.Entry(btnFrame, width=12)
userInputPM10offs.grid(row=riga, column=1, padx=12, pady=2)

f = open("/home/pi/AirPlatform/OffsetPM10.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()
userInputPM10offs.insert(0, str(offset))

firstLabelT = tkinter.Label(btnFrame, text="Amplitude")
firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

userInputPM10Ampl = tkinter.Entry(btnFrame, width=12)
userInputPM10Ampl.grid(row=riga, column=3, padx=12, pady=2)

f = open("/home/pi/AirPlatform/AmplPM10.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
userInputPM10Ampl.insert(0, str(Amplificazione))

yellowBtnP = tkinter.Button(btnFrame, text="Set Values ", command=pm10)
yellowBtnP.grid(row=riga, column=4, padx=10, pady=2)


riga = riga + 1


firstLabelT = tkinter.Label(btnFrame, text="CO Offset")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)


userInputCOoffs = tkinter.Entry(btnFrame, width=12)
userInputCOoffs.grid(row=riga, column=1, padx=12, pady=2)

f = open("/home/pi/AirPlatform/OffsetCO.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()
userInputCOoffs.insert(0, str(offset))

firstLabelT = tkinter.Label(btnFrame, text="Amplitude")
firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

userInputCOAmpl = tkinter.Entry(btnFrame, width=12)
userInputCOAmpl.grid(row=riga, column=3, padx=12, pady=2)

f = open("/home/pi/AirPlatform/AmplCO.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
userInputCOAmpl.insert(0, str(Amplificazione))


yellowBtnP = tkinter.Button(btnFrame, text="Set Values ", command=co)
yellowBtnP.grid(row=riga, column=4, padx=10, pady=2)


riga = riga + 1


firstLabelT = tkinter.Label(btnFrame, text="NH3 Offset")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)

userInputNH3offs = tkinter.Entry(btnFrame, width=12)
userInputNH3offs.grid(row=riga, column=1, padx=12, pady=2)

f = open("/home/pi/AirPlatform/OffsetNH3.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()
userInputNH3offs.insert(0, str(offset))

firstLabelT = tkinter.Label(btnFrame, text="Amplitude")
firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

userInputNH3Ampl = tkinter.Entry(btnFrame, width=12)
userInputNH3Ampl.grid(row=riga, column=3, padx=12, pady=2)

f = open("/home/pi/AirPlatform/AmplNH3.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
userInputNH3Ampl.insert(0, str(Amplificazione))

yellowBtnP = tkinter.Button(btnFrame, text="Set Values ", command=nh3)
yellowBtnP.grid(row=riga, column=4, padx=10, pady=2)

riga = riga + 1


firstLabelT = tkinter.Label(btnFrame, text="NO2 Offset")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)

userInputNO2offs = tkinter.Entry(btnFrame, width=12)
userInputNO2offs.grid(row=riga, column=1, padx=12, pady=2)

f = open("/home/pi/AirPlatform/OffsetNO2.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()
userInputNO2offs.insert(0, str(offset))

firstLabelT = tkinter.Label(btnFrame, text="Amplitude")
firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

userInputNO2Ampl = tkinter.Entry(btnFrame, width=12)
userInputNO2Ampl.grid(row=riga, column=3, padx=12, pady=2)

f = open("/home/pi/AirPlatform/AmplNO2.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
userInputNO2Ampl.insert(0, str(Amplificazione))

yellowBtnP = tkinter.Button(btnFrame, text="Set Values ", command=no2)
yellowBtnP.grid(row=riga, column=4, padx=10, pady=2)

riga = riga + 1


firstLabelT = tkinter.Label(btnFrame, text="CO2 Offset")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)

userInputCO2offs = tkinter.Entry(btnFrame, width=12)
userInputCO2offs.grid(row=riga, column=1, padx=12, pady=2)


f = open("/home/pi/AirPlatform/OffsetCO2.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()
userInputCO2offs.insert(0, str(offset))


firstLabelT = tkinter.Label(btnFrame, text="Amplitude")
firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

userInputCO2Ampl = tkinter.Entry(btnFrame, width=12)
userInputCO2Ampl.grid(row=riga, column=3, padx=12, pady=2)

f = open("/home/pi/AirPlatform/AmplCO2.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
userInputCO2Ampl.insert(0, str(Amplificazione))

yellowBtnP = tkinter.Button(btnFrame, text="Set Values ", command=co2)
yellowBtnP.grid(row=riga, column=4, padx=10, pady=2)

riga = riga + 1


firstLabelT = tkinter.Label(btnFrame, text="CO2 Ampl. Parameter")
firstLabelT.grid(row=riga, column=0, padx=30, pady=2)

userInputDECO2 = tkinter.Entry(btnFrame, width=12)
userInputDECO2.grid(row=riga, column=1, padx=12, pady=2)
f = open("/home/pi/AirPlatform/DECO2.txt", "r")
stringa = f.read()
DECO2 = floatERR(stringa)
f.close()
userInputDECO2.insert(0, str(DECO2))
# firstLabelT = tkinter.Label(btnFrame, text="")
# firstLabelT.grid(row=riga, column=2, padx=30, pady=2)

# userInputTAmpl = tkinter.Entry(btnFrame, width=12)
# userInputTAmpl.grid(row=riga, column=3, padx=12, pady=2)

yellowBtnP = tkinter.Button(btnFrame, text="Set Value ", command=deco)
yellowBtnP.grid(row=riga, column=2, padx=10, pady=2)

riga = riga + 1

yellowBtnReb = tkinter.Button(btnFrame, text="AQP Reboot", command=reboot)
yellowBtnReb.grid(row=riga, column=0, padx=10, pady=2)
root.mainloop()
