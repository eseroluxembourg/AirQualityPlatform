import string
import time

import pynmea2
import serial

port = "/dev/ttyAMA0"  # the serial port to which the pi is connected.
# $GPGGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx*hh
# 1    = UTC of Position
# 2    = Latitude
# 3    = N or S
# 4    = Longitude
# 5    = E or W
# 6    = GPS quality indicator (0=invalid; 1=GPS fix; 2=Diff. GPS fix)
# 7    = Number of satellites in use [not those in view]
# 8    = Horizontal dilution of position
# 9    = Antenna altitude above/below mean sea level (geoid)
# 10   = Meters  (Antenna height unit)
# 11   = Geoidal separation (Diff. between WGS-84 earth ellipsoid and
#       mean sea level.  -=geoid is below WGS-84 ellipsoid)
# 12   = Meters  (Units of geoidal separation)
# 13   = Age in seconds since last update from diff. reference station
# 14   = Diff. reference station ID#
# 15   = Checksum
# create a serial object
ser = serial.Serial(port, baudrate=9600, timeout=3)

# ser = serial.Serial(port)
while 1:

    data = ser.readline()

    # print (data)

    # if data[0:6] == '$GPGGA': # the long and lat data are always contained in the GPGGA string of the NMEA data
    if data[0:6] == "$GPRMC":

        msg = pynmea2.parse(data)
        # print (msg)
        # print repr(msg)
        print(str(msg.datestamp) + " " + str(msg.timestamp))

        # print ("ENDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
        break

# wait for the serial port to churn out data
