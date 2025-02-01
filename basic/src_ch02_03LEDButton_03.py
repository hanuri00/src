from gpiozero import LED, Button
from time import sleep

led = LED(17)
btn = Button(16)

while True:
    led.source = btn
    sleep(1)
