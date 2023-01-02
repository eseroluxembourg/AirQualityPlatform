import datetime as dt
import json
import os
import subprocess

import requests


def sendMessage(message):
    print(message)


def esegui_comando(command):
    info = ""
    print(command)
    # print(chat_id)

    # info = commands.getoutput("python send_telegram_msg_start.py")
    if command == "Info":
        info = subprocess.getoutput("uname -a")

    if command == "T":
        info = "test"
    if command == "Stm":
        info = "ST"
        # send telegram message

    if command == "??":
        info = "T per test" + "/n"
        info = info + "Dg- Num sens - Data ini Data Fin"

        # sendMessage(chat_id, 'Sf - Send foto')
        # sendMessage(chat_id, 'Info Versione SO')
        # sendMessage(chat_id, 'Ver Versione codice AQP')
        # sendMessage(chat_id, 'Sa- Send audio')
        # sendMessage(chat_id, 'Sd-nome file Send document')
        # sendMessage(chat_id, 'cmd - comando ')
        # sendMessage(chat_id, 'Sa- Send audio')
        # sendMessage(chat_id, 'Lf - lista file prog python')
        # sendMessage(chat_id, 'KM -  Kill Manager')
        # sendMessage(chat_id, 'Dp - Dammi processi')
        # sendMessage(chat_id, 'Ping - ping www.google.it')
        # sendMessage(chat_id, 'Calibra - effettua cal aria pulita')
        # sendMessage(chat_id, 'Darduino- Dammi ppm & Volt Arduino')
        # sendMessage(chat_id, 'Dgps- Dammi valori GPS')
        # sendMessage(chat_id, 'Dtemperature- Dammi valori Temp & Umid')
        # sendMessage(chat_id, 'Dparticolate- Dammi valori Particolato')

        # sendMessage(chat_id, 'reboot ')

    if command.find("cmd ") == 0:
        info = subprocess.getoutput(command[4:])
        # print (command[4:])

    if command.find("Sf ") == 0:
        f = open(command[3:], "rb")
        response = bot.sendPhoto(chat_id, f)
    if command.find("Ver") == 0:
        info = subprocess.getoutput("cat ver.txt")
        # sendMessage(chat_id, info)
    if command.find("Dg ") == 0:
        # sendMessage(chat_id,command[3:] )
        # info = os.system("sudo python dammi_grafico.py " +command[3:])
        info = subprocess.getoutput("sudo python dammi_grafico.py " + command[3:])
        # sendMessage(chat_id, info)

        f = open("/home/pi/AirPlatform/grafico.png", "rb")
        response = bot.sendPhoto(chat_id, f)
    if command.find("Sa ") == 0:
        f = open(command[3:], "rb")
        response = bot.sendAudio(chat_id, f)
    if command.find("Sd ") == 0:
        f = open(command[3:], "rb")
        response = bot.sendDocument(chat_id, f)
    if command.find("ScriviF ") == 0:
        print(command[8:])
        info = subprocess.getoutput("sudo python scrivi_file.py " + command[8:])

    if command.find("Upload ") == 0:
        print(command[7:])
        file_nome = command[7:]
        # info = subprocess.getoutput("sudo python scrivi_file.py " +command[7:])

        # path = os.path.join(r'C:\Users\aless\Desktop', "test.txt")
        path = os.path.join(file_nome)
        url = "https://aqp.gedatech.it/testaqp/dataserver/upload.php"

        data = {"file": open(path, "r")}

        response = requests.post(
            url, files={"file": data["file"]}, auth=("aqp", "aqp654321")
        )
        info = str(response.status_code) + " " + str(response.content)

        # print("Status Code", response.status_code)
        # print("Response ", response.content)
    if command.find("Download ") == 0:
        print(command[9:])
        file_nome = command[9:]
        info = subprocess.getoutput("sudo wget " + file_nome)
        # info = subprocess.getoutput("sudo python scrivi_file.py " +command[7:])

        # path = os.path.join(r'C:\Users\aless\Desktop', "test.txt")

    if command == "Lf":
        info = commands.getoutput("ls *.py")
        sendMessage(chat_id, info)
    if command == "KM":
        info = subprocess.getoutput("sudo python killManager.py ")
        # sendMessage(chat_id, info)
    if command == "Dp":
        info = subprocess.getoutput("ps ax | grep -i .py")

    if command == "reboot":
        sendMessage(chat_id, "rebootok")
        info = subprocess.getoutput("reboot")
        # sendMessage(chat_id, info)
    if command == "Cal":
        info = subprocess.getoutput("sudo python Calibra.py ")
        # sendMessage(chat_id, info)
    if command[:9] == "Dd":
        info = str(dt.datetime.now())
        # sendMessage(chat_id, n0)

    if command == "Ping":

        info = subprocess.getoutput("ping -c 1 -w 1 www.google.it")
        # info = os.system("ping -c 1 -w 1 www.google.it")
        # sendMessage(chat_id, info)
    if command == "Darduino":
        info = subprocess.getoutput("sudo python testArduino3.py")
        # sendMessage(chat_id, info)
    if command == "Dgps":
        info = subprocess.getoutput("sudo python gpsok.py")
        # sendMessage(chat_id, info)
    if command == "Dtemperature":
        info = subprocess.getoutput("sudo python testTemperatura.py")
        sendMessage(chat_id, info)
    if command == "Dparticolate":
        info = subprocess.getoutput("sudo python aqiMax.py")
        sendMessage(chat_id, info)

    return info


url = "https://aqp.gedatech.it/testaqp/dataserver/get_commands.php"

f = open("PlatformID.txt")
appo_stringa = f.read()
Device = int(appo_stringa)
# print(Device)
# print("Air quality Platform " + str(Device))
f.close()
# params = {'id': '58'}

params = {"id": Device}
response = requests.get(
    "https://aqp.gedatech.it/testaqp/dataserver/get_commands.php",
    params=params,
    auth=("aqp", "aqp654321"),
    timeout=10,
)

print(response.content)
print(response.status_code)

var = response.content[:-17]

data = json.loads(var.decode(encoding="UTF-8"))

print("data")
print(data)
comandi = data["commands"]
print(comandi)
# print(len(comandi))


for linea in range(len(comandi)):
    # print(comandi[linea])
    a = esegui_comando(comandi[linea])
    print(a)

    n0 = str(dt.datetime.utcnow())
    appo_stringa = n0[0:19]
    a = "# " + appo_stringa + " " + comandi[linea] + "\n >" + str(a) + "\n"
    a = a.encode("utf-8")

    # aggiungere comando iniziale alla risposta
    response = requests.post(
        "https://aqp.gedatech.it/testaqp/dataserver/response.php",
        params=params,
        data=a,
        auth=("aqp", "aqp654321"),
        timeout=10,
    )
    print("risposta ")
    print(response.content)
