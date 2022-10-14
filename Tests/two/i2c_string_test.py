from smbus2 import SMBus

with SMBus(1) as bus:
    # Write a block of 8 bytes to address 80 from offset 0
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    bus.write_i2c_block_data(0x8, 0, data)
