import datetime as dt
import subprocess
import time
import urllib

import Adafruit_DHT as dht
import adafruit_dht
import board

# h,t = dht.read_retry(dht.DHT22, 4)
subprocess.getoutput("sudo python /home/pi/AirPlatform/killTemp.py")

dhtDevice = adafruit_dht.DHT22(board.D4)
time.sleep(0.2)
t = dhtDevice.temperature
h = dhtDevice.humidity


temp = str("Temperature={0:0.1f}*C, Humidity={1:0.1f}%".format(t, h))
subprocess.getoutput("sudo python /home/pi/AirPlatform/killTemp.py")
time.sleep(0.2)
print(temp)
