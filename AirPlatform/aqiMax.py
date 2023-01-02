#!/usr/bin/python

from __future__ import print_function

import json
import struct
import sys
import time
import urllib

import commands
import serial

DEBUG = 0
CMD_MODE = 2
CMD_QUERY_DATA = 4
CMD_DEVICE_ID = 5
CMD_SLEEP = 6
CMD_FIRMWARE = 7
CMD_WORKING_PERIOD = 8
MODE_ACTIVE = 0
MODE_QUERY = 1


def floatERR(stringa):
    ritorno = None
    try:
        ritorno = float(stringa)
    except:
        ritorno = None
    return ritorno


f = open("/home/pi/AirPlatform/PortaParticolato.txt", "r")
posizioneporta = f.read()
f.close()


ser = serial.Serial()

ser.port = posizioneporta
ser.baudrate = 9600

ser.open()
ser.flushInput()

byte, data = 0, ""


def dump(d, prefix=""):
    print(prefix + " ".join(x.encode("hex") for x in d))


def construct_command(cmd, data=[]):
    assert len(data) <= 12
    data += [
        0,
    ] * (12 - len(data))
    checksum = (sum(data) + cmd - 2) % 256
    ret = "\xaa\xb4" + chr(cmd)
    ret += "".join(chr(x) for x in data)
    ret += "\xff\xff" + chr(checksum) + "\xab"

    if DEBUG:
        dump(ret, "> ")
    return ret


def process_data(d):
    r = struct.unpack("<HHxxBB", d[2:])
    pm25 = r[0] / 10.0
    pm10 = r[1] / 10.0
    checksum = sum(ord(v) for v in d[2:8]) % 256
    return [pm25, pm10]


def process_version(d):
    r = struct.unpack("<BBBHBB", d[3:])
    checksum = sum(ord(v) for v in d[2:8]) % 256
    print(
        "Y: {}, M: {}, D: {}, ID: {}, CRC={}".format(
            r[0],
            r[1],
            r[2],
            hex(r[3]),
            "OK" if (checksum == r[4] and r[5] == 0xAB) else "NOK",
        )
    )


def read_response():
    byte = 0
    while byte != "\xaa":
        byte = ser.read(size=1)

    d = ser.read(size=9)

    if DEBUG:
        dump(d, "< ")
    return byte + d


def cmd_set_mode(mode=MODE_QUERY):
    ser.write(construct_command(CMD_MODE, [0x1, mode]))
    read_response()


def cmd_query_data():
    ser.write(construct_command(CMD_QUERY_DATA))
    d = read_response()
    values = []
    if d[1] == "\xc0":
        values = process_data(d)
    return values


def cmd_set_sleep(sleep=1):
    mode = 0 if sleep else 1
    ser.write(construct_command(CMD_SLEEP, [0x1, mode]))
    read_response()


def cmd_set_working_period(period):
    ser.write(construct_command(CMD_WORKING_PERIOD, [0x1, period]))
    read_response()


def cmd_firmware_ver():
    ser.write(construct_command(CMD_FIRMWARE))
    d = read_response()
    process_version(d)


def cmd_set_id(id):
    id_h = (id >> 8) % 256
    id_l = id % 256
    ser.write(construct_command(CMD_DEVICE_ID, [0] * 10 + [id_l, id_h]))
    read_response()


if __name__ == "__main__":
    # while True:
    cmd_set_sleep(0)
    cmd_set_mode(1)
    for t in range(2):
        values = cmd_query_data()
        if values is not None:

            f = open("/home/pi/AirPlatform/OffsetPM25.txt", "r")
            stringa = f.read()
            offset = floatERR(stringa)
            f.close()

            f = open("/home/pi/AirPlatform/AmplPM25.txt", "r")
            stringa = f.read()
            Amplificazione = floatERR(stringa)
            f.close()
            values[0] = values[0] * Amplificazione + offset

            f = open("/home/pi/AirPlatform/OffsetPM10.txt", "r")
            stringa = f.read()
            offset = floatERR(stringa)
            f.close()

            f = open("/home/pi/AirPlatform/AmplPM10.txt", "r")
            stringa = f.read()
            Amplificazione = floatERR(stringa)
            f.close()
                values[1]=values[1]*Amplificazione+offset
                stringa= "PM2.5: " + str( values[0])  + "ppm, PM10: " + str( values[1]) +"ppm"
                #print(stringa )
                time.sleep(0.3)
                
        print(stringa )
