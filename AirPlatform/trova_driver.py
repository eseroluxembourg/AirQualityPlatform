import time
import urllib

import commands
import serial

info = commands.getoutput("ps -ax | grep pulseio/libgpiod_pulsein")
print(info)
# print("operational")

posizione = info.find(
    "/usr/local/lib/python3.7/dist-packages/adafruit_blinka/microcontroller"
)
# print(posizione)
if posizione != -1:
    array = info.split("\n")
    # print(array)

    # print(len(array))
    for conta in range(len(array)):
        stringa = array[conta].lstrip(" ")
        # print(conta, stringa)
        # print(conta, ord(array[conta][0]))
        valori = stringa.split(" ")
        # print(valori[0])
        kid = stringa.find(
            "/usr/local/lib/python3.7/dist-packages/adafruit_blinka/microcontroller"
        )
        if kid != -1:
            processo = valori[0]
            risposta = "ps -p  " + processo + " -o etime"
            print(risposta)
            rispostakill = commands.getoutput(risposta)
            print(rispostakill)
            posizione = rispostakill.find("ELAPSED")
            print(posizione)

            rispostakill = rispostakill[posizione + 8 :]
            rispostakill = rispostakill.lstrip(" ")
            rispostakill = rispostakill.replace(":", "")

            print(1, rispostakill)
            tempo = int(rispostakill)
            print(tempo)
            if tempo > 60:

                # info = commands.getoutput("sudo python /home/pi/AirPlatform/killProTemp.py")

                info = commands.getoutput("ps -ax | grep pulseio/libgpiod_pulsein")
                print(info)

                posizione = info.find(
                    "/usr/local/lib/python3.7/dist-packages/adafruit_blinka/microcontroller"
                )
                # print(posizione)
                if posizione != -1:
                    array = info.split("\n")
                    # print(array)

                    # print(len(array))
                    for conta in range(len(array)):
                        stringa = array[conta].lstrip(" ")
                        # print(conta, stringa)
                        # print(conta, ord(array[conta][0]))
                        valori = stringa.split(" ")
                        # print(valori[0])
                        kid = stringa.find(
                            "/usr/local/lib/python3.7/dist-packages/adafruit_blinka/microcontroller"
                        )
                        if kid != -1:
                            processo = valori[0]
                            risposta = "sudo kill -9 " + processo
                            print(risposta)
                            rispostakill = commands.getoutput(risposta)

                info = commands.getoutput("ps -ax | grep testTemperatura.py")
                print(info)

                posizione = info.find("testTemperatura.py")

                if posizione != -1:
                    array = info.split("\n")

                    for conta in range(len(array)):
                        stringa = array[conta].lstrip(" ")
                        # print(conta, stringa)
                        # print(conta, ord(array[conta][0]))
                        valori = stringa.split(" ")
                        # print(valori[0])
                        kid = stringa.find("testTemperatura.py")
                        if kid != -1:
                            processo = valori[0]
                            risposta = "sudo kill -9 " + processo
                            print(risposta)
                            rispostakill = commands.getoutput(risposta)
