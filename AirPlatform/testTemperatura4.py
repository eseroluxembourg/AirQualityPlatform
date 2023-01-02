import datetime as dt
import time

import adafruit_dht
import board

dhtDevice = adafruit_dht.DHT22(board.D4)
for conta in range(1, 1000):

    # dhtDevice = adafruit_dht.DHT22(board.D4)
    time.sleep(0.2)
    t = dhtDevice.temperature
    h = dhtDevice.humidity

    # h,t = dht.read_retry(dht.DHT22, 4)
    temp = str("Temperature={0:0.1f}*C, Humidity={1:0.1f}%".format(t, h))
    time.sleep(1)
    print(temp)
