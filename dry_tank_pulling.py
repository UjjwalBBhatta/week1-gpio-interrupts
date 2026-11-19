import time
from machine import Pin

p0 = Pin(4, Pin.IN, Pin.PULL_UP)
p1 = Pin(13, Pin.OUT)
last_state = p0.value()

while True:
    current_state = p0.value()
    if current_state != last_state:
        time.sleep_ms(20)
        if p0.value()==current_state:
            if current_state == 0:
                p1.value(not p1.value())
            last_state = current_state
    time.sleep_ms(5)