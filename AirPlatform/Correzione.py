import time

import commands
import requests
import RPi.GPIO as GPIO

print("Questo programma termina l'esecuzione invio dati al Server \n")
print(
    "Per riavviare il programma che invia dati al server occorre fare il reboot della piattaforma \n"
)

print("This program stops the sending data to the webserver \n")
print("To restart sending data to the Webserver please reboot the Platform \n")

valore = raw_input("Prem invio per procedere:")
x = commands.getoutput("sudo python /home/pi/AirPlatform/killManager.py")
print(x)


while 1:
    x = commands.getoutput("sudo clear")
    print(x)
    print("Premi ")
    print("1 Per cambiare valore offset CO")
    print("2 Per cambiare valore Amplificazione CO:  ")
    print("3 Per cambiare  valore offset NH3 ")
    print("4 Per cambiare valore Amplificazione NH3: ")
    print("5 Per cambiare  valore offset NO2:")
    print("6 Per cambiare  valore Amplificazione NO2:")
    print("7 Per cambiare  valore offset CO2:")
    print("8 Per cambiare  valore Amplificazione CO2:")
    print("9 Per Visualizzare tensione Arduino:")
    print("10 Per cambiare  riferimento tensione  CO  in aria pulita :")
    print("11 Per cambiare  riferimento tensione  NH3  in aria pulita :")
    print("12 Per cambiare  riferimento tensione  NO2  in aria pulita :")
    print("13 Per cambiare  riferimento tensione  CO2  in aria pulita :")
    print("14 Per cambiare  Delta range  CO2 da aria pulita a saturazione:")

    print("15 Per uscire e fare il reboot della piattaforma \n")

    valore = raw_input("Inserisci la scelta: ")
    if valore == "1":
        valore = raw_input("Inserisci valore offset CO: ")
        f = open("/home/pi/AirPlatform/OffsetCO.txt", "w")
        f.write(valore)
        f.close()

    if valore == "2":
        valore = raw_input("Inserisci valore Amplificazione CO: ")
        f = open("/home/pi/AirPlatform/AmplCO.txt", "w")
        f.write(valore)
        f.close()

    if valore == "3":
        valore = raw_input("Inserisci valore offset NH3: ")
        f = open("/home/pi/AirPlatform/OffsetNH3.txt", "w")
        f.write(valore)
        f.close()

    if valore == "4":
        valore = raw_input("Inserisci valore Amplificazione NH3: ")
        f = open("/home/pi/AirPlatform/AmplNH3.txt", "w")
        f.write(valore)
        f.close()

    if valore == "5":
        valore = raw_input("Inserisci valore offset NO2: ")
        f = open("/home/pi/AirPlatform/OffsetNO2.txt", "w")
        f.write(valore)
        f.close()

    if valore == "6":
        valore = raw_input("Inserisci valore Amplificazione NO2: ")
        f = open("/home/pi/AirPlatform/AmplNO2.txt", "w")
        f.write(valore)
        f.close()

    if valore == "7":
        valore = raw_input("Inserisci valore offset CO2: ")
        f = open("/home/pi/AirPlatform/OffsetCO2.txt", "w")
        f.write(valore)
        f.close()

    if valore == "8":
        valore = raw_input("Inserisci valore Amplificazione NO2: ")
        f = open("/home/pi/AirPlatform/AmplCO2.txt", "w")
        f.write(valore)
        f.close()

    if valore == "9":
        x = commands.getoutput("sudo python /home/pi/AirPlatform/testArduino3.py")
        print(x)

    if valore == "10":

        valore = raw_input("Inserisci valore tensione CO: ")
        f = open("/home/pi/AirPlatform/V0CO.txt", "w")
        f.write(valore)
        f.close()
        print(x)

    if valore == "11":

        valore = raw_input("Inserisci valore tensione NH3: ")
        f = open("/home/pi/AirPlatform/V0NH3.txt", "w")
        f.write(valore)
        f.close()
        print(x)

    if valore == "12":

        valore = raw_input("Inserisci valore tensione NO2: ")
        f = open("/home/pi/AirPlatform/V0NO2.txt", "w")
        f.write(valore)
        f.close()
        print(x)

    if valore == "13":

        valore = raw_input("Inserisci valore tensione CO2: ")
        f = open("/home/pi/AirPlatform/V0CO2.txt", "w")
        f.write(valore)
        f.close()
        print(x)

    if valore == "14":

        valore = raw_input("Inserisci Delta range  CO2 da aria pulita a saturazione:: ")
        f = open("/home/pi/AirPlatform/DECO2.txt", "w")
        f.write(valore)
        f.close()
        print(x)

    if valore == "15":
        x = commands.getoutput("sudo reboot")
        break
    time.sleep(5)
