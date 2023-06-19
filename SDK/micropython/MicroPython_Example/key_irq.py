from machine import Pin

p2 = Pin(23, Pin.IN, Pin.PULL_UP)

p2.irq(lambda pin: print("IRQ with flags:", pin.irq().flags()),Pin.IRQ_RISING)
