from smbus import SMBus
import time
 
driver = 0x8 #driver atmega address
sensor = 0x4 #sensor atmaga address
bus = SMBus(1) 
 
print ("Flip Flopping")

ledstate = 0
while 1:
    time.sleep(0.250)
    if ledstate == 1:
        bus.write_byte(driver, 0x1) # switch driver on
	bus.write_byte(sensor, 0x0) # switch sensor off
        ledstate = 0
    elif ledstate == 0:
        bus.write_byte(driver, 0x0) # switch driver off
	bus.write_byte(sensor, 0x1) # switch sensor on
	ledstate = 1


