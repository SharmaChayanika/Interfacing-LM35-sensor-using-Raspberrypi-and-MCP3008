import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')

print('| Temperature (chr(176)) |'.format(*range(8)))
print('-' * 57)

while True:
    
    values = [0]*8
    voltage=[0]*8
    temperature=[0]*8

    for i in range(8):
        
        values[i] = mcp.read_adc(i)
        voltage[i]=values[i]*3.3/1024
        temperature[i]= voltage[i]*100

    
    print('| {0:>4} |'.format(*temperature))
    # Pause for half a second.
    time.sleep(0.5)
