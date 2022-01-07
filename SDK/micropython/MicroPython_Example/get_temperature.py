import machine
import utime
sensorTemp = machine.ADC(4)
offset = 3.3/65535


while True:
    read = sensorTemp.read_u16()*offset
    temp = 27 - (read - 0.706)/0.001721

    print(temp)
    utime.sleep(2)
