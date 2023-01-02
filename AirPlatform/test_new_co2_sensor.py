from smbus import SMBus

I2C_CHANNEL = 1
DEVICE_ADDRESS = 0x41
SELF_TEST = (0x50, 1)
READ_CO2 = (0x34, 2)


def read_i2c_block(register, num_bytes):
    bus = SMBus(I2C_CHANNEL)
    return int.from_bytes(
        bus.read_i2c_block_data(DEVICE_ADDRESS, register, num_bytes), "big"
    )


def test():
    if read_i2c_block(SELF_TEST[0], SELF_TEST[1]) == 85:
        print("CO2 sensor is working properly!")
        co2_level = read_i2c_block(READ_CO2[0], READ_CO2[1])
        print("Current CO2 in ppm: {}".format(co2_level))


if __name__ == "__main__":
    test()
