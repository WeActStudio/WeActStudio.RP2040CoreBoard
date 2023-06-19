from machine import Pin,PWM
import utime
LED = PWM(Pin(25))
n = 0

while True:
    LED.duty_u16(abs(32000-n*1000))
    n = (n+4)%64
    print(n)
    utime.sleep(0.1)