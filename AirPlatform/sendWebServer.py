import datetime as dt
import json
import string
import time
import urllib

import Adafruit_DHT as dht
import commands
import requests
import serial

f = open("PlatformID.txt")  # riapriamo il file in lettura
appo_stringa = f.read()  # leggiamo tutto il contenuto del file
Device = int(appo_stringa)
print("ID Platform " + str(Device))
f.close()  # chiudiamo il file


umidita = None
temperature = None


CO2 = None
NO2 = None
NH3 = None
CO = None

PM10 = None
PM25 = None
LONG = 0
LAT = 0
GPS_precision = 2

# https://api.lps19airquality.esa.int/fpdemo

f = open("valori.dat", "r")
payload_json = f.read()
f.close()
# print(payload_json)

url = "https://api.aqp.eo.esa.int/api/acquisitions"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

r = requests.post(
    url,
    data=payload_json,
    headers=headers,
    auth=("airplatform", "airplatform"),
    timeout=10,
)

# print(r.url)
print(r.content)
print(r.status_code)
