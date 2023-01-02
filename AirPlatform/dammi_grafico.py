import os

import matplotlib
import numpy as np

matplotlib.use("Pdf")
import datetime

# import matplotlib.dates as mdates
import sys

import matplotlib.pyplot as plt

if len(sys.argv) == 2:
    n0 = str(datetime.datetime.now())
    data1 = n0[0:10]
    data2 = data1
    numero_sensore = sys.argv[1]
else:  #
    nome_script, numero_sensore, data1, data2 = sys.argv


def floatERR(stringa):
    ritorno = None
    try:
        ritorno = float(stringa)
    except:
        ritorno = None
    return ritorno


assex = []
assey = []
nome_file = "/home/pi/AirPlatform/log.txt"
f = open(nome_file, "r")  # riapriamo il file in lettura
lunghezza = os.path.getsize(nome_file)
# print(f.tell())
conta = 0

while f.tell() < lunghezza:

    appo_stringa = f.readline()  # leggiamo tutto il contenuto del file
    # print(appo_stringa)
    if len(appo_stringa) > 1:
        if appo_stringa[1] == "*":
            # print(appo_stringa)

            # identifica riga dati acquisiti

            giorno = appo_stringa[3:13]

            # print(giorno)
            ora = appo_stringa[14:22]
            # print(ora)

            if (giorno >= data1) & (giorno <= data2):
                # print(giorno)
                # print(ora)
                conta = conta + 1
                appo_stringa = appo_stringa[23:]
                # print (appo_stringa)
                posizione = appo_stringa.find("Temperature=")
                posizione2 = appo_stringa.find("*C")
                valoreSensore = appo_stringa[posizione + 12 : posizione2]
                valore = floatERR(valoreSensore)
                temperature = valore
                # print ("Temperature " + str(temperature))
                # Humidity=40.1%
                posizione = appo_stringa.find("Humidity=")
                posizione2 = appo_stringa.find("%")
                valoreSensore = appo_stringa[posizione + 9 : posizione2]
                valore = floatERR(valoreSensore)
                umidita = valore
                # print ("Humidity " + str(umidita))

                x = appo_stringa

                plt.grid(True)
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
                else:
                    CO2 = None
                    NO2 = None
                    NH3 = None
                    CO = None
                x = x[posizione2 + 1 :]
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

                x = x[posizione2 + 1 :]
                if (x.find("LAT=") != -1) & (x.find("LONG=") != -1):

                    posizione = x.find("LAT=")
                    posizione2 = x.find(",")
                    valoreSensore = x[posizione + 4 : posizione2]
                    valore = floatERR(valoreSensore)
                    LAT = valore
                    precedente_lat_grad = LAT
                    # print ("LAT " + str(LAT))
                    x = x[posizione2 + 2 :]

                    posizione = x.find("LONG=")
                    posizione2 = x.find(",")
                    valoreSensore = x[posizione + 5 : posizione2]
                    valore = floatERR(valoreSensore)
                    LONG = valore
                    precedente_long_grad = LONG
                    # print ("LONG " + str(LONG))

                    if x.find("Last Known Point") != -1:
                        GPS_precision = 0
                        LONG = precedente_long_grad
                        LAT = precedente_lat_grad
                    else:
                        GPS_precision = 1
                    # print ("GPS precision " + str(GPS_precision))
                else:
                    LONG = None
                    LAT = None
                    GPS_precision = 2

                x = x[x.find("VOLT:") + 5 :]
                # print(x)
                if (
                    (x.find("CO=") != -1)
                    & (x.find("NH3=") != -1)
                    & (x.find("NO2") != -1)
                    & (x.find("CO2=") != -1)
                ):
                    posizione = x.find("CO=")
                    posizione2 = x.find("V")
                    valoreSensore = x[posizione + 3 : posizione2]
                    valore = floatERR(valoreSensore)
                    VCO = valore
                    # print ("CO " + str(VCO))
                    x = x[posizione2 + 1 :]

                    posizione = x.find("NH3=")
                    posizione2 = x.find("V")
                    valoreSensore = x[posizione + 4 : posizione2]
                    # print(valoreSensore)
                    valore = floatERR(valoreSensore)
                    VNH3 = valore
                    # print ("NH3 " + str(VNH3))
                    x = x[posizione2 + 1 :]

                    posizione = x.find("NO2=")
                    posizione2 = x.find("V")
                    valoreSensore = x[posizione + 4 : posizione2]
                    # print(valoreSensore)
                    valore = floatERR(valoreSensore)
                    VNO2 = valore
                    # print ("NO2 " + str(VNO2))
                    x = x[posizione2 + 1 :]

                    posizione = x.find("CO2=")
                    posizione2 = x.find("V")
                    valoreSensore = x[posizione + 4 : posizione2]
                    # print(valoreSensore)
                    valore = floatERR(valoreSensore)
                    VCO2 = valore
                    # print ("CO2 " + str(VCO2))
                else:
                    VCO2 = None
                    VNO2 = None
                    VNH3 = None
                    VCO = None

                data_grafico = datetime.datetime.strptime(
                    giorno + " " + ora, "%Y-%m-%d %H:%M:%S"
                )
                # print(ora_time_stampa)

                assex.append(data_grafico)
                if numero_sensore == "1":
                    nome_grafico = "Temperature"
                    unita_misura = "*C"
                    # plt.yscale('log')
                    assey.append(temperature)
                if numero_sensore == "2":
                    nome_grafico = "Humidity"
                    unita_misura = "%"
                    # plt.yscale('log')
                    assey.append(umidita)
                if numero_sensore == "3":
                    nome_grafico = "CO"
                    unita_misura = "ppm"
                    # plt.yscale('log')
                    assey.append(CO)

                if numero_sensore == "4":
                    nome_grafico = "NH3"
                    unita_misura = "ppm"
                    # plt.yscale('log')
                    assey.append(NH3)

                if numero_sensore == "5":
                    nome_grafico = "NO2"
                    unita_misura = "ppm"
                    # plt.yscale('log')
                    assey.append(NO2)

                if numero_sensore == "6":
                    nome_grafico = "CO2"
                    unita_misura = "ppm"
                    # plt.yscale('log')
                    assey.append(CO2)

                if numero_sensore == "7":
                    nome_grafico = "PM10"
                    unita_misura = "ppm"
                    # plt.yscale('log')
                    assey.append(PM10)

                if numero_sensore == "8":
                    nome_grafico = "PM25"
                    unita_misura = "ppm"
                    # plt.yscale('log')
                    assey.append(PM25)

                if numero_sensore == "9":
                    nome_grafico = "Lat"
                    unita_misura = "Deg"
                    # plt.yscale('log')
                    assey.append(LAT)

                if numero_sensore == "10":
                    nome_grafico = "Long"
                    unita_misura = "Deg"
                    # plt.yscale('log')
                    assey.append(LONG)

                if numero_sensore == "11":
                    nome_grafico = "Voltage CO"
                    unita_misura = "V"
                    # plt.yscale('log')
                    assey.append(VCO)

                if numero_sensore == "12":
                    nome_grafico = "Voltage NH3"
                    unita_misura = "V"
                    # plt.yscale('log')
                    assey.append(VNH3)

                if numero_sensore == "13":
                    nome_grafico = "Voltage NO2"
                    unita_misura = "V"
                    # plt.yscale('log')
                    assey.append(VNO2)

                if numero_sensore == "14":
                    nome_grafico = "Voltage CO2"
                    unita_misura = "V"
                    # plt.yscale('log')
                    assey.append(VCO2)

# (x.find("CO=")!=-1) & (x.find("NH3=")!=-1) & (x.find("NO2")!=-1) & (x.find("CO2=")!=-1):
f.close()


# x = np.linspace(-(2*np.pi), 2*np.pi, 100)
# y = np.sin(x)
# myFmt = mdates.DateFormatter('%H:%M')
# plt.gca().xaxis.set_major_formatter(myFmt)

# dates = matplotlib.dates.date2num(assex)
# plt.plot_date(dates, assey)

plt.plot(assex, assey, marker="o", color="red")
plt.title(nome_grafico)
# plt.yscale('log')
plt.xlabel("Time")
plt.ylabel(unita_misura)
# plt.grid(True)
plt.gcf().autofmt_xdate()
# plt.show()
plt.savefig("/home/pi/AirPlatform/grafico.png")  # save the figure to file


plt.close()
