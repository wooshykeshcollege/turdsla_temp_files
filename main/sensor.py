'''
SENSOR MODULE COMM

'''

import time
from smbus import SMBus
print(">>>>>tx_data module successfully imported")

addr = 0x4  # bus address
bus = SMBus(1)  # indicates /dev/ic2-1
speed = 349.5  # m/s


def mapp(x, in_min, in_max, out_min, out_max):
    return int(((x - in_min) * (out_max - out_min)) / ((in_max - in_min) + out_min))


def ConvertStringsToBytes(src):
    converted = []
    for b in src:
        converted.append(ord(b))
    return converted


def ConvertBytesToStrings(src):
    converted = ""
    for b in src:
        converted += chr(b)
    return converted


def get_data():
    time.sleep(0.005)
    try:
        data = bus.read_i2c_block_data(addr, 0x8, 8)
    except:
        print("remote i/o error")
        return -1, -1, 0, -1, -1

    answer = ConvertBytesToStrings(data)
    answer = answer.split("/")
    answer[1] = answer[1][0:int(answer[0])]
    string_data = answer[1].split(",")
    throttle = mapp(int(string_data[0]), 994, 1976, 0, 100)
    steering = mapp(int(string_data[1]), 994, 1988, -33, 33)
    kill = int(string_data[2])
    ping = (speed*int(string_data[3]))/(2*10**5)
    irstat = int(string_data[4])
    return throttle, steering, kill, ping, irstat


def handshake():
    time.sleep(0.005)
    with SMBus(1) as bus:
        bus.write_byte_data(80, 0, ConvertStringsToBytes("Handshake"))
    try:
        return bus.read_i2c_block_data(addr, 0x8, 8)
    except:
        print("remote i/o error")
        return -1
