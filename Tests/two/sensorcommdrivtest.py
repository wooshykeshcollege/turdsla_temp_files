import time
from smbus import SMBus
print(">>>>>tx_data module successfully imported")

sensor = 0x4  # sensor address
driver = 0x8  # driver address
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
        data = bus.read_i2c_block_data(sensor, 0x8, 8)
    except:
        print("remote i/o error")
        return 0, 0, 0, 0, 0

    answer = ConvertBytesToStrings(data)
    print(answer)
    answer = answer.split("/")
    answer[1] = answer[1][0:int(answer[0])]
    string_data = answer[1].split(",")
    throttle = mapp(int(string_data[0]), 994, 1976, 0, 100)
    steering = mapp(int(string_data[1]), 994, 1988, 0, 100)
    kill = mapp(int(string_data[2]), 994, 1988, 0, 1)
    ping = ((speed*int(string_data[3]))/(2*10**5))
    ir_stat = int(string_data[4])
    print(throttle, ",", steering, ",", kill, ",", ping, ",", ir_stat)
    return throttle, steering, kill, ping, ir_stat


def send_data(throttle, steering, kill):
    if kill == 1:
        message = "5/"+str(0)+","+str(0)+",1"
        bus.write_i2c_block_data(driver, 0, message)
    else:
        dummy = str(throttle)+","+str(steering)+","+str(kill)
        message = str(len(dummy))+"/"+dummy
        bus.write_i2c_block_data(driver, 0, message)


for i in range(100):
    throttle, steering, kill, ping, ir_stat = get_data()
    print(throttle, ",", steering, ",", kill, ",", ping, ",", ir_stat)
