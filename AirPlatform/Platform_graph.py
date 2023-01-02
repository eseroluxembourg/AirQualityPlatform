#!/usr/bin/python
import datetime
import os
import os.path
import random
import subprocess
import tkinter
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import pandas as pd

dfs = []
df = []
AQP = 1
nome_file = "/home/pi/AirPlatform/out.csv"


root = tkinter.Tk()

d = {
    "humidity": "%",
    "temperature": "°C",
    "pm10": "ppm",
    "pm25": "ppm",
    "co": "ppm",
    "co2": "ppm",
    "nh3": "ppm",
    "no2": "ppm",
    "latitude": "°",
    "gps_precision": " ",
    "longitude": "°",
    "sensor1": "lux",
    "sensor2": "#",
    "sensor3": "mbar",
    "sensor4": " ",
    "sensor5": "dB",
}


def controlla_lunghezza():

    userInputPK.delete(0, END)
    lung = os.path.getsize(nome_file)
    if lung < 20:
        tkinter.messagebox.showinfo(
            "WARNING", "No data from the AQP in the selected period"
        )
        userInputPK.insert(0, "NO DATA")
    else:

        df = pd.read_csv(nome_file)
        testo = str(df["acquisition_date"].size)
        userInputPK.insert(0, testo)

    return os.path.getsize(nome_file)


def read_file(nomeFile):
    file = open(nomeFile, "r")
    appo = file.readline()
    file.close()
    return appo


def download_today():
    if os.path.isfile(nome_file):
        os.remove(nome_file)
    dfs = []
    n0 = str(datetime.datetime.now())
    data1 = n0[0:10]
    AQP = userInputID.get()
    # pre = 'https://api.aqp.eo.esa.int/api/device/' + str(AQP)
    pre = "https://api.aqp.eo.esa.int/api/device/" + PlatformId
    post1 = "/csv?start_date=" + data1
    post2 = "&end_date=" + data1
    stringa = pre + post1 + post2
    dfs.append(pd.read_csv(stringa))
    big_frame = pd.concat(dfs, ignore_index=True)
    big_frame.to_csv(nome_file, index=False)

    controlla_lunghezza()


def download():
    dfs = []
    d1 = userInput1.get()

    d2 = userInput2.get()
    AQP = userInputID.get()
    # pre = 'https://api.aqp.eo.esa.int/api/device/' + str(AQP)
    pre = "https://api.aqp.eo.esa.int/api/device/" + PlatformId
    post1 = "/csv?start_date=" + d1
    post2 = "&end_date=" + d2
    stringa = pre + post1 + post2

    dfs.append(pd.read_csv(stringa))

    big_frame = pd.concat(dfs, ignore_index=True)
    big_frame.to_csv(nome_file, index=False)

    controlla_lunghezza()


def grafica():
    stringa = nome_file
    df = pd.read_csv(stringa)
    indice = box_value.get()

    if (df.size == 0) or (
        df[box_value.get()].size == df[box_value.get()].isnull().sum()
    ):
        tkinter.messagebox.showinfo("WARNING", "No data to visualize")
    else:
        if var1.get() == 1:

            fig = plt.figure()
            fig.canvas.set_window_title("AQP Download values")

        colore = "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])

        df["data time "] = pd.to_datetime(df["acquisition_date"])

        plt.title("AQP ")
        plt.xlabel("time")
        plt.ylabel(indice + " " + d.get(indice))

        plt.plot(
            df["data time "],
            df[box_value.get()],
            marker="o",
            label="AQP " + str(df[df.columns[1]][0]),
            color=colore,
        )

        plt.legend()
        plt.gcf().autofmt_xdate()

        plt.show()


n0 = str(datetime.datetime.now())
data1 = n0[0:10]
# root.geometry('370x180')
root.geometry("460x190")

root.wm_title(
    "AQP Download & Graph "
)  # Makes the title that will appear in the top left

root.config(background="#FFFFFF")  # sets background color to white

myFont = tkFont.Font(family="Helvetica", size=36, weight="bold")
# Right Frame and its contents
rightFrame = tkinter.Frame(root, width=600, height=600)
rightFrame.grid(row=3, column=1, padx=10, pady=2)

btnFrame = tkinter.Frame(rightFrame, width=600, height=600)
btnFrame.grid(row=0, column=0, padx=10, pady=2)


firstLabel = tkinter.Label(btnFrame, text="Air Platform ID")
firstLabel.grid(row=0, column=0, padx=10, pady=2)


PlatformId = read_file("/home/pi/AirPlatform/PlatformID.txt")

userInputID = tkinter.Entry(
    btnFrame, width=10
)  # the width refers to the number of characters
userInputID.grid(row=0, column=1, padx=10, pady=2)
userInputID.insert(0, PlatformId)


firstLabel1 = tkinter.Label(btnFrame, text="start date ")
firstLabel1.grid(row=1, column=1, padx=10, pady=2)


firstLabel = tkinter.Label(btnFrame, text="end date ")
firstLabel.grid(row=1, column=2, padx=10, pady=2)

yellowBtn = tkinter.Button(
    btnFrame, text="Download data               ", command=download
)
yellowBtn.grid(row=2, column=0, padx=10, pady=2)

userInput1 = tkinter.Entry(
    btnFrame, width=10
)  # the width refers to the number of characters
userInput1.grid(row=2, column=1, padx=10, pady=2)
userInput1.insert(0, data1)

userInput2 = tkinter.Entry(
    btnFrame, width=10
)  # the width refers to the number of characters
userInput2.grid(row=2, column=2, padx=10, pady=2)
userInput2.insert(0, data1)

yellowBtn = tkinter.Button(
    btnFrame, text="Download today data    ", command=download_today
)
yellowBtn.grid(row=4, column=0, padx=10, pady=2)

firstLabelPk = tkinter.Label(btnFrame, text="Packets :")
firstLabelPk.grid(row=4, column=1, padx=10, pady=2)

userInputPK = tkinter.Entry(
    btnFrame, width=10
)  # the width refers to the number of characters
userInputPK.grid(row=4, column=2, padx=10, pady=2)
userInputPK.insert(0, "0")


box_value = StringVar()
coltbox = ttk.Combobox(btnFrame, textvariable=box_value, state="readonly")
coltbox["values"] = [
    "temperature",
    "humidity",
    "co",
    "nh3",
    "no2",
    "co2",
    "latitude",
    "longitude",
    "gps_precision",
    "pm25",
    "pm10",
    "sensor1",
    "sensor2",
    "sensor3",
    "sensor4",
    "sensor5",
]
coltbox.current(0)
coltbox.grid(row=5, column=0, padx=10, pady=2)

var1 = IntVar()
Checkbutton(btnFrame, text="Multi-window", variable=var1).grid(
    row=5, column=1, sticky=W
)

yellowBtn = tkinter.Button(
    btnFrame, text="       graph                         ", command=grafica
)
yellowBtn.grid(row=6, column=0, padx=10, pady=2)

root.mainloop()
