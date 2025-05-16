from machine import I2C, Pin

class PicoI2C:
    def __init__(self, scl=1, sda=0, freq=100000):
        self.i2c = I2C(0, scl=Pin(scl), sda=Pin(sda), freq=freq)

    def scan(self):
        return self.i2c.scan()

    def write(self, address, data):
        self.i2c.writeto(address, data)

    def read(self, address, num_bytes):
        return self.i2c.readfrom(address, num_bytes)
