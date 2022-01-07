from machine import Pin
import utime
key = Pin(23,Pin.IN)

while True:
    print(key.value())
    utime.sleep(0.1)
