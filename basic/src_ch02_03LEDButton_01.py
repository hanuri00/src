from gpiozero import LED, Button
from time import sleep

led = LED(17)
btn = Button(16)

while True:
    btn.when_pressed = led.on
    btn.when_released = led.off
    sleep(1)
