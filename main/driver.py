import time
from smbus import SMBus
print(">>>>>tx_data module successfully imported")

addr = 0x8  # bus address
bus = SMBus(1)  # indicates /dev/ic2-1


def ConvertStringsToBytes(src):
    converted = []
    for b in src:
        converted.append(ord(b))
    return converted


def handshake():
    time.sleep(0.005)
    with SMBus(1) as bus:
        bus.write_byte_data(addr, 0, 2)
    try:
        data = bus.read_byte_data(addr, 0)
        return data
    except:
        print("remote i/o error")
        return -1


def drive(throttle, steering):
    time.sleep(0.005)
    with SMBus(1) as bus:
        bus.write_byte_data(addr, 0, 3)
    time.sleep(0.01)
    with SMBus(1) as bus:
        bus.write_byte_data(addr, 0, ConvertStringsToBytes(
            str(steering) + "/"+str(throttle)))
# check if the timing works out, adjust accordingly


def stop():
    time.sleep(0.005)
    with SMBus(1) as bus:
        bus.write_byte_data(addr, 0, 4)


def kill():
    time.sleep(0.005)
    with SMBus(1) as bus:
        bus.write_byte_data(addr, 0, 5)


def init():
    time.sleep(0.005)
    with SMBus(1) as bus:
        bus.write_byte_data(addr, 0, 6)
