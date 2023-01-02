import datetime as dt
import time

import Adafruit_DHT as dht
import adafruit_dht
import board

n0 = str(dt.datetime.utcnow())
# h,t = dht.read_retry(dht.DHT22, 4)
try:
    dhtDevice = adafruit_dht.DHT22(board.D4)
    time.sleep(0.2)

    t = dhtDevice.temperature
    h = dhtDevice.humidity

    temp = str("Temperature={0:0.1f}*C, Humidity={1:0.1f}%".format(t, h))
    if h > 100:

        dhtDevice = adafruit_dht.DHT22(board.D4)
        time.sleep(0.2)

        t = dhtDevice.temperature
        h = dhtDevice.humidity

        temp = str("Temperature={0:0.1f}*C, Humidity={1:0.1f}%".format(t, h))

    temp = n0[:19] + " " + temp
    if temp.find("*C") > -1:
        print(temp)

except:
    time.sleep(0.8)
    dhtDevice = adafruit_dht.DHT22(board.D4)
    time.sleep(0.4)

    t = dhtDevice.temperature
    h = dhtDevice.humidity

    temp = str("Temperature={0:0.1f}*C, Humidity={1:0.1f}%".format(t, h))
    if h > 100:

        dhtDevice = adafruit_dht.DHT22(board.D4)
        time.sleep(0.4)

        t = dhtDevice.temperature
        h = dhtDevice.humidity

        temp = str("Temperature={0:0.1f}*C, Humidity={1:0.1f}%".format(t, h))

    temp = n0[:19] + " " + temp
    if temp.find("*C") > -1:
        print(temp)
