import math
import time
import urllib

import commands
import serial


def floatERR(stringa):
    ritorno = None
    try:
        ritorno = float(stringa)
    except:
        ritorno = None
    return ritorno


f = open("/home/pi/AirPlatform/PortaArduino.txt", "r")
posizioneporta = f.read()
f.close()
# print(posizioneporta)

ser = serial.Serial(
    # port='/dev/ttyUSB0',
    port=posizioneporta,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)
x = ser.readline()
x = ser.readline()
x = ser.readline()
numeroSensoriTrovati = 0
sensori = [-1, -1, -1, -1]
for conta in range(1, 10):

    x = ser.readline()
    # print(x)
    if x.find("Sensor") != -1:
        # print("trovato " + x)
        posizione = x.find("=")
        numero = int(x[posizione - 2])
        # print(numero)
        valoreSensore = x[posizione + 1 : len(x) - 2]
        valore = int(valoreSensore)
        # print( numero, valore)
        if sensori[numero] == -1:
            sensori[numero] = valore
            # print(numero,valore)
            numeroSensoriTrovati = numeroSensoriTrovati + 1
            if numeroSensoriTrovati >= 4:

                break
# print(sensori)
Vcc = 5
# *************************
# legge di conversione
# *************************
appo_dato = float(sensori[0])
# print(appo_dato)
CO = float(appo_dato * Vcc / 1024)
# print(CO)


# NH3
appo_dato = float(sensori[1])
# print(appo_dato)
NH3 = float(appo_dato * Vcc / 1024)
# print(NH3)


appo_dato = float(sensori[2])
# print(appo_dato)
NO2 = float(appo_dato * Vcc / 1024)
# print(NO2)


appo_dato = float(sensori[3])
# print(appo_dato)
CO2 = float(appo_dato * Vcc / 1024)
# valore letto in mv da Arduino
# print(CO2)


appo_stringa = "CO=" + str(CO) + "V ,"


appo_stringa = appo_stringa + "NH3=" + str(NH3) + "V ,"
appo_stringa = appo_stringa + "NO2=" + str(NO2) + "V ,"
appo_stringa = appo_stringa + "CO2=" + str(CO2) + "V"
print(appo_stringa)

f = open("/home/pi/AirPlatform/V0CO.txt", "w")
f.write(str(CO))
f.close()


f = open("/home/pi/AirPlatform/V0NH3.txt", "w")
f.write(str(NH3))
f.close()


f = open("/home/pi/AirPlatform/V0NO2.txt", "w")
f.write(str(NO2))
f.close()


f = open("/home/pi/AirPlatform/V0CO2.txt", "w")
f.write(str(CO2))
f.close()
