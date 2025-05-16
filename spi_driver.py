from machine import SPI, Pin

class PicoSPI:
    def __init__(self, sck=2, mosi=3, miso=4, cs=5, baudrate=1000000):
        self.cs = Pin(cs, Pin.OUT)
        self.cs.value(1)
        self.spi = SPI(0, baudrate=baudrate, polarity=0, phase=0,
                       sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))

    def transfer(self, data_out, num_bytes_in):
        self.cs.value(0)
        self.spi.write(data_out)
        data_in = self.spi.read(num_bytes_in)
        self.cs.value(1)
        return data_in
