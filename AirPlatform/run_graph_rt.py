#!/usr/bin/python
import datetime
import os
import subprocess
import tkinter
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import pandas as pd

stringa_finale = ""

root = tkinter.Tk()  # Makes the window


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


def RT():

    plt.ion()

    fig = plt.figure()
    fig.canvas.set_window_title("AQP RT Sensor values")

    # print(box_value.get())
    scelta = box_value.get()
    if scelta == "humidity":
        indice = 2
    if scelta == "temperature":
        indice = 1
    if scelta == "pm10":
        indice = 3

    if scelta == "pm2.5":
        indice = 4
    if scelta == "co2":
        indice = 5
    if scelta == "co":
        indice = 6
    if scelta == "nh3":
        indice = 7
    if scelta == "no2":
        indice = 8

    i = 0
    x_step = 0
    x = list()
    y = list()

    # plt.yscale('log')
    plt.xlabel("Time")

    # giorno="2020-10-07"
    # ora="17:47:00"
    # data_grafico = datetime.datetime.strptime(giorno + ' ' + ora, "%Y-%m-%d %H:%M:%S")
    # plt.grid(True)
    plt.gcf().autofmt_xdate()

    while i < 100:
        if indice == 1:
            if i == 0:
                nome_grafico = "Temperature"
                unita_misura = "°C"
                plt.title(nome_grafico)
                plt.ylabel(unita_misura)
                ymax = 35
                plt.axis([0, 100, 0, ymax])

            # temp_y=np.random.random();
            x = subprocess.getoutput(
                "sudo python3 /home/pi/AirPlatform/testTemperatura2.py"
            )
            # print(x)

            if (x.find("Temperature=") != -1) & (x.find("Humidity=") != -1):
                posizione = x.find("Temperature=")
                posizione2 = x.find("*C")
                valoreSensore = x[posizione + 12 : posizione2]
                valore = floatERR(valoreSensore)
                temperature = valore
                # print("Temperature " + str(valore))
                # Humidity=40.1%
                posizione = x.find("Humidity=")
                posizione2 = x.find("%")
                valoreSensore = x[posizione + 9 : posizione2]
                valore = floatERR(valoreSensore)
                umidita = valore
                # print("Humidity " + str(umidita))
            else:
                umidita = None
                temperature = None

            # temp_y=math.sin(x_step)
            temp_y = temperature

        if indice == 2:
            if i == 0:
                nome_grafico = "Humidity"
                unita_misura = "%"
                plt.title(nome_grafico)
                plt.ylabel(unita_misura)
                ymax = 100
                plt.axis([0, 100, 0, ymax])
            # temp_y=np.random.random();

            #
            plt.ylabel(unita_misura)
            x = subprocess.getoutput(
                "sudo python3 /home/pi/AirPlatform/testTemperatura2.py"
            )
            # print(x)

            if (x.find("Temperature=") != -1) & (x.find("Humidity=") != -1):
                posizione = x.find("Temperature=")
                posizione2 = x.find("*C")
                valoreSensore = x[posizione + 12 : posizione2]
                valore = floatERR(valoreSensore)
                temperature = valore
                # print("Temperature " + str(valore))
                # Humidity=40.1%
                posizione = x.find("Humidity=")
                posizione2 = x.find("%")
                valoreSensore = x[posizione + 9 : posizione2]
                valore = floatERR(valoreSensore)
                umidita = valore
                # print("Humidity " + str(umidita))
            else:
                umidita = None
                temperature = None

            # temp_y=math.sin(x_step)
            temp_y = umidita

        if indice == 3:
            if i == 0:
                nome_grafico = "PM10"
                unita_misura = "ppm"
                plt.title(nome_grafico)
                plt.ylabel(unita_misura)
                ymax = 35
                plt.axis([0, 100, 0, ymax])
            x = subprocess.getoutput("sudo python /home/pi/AirPlatform/aqiMax.py")

            if (x.find("PM2.5:") != -1) & (x.find("PM10:") != -1):

                posizione = x.find("PM2.5:")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 6 : posizione2]
                valore = floatERR(valoreSensore)
                PM25 = valore
                # print ("PM2.5 " + str(PM25))
                x = x[posizione2 + 3 :]

                posizione = x.find("PM10:")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 5 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                PM10 = valore
                # print ("PM10 " + str(PM10))
            else:
                PM10 = None
                PM25 = None
            temp_y = PM10

        if indice == 4:
            if i == 0:
                nome_grafico = "PM2.5"
                unita_misura = "ppm"
                plt.title(nome_grafico)
                plt.ylabel(unita_misura)
                ymax = 35
                plt.axis([0, 100, 0, ymax])

            x = subprocess.getoutput("sudo python /home/pi/AirPlatform/aqiMax.py")
            # print(x)

            nome_grafico = "PM2.5"
            unita_misura = "ppm"
            plt.title(nome_grafico)
            #
            plt.ylabel(unita_misura)

            if (x.find("PM2.5:") != -1) & (x.find("PM10:") != -1):

                posizione = x.find("PM2.5:")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 6 : posizione2]
                valore = floatERR(valoreSensore)
                PM25 = valore
                # print ("PM2.5 " + str(PM25))
                x = x[posizione2 + 3 :]

                posizione = x.find("PM10:")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 5 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                PM10 = valore
                # print ("PM10 " + str(PM10))
            else:
                PM10 = None
                PM25 = None
            temp_y = PM25

        if indice == 5:
            # temp_y=0

            if i == 0:

                nome_grafico = "CO2"
                unita_misura = "ppm"
                plt.title(nome_grafico)
                plt.ylabel(unita_misura)
                ymax = 500
                plt.axis([0, 100, 0, ymax])

            x = subprocess.getoutput("sudo python /home/pi/AirPlatform/testArduino2.py")
            # print (x)
            # CO2=None
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
                # print ("CO " + str(CO))
                x = x[posizione2 + 3 :]

                posizione = x.find("NH3=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                NH3 = valore
                # print ("NH3 " + str(NH3))
                x = x[posizione2 + 3 :]

                posizione = x.find("NO2=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                NO2 = valore
                # print ("NO2 " + str(NO2))
                x = x[posizione2 + 3 :]

                posizione = x.find("CO2=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                CO2 = valore
                # print ("CO2 " + str(CO2))

                posizione = x.find("Lum=")
                posizione2 = x.find("lx ")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                Luce = valore
                # print ("Lum " + str(Luce))

            else:
                CO2 = None
                NO2 = None
                NH3 = None
                CO = None
                Luce = None

            temp_y = CO2

        if indice == 6:
            # temp_y=0
            if i == 0:

                nome_grafico = "CO"
                unita_misura = "ppm"
                plt.title(nome_grafico)
                plt.ylabel(unita_misura)
                ymax = 10
                plt.axis([0, 100, 0, ymax])
            x = subprocess.getoutput("sudo python /home/pi/AirPlatform/testArduino2.py")
            # print (x)
            # CO2=None
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
                # print ("CO " + str(CO))
                x = x[posizione2 + 3 :]

                posizione = x.find("NH3=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                NH3 = valore
                # print ("NH3 " + str(NH3))
                x = x[posizione2 + 3 :]

                posizione = x.find("NO2=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                NO2 = valore
                # print ("NO2 " + str(NO2))
                x = x[posizione2 + 3 :]

                posizione = x.find("CO2=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                CO2 = valore
                # print ("CO2 " + str(CO2))

                posizione = x.find("Lum=")
                posizione2 = x.find("lx ")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                Luce = valore
                # print ("Lum " + str(Luce))

            else:
                CO2 = None
                NO2 = None
                NH3 = None
                CO = None
                Luce = None

            temp_y = CO

        if indice == 7:
            # temp_y=0
            if i == 0:

                nome_grafico = "NH3"
                unita_misura = "ppm"
                plt.title(nome_grafico)
                plt.ylabel(unita_misura)
                ymax = 3
                plt.axis([0, 100, 0, ymax])
                #

            x = subprocess.getoutput("sudo python /home/pi/AirPlatform/testArduino2.py")
            # print (x)
            # CO2=None
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
                # print ("CO " + str(CO))
                x = x[posizione2 + 3 :]

                posizione = x.find("NH3=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                NH3 = valore
                # print ("NH3 " + str(NH3))
                x = x[posizione2 + 3 :]

                posizione = x.find("NO2=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                NO2 = valore
                # print ("NO2 " + str(NO2))
                x = x[posizione2 + 3 :]

                posizione = x.find("CO2=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                CO2 = valore
                # print ("CO2 " + str(CO2))

                posizione = x.find("Lum=")
                posizione2 = x.find("lx ")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                Luce = valore
                # print ("Lum " + str(Luce))

            else:
                CO2 = None
                NO2 = None
                NH3 = None
                CO = None
                Luce = None

            temp_y = NH3

        if indice == 8:
            # temp_y=0

            if i == 0:

                nome_grafico = "NO2"
                unita_misura = "ppm"
                plt.title(nome_grafico)
                plt.ylabel(unita_misura)
                ymax = 4
                plt.axis([0, 100, 0, ymax])

            x = subprocess.getoutput("sudo python /home/pi/AirPlatform/testArduino2.py")
            # print (x)
            # CO2=None
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
                # print ("CO " + str(CO))
                x = x[posizione2 + 3 :]

                posizione = x.find("NH3=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                NH3 = valore
                # print ("NH3 " + str(NH3))
                x = x[posizione2 + 3 :]

                posizione = x.find("NO2=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                NO2 = valore
                # print ("NO2 " + str(NO2))
                x = x[posizione2 + 3 :]

                posizione = x.find("CO2=")
                posizione2 = x.find("ppm")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                CO2 = valore
                # print ("CO2 " + str(CO2))

                posizione = x.find("Lum=")
                posizione2 = x.find("lx ")
                valoreSensore = x[posizione + 4 : posizione2]
                # print(valoreSensore)
                valore = floatERR(valoreSensore)
                Luce = valore
                # print ("Lum " + str(Luce))

            else:
                CO2 = None
                NO2 = None
                NH3 = None
                CO = None
                Luce = None

            temp_y = NO2
        # x.append(i);
        # x.append(data_grafico);
        # y.append(temp_y);
        # plt.scatter(i,temp_y,marker = "o", color = 'red');
        if temp_y != None:
            if temp_y > ymax:
                ymax = temp_y + 10
                plt.axis([0, 100, 0, ymax])
            plt.scatter(i, temp_y, marker="o", color="red")
            x_step = x_step + 0.2
            i += 1
            stringa_finale = str(i) + ") " + str(temp_y) + " " + str(unita_misura)
            # nome_grafico="Temperature"
            plt.xlabel("Time     - sample " + stringa_finale)
            # plt.title(stringa_finale)

            # print(stringa_finale)

            userInputID.delete(0, END)

            userInputID.insert(0, stringa_finale)
            plt.show()
            plt.pause(0.1)
        else:
            userInputID.insert(0, "None data")


x = subprocess.getoutput("sudo python /home/pi/AirPlatform/killManager.py")

messagebox.showinfo(
    "RT graph ",
    "This program stops the sending data to the webserver \nTo restart sending data to the Webserver please reboot the Platform \n",
)

# print(x)
n0 = str(datetime.datetime.now())
data1 = n0[0:10]
root.geometry("345x160".format(20, 20))

root.wm_title(
    "AQP Download & Graph "
)  # Makes the title that will appear in the top left

root.config(background="#FFFFFF")  # sets background color to white


root.protocol("WM_DELETE_WINDOW", closeWindow)

myFont = tkFont.Font(family="Helvetica", size=36, weight="bold")
# Right Frame and its contents
rightFrame = tkinter.Frame(root, width=600, height=600)
rightFrame.grid(row=3, column=1, padx=10, pady=2)

btnFrame = tkinter.Frame(rightFrame, width=600, height=600)
btnFrame.grid(row=0, column=0, padx=10, pady=2)


firstLabel = tkinter.Label(btnFrame, text="AQP real time graph")
firstLabel.grid(row=0, column=0, padx=10, pady=2)

# PlatformId=read_file("PlatformID.txt")
yellowBtnReb = tkinter.Button(btnFrame, text="AQP Reboot", command=reboot)
yellowBtnReb.grid(row=4, column=0, padx=10, pady=2)


box_value = StringVar()
coltbox = ttk.Combobox(btnFrame, textvariable=box_value, state="readonly")
coltbox["values"] = [
    "pm2.5",
    "pm10",
    "temperature",
    "humidity",
    "co2",
    "co",
    "nh3",
    "no2",
]
coltbox.current(0)
coltbox.grid(row=1, column=0, padx=10, pady=2)

yellowBtn = tkinter.Button(
    btnFrame, text="       graph                         ", command=RT
)
yellowBtn.grid(row=2, column=0, padx=10, pady=2)

userInputID = tkinter.Entry(
    btnFrame, width=30
)  # the width refers to the number of characters
userInputID.grid(row=3, column=0, padx=30, pady=4)
userInputID.insert(3, "")

root.mainloop()
