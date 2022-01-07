from machine import UART,Pin
import utime
uart = UART(0,baudrate=115200,bits=8,parity=None,stop=1,tx=Pin(0),rx=Pin(1))
n = 0
while True:
    n = (n+1)%100
    print(n)
    uart.write("num = %3d\r\n"%(n))
    utime.sleep(1)
