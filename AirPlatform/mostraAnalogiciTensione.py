import subprocess

while 1:
    x = subprocess.getoutput("sudo python /home/pi/AirPlatform/testArduino2.py")
    # print(x)
    f = open("/home/pi/AirPlatform/tensione.txt", "r")
    appo_stringa = f.read()
    f.close()
    print(appo_stringa)
  
