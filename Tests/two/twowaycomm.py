from smbus import SMBus
sensor = 0x4
bus = SMBus(1)
data = 45
bus.write_byte_data(sensor, 0, data)
#b = bus.read_byte_data(sensor, 0)
b = bus.read_i2c_block_data(Sensor, 0, 10)
print(b)
