from gpiozero import LED, Button
from time import sleep

led = LED(17)
btn = Button(16)

while True:
    btn.when_pressed = led.toggle()
    sleep(1)
