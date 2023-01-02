import datetime as dt
import time

import commands
import serial

while 1:

    info = commands.getoutput("sudo python3 Client_ping.py")
    print(info)

    time.sleep(60)
