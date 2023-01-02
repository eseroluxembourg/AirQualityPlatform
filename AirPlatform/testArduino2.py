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


# info = commands.getoutput('dmesg | grep "usb 1-1.3: ch341-uart"')
# print (info)
# if info.find("usb 1-1.3: ch341-uart converter now attached")> -1 :
# posizioneporta = "/dev/" + info[-7:]
# posizioneporta = "/dev/ttyUSB0"
# print(posizioneporta)
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
for conta in range(1, 15):

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
tenCO = CO
# print(CO)
f = open("/home/pi/AirPlatform/V0CO.txt", "r")
stringa = f.read()
VM0 = floatERR(stringa)
f.close()

# VM0=1.78
VM1 = CO
r0 = VM0 * 10000 / (Vcc - VM0)
# print(r0)
rs = VM1 * 10000 / (Vcc - VM1)
# print(rs)

rs_r0 = rs / r0
# rs_r0=1
# print(rs_r0)
if rs != 0:
    x = math.log10(rs_r0)
    y = 10 ** (
        (x - math.log10(3))
        / (math.log10(0.01) - math.log10(3))
        * (math.log10(1000) - math.log10(1))
    )
    CO = y
    # print (y)
    # print(CO)
    # correzione
    f = open("/home/pi/AirPlatform/OffsetCO.txt", "r")
    stringa = f.read()
    offset = floatERR(stringa)
    f.close()

    f = open("/home/pi/AirPlatform/AmplCO.txt", "r")
    stringa = f.read()
    Amplificazione = floatERR(stringa)
    f.close()
    CO = CO * Amplificazione + offset
    # print(CO)
else:
    CO = 0


# NH3
appo_dato = float(sensori[1])
# print(appo_dato)
NH3 = float(appo_dato * Vcc / 1024)
tenNH3 = NH3
# print(NH3)


f = open("/home/pi/AirPlatform/V0NH3.txt", "r")
stringa = f.read()
VM0 = floatERR(stringa)
f.close()

# VM0=1.2646484375

VM1 = NH3
r0 = VM0 * 10000 / (Vcc - VM0)
# print(r0)
rs = VM1 * 10000 / (Vcc - VM1)
# print(rs)

rs_r0 = rs / r0
if rs != 0:
    x = math.log10(rs_r0)

    y = 10 ** (
        (x - math.log10(0.8))
        / (math.log10(0.05) - math.log10(0.8))
        * (math.log10(150) - math.log10(1))
        + math.log10(1)
    )
    # print (y)
    NH3 = y
    # correzione NH3
    f = open("/home/pi/AirPlatform/OffsetNH3.txt", "r")
    stringa = f.read()
    offset = floatERR(stringa)
    f.close()

    f = open("/home/pi/AirPlatform/AmplNH3.txt", "r")
    stringa = f.read()
    Amplificazione = floatERR(stringa)
    f.close()
    NH3 = NH3 * Amplificazione + offset
else:
    NH3 = 0
# print(CO)


appo_dato = float(sensori[2])
# print(appo_dato)
NO2 = float(appo_dato * 5 / 1024)
tenNO2 = NO2
# print(NO2)
f = open("/home/pi/AirPlatform/V0NO2.txt", "r")
stringa = f.read()
VM0 = floatERR(stringa)
f.close()

# VM0=4.4775

VM1 = NO2
r0 = VM0 * 1000 / (Vcc - VM0)
# print(r0)
rs = VM1 * 1000 / (Vcc - VM1)
# print(rs)

rs_r0 = rs / r0
# print(rs_r0)
if rs != 0:
    x = math.log10(rs_r0)
    y = 10 ** (
        (x - math.log10(0.06))
        / (math.log10(40) - math.log10(0.06))
        * (math.log10(6) - math.log10(0.01))
        + math.log10(0.01)
    )
    # print(y)
    NO2 = y
    # correzione NO2
    f = open("/home/pi/AirPlatform/OffsetNO2.txt", "r")
    stringa = f.read()
    offset = floatERR(stringa)
    f.close()

    f = open("/home/pi/AirPlatform/AmplNO2.txt", "r")
    stringa = f.read()
    Amplificazione = floatERR(stringa)
    f.close()
    NO2 = NO2 * Amplificazione + offset
else:
    NO2 = 0
# print(CO)


appo_dato = float(sensori[3])
# print(appo_dato)
CO2 = float(appo_dato * 5 / 1024)
tenCO2 = CO2
# valore letto in mv da Arduino
# print(CO2)
f = open("/home/pi/AirPlatform/V0CO2.txt", "r")
stringa = f.read()
VM0 = floatERR(stringa)
f.close()

f = open("/home/pi/AirPlatform/DECO2.txt", "r")
stringa = f.read()
DECO2 = floatERR(stringa)
f.close()

# CO2= (CO2-(VM0-0.2))/0.2*(325-265)+265

CO2 = (CO2 - (VM0 - DECO2)) / DECO2 * (325 - 265) + 265
# print(CO2)
# CO2=265+((CO2-0.2)/0.4)*60
# valore mVolt arduino al range 265mv a 325mv del grafico chinese
# Basandosi su - sensor in clean air (typically 400ppm CO2)
# all'aria aperta lo calibro a 400ppm con relativo valore lettura arduino rapportato a 350mv
# Cioe' ad aria pulita il valore di arduino e' convertio a 350mv
# Per il massimo ..... ipotzzo il delta max fornito dal datasheet
# moltiplicato per il fattore moltiplicativo scheda esterna.
# sembra che calza
# print(CO2)print(CO2)
# CO2= 325
CO2 = float(10 ** ((4 - ((CO2 - 265) / 60) * (4 - math.log10(400)))))
# conversione  ppm da grafico datasheet

# correzione
f = open("/home/pi/AirPlatform/OffsetCO2.txt", "r")
stringa = f.read()
offset = floatERR(stringa)
f.close()

f = open("/home/pi/AirPlatform/AmplCO2.txt", "r")
stringa = f.read()
Amplificazione = floatERR(stringa)
f.close()
CO2 = CO2 * Amplificazione + offset

appo_stringa = "CO=" + str(CO) + "ppm ,"

appo_stringa = appo_stringa + "NH3=" + str(NH3) + "ppm ,"
appo_stringa = appo_stringa + "NO2=" + str(NO2) + "ppm ,"
appo_stringa = appo_stringa + "CO2=" + str(CO2) + "ppm"
print(appo_stringa)


# tensione letta nel momento dei sensori salvata su file

appo_stringa = appo_stringa + "VOLT: CO=" + str(tenCO) + "V ,"

appo_stringa = appo_stringa + "NH3=" + str(tenNH3) + "V ,"
appo_stringa = appo_stringa + "NO2=" + str(tenNO2) + "V ,"
appo_stringa = appo_stringa + "CO2=" + str(tenCO2) + "V"

f = open("/home/pi/AirPlatform/tensione.txt", "w")
f.write(appo_stringa)
# print(appo_stringa)
f.close()
