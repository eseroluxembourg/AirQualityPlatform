import math
import urllib

import commands
import serial

info = commands.getoutput('dmesg | grep "now attached to ttyUSB"')

posizioneporta = "/dev/ttyUSB0"


try:
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
    stringa = x

    x = ser.readline()
    stringa = stringa + x

    x = ser.readline()

    stringa = stringa + x

except:
    print("ERRORE USB0")
    stringa = ""

if stringa.find("Sensor") != -1:
    print(posizioneporta)
    f = open("PortaArduino.txt", "w")
    f.write("/dev/ttyUSB0")
    f.close()
    f = open("PortaParticolato.txt", "w")
    f.write("/dev/ttyUSB1")
    f.close()

else:

    posizioneporta = "/dev/ttyUSB1"

    try:
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
        stringa = x

        x = ser.readline()
        stringa = stringa + x

        x = ser.readline()

        stringa = stringa + x

    except:
        print("ERRORE USB1")
        stringa = ""
    if stringa.find("Sensor") != -1:
        print(posizioneporta)
        f = open("PortaArduino.txt", "w")
        f.write("/dev/ttyUSB1")
        f.close()
        f = open("PortaParticolato.txt", "w")
        f.write("/dev/ttyUSB0")
        f.close()
    else:
        print("ARDUINO NON TROVATO")
        f = open("PortaParticolato.txt", "w")
        f.write("/dev/ttyUSB0")
        f.close()
