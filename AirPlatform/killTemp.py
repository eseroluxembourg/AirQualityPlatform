import time
import urllib

import commands
import serial

info = commands.getoutput('ps -ax | grep "libgpiod_pulsein"')
# print (info)
# print("operational")
# posizione= info.find("sudo python testManager.py")
# posizione= posizione+ 28
# info=info[posizione:]

posizione = info.find("?")
# print(posizione)

if posizione != -1:
    info = info[:posizione]

    info = "sudo kill -9 " + info
    # print(info)
    info = commands.getoutput(info)
    # print(info)

# posizioneporta = "/dev/ttyUSB0"
#print(posizioneporta)
