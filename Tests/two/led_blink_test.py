from smbus import SMBus
import time

sensor = 0x4  # sensor atmaga address
bus = SMBus(1)

print("Flip Flopping")

ledstate = 0
while 1:
    time.sleep(0.250)
    if ledstate == 1:
        bus.write_byte(sensor, ledstate)  # switch sensor off
        ledstate = !ledstate
    elif ledstate == 0:
        bus.write_byte(sensor, ledstate)  # switch sensor on
        ledstate = !ledstate
