import time
from machine import Pin

sensor = Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(13, Pin.OUT)

led_state = 0
last_trigger_time = 0
DEBOUNCE_MS = 100  

def toggle(pin):
    global led_state, last_trigger_time
    now = time.ticks_ms()
    
    if time.ticks_diff(now, last_trigger_time) > DEBOUNCE_MS:
        led_state = 1 - led_state
        led.value(led_state)
        last_trigger_time = now

sensor.irq(trigger=Pin.IRQ_FALLING, handler=toggle)

while True:
    time.sleep(1)
