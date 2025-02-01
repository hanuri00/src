from gpiozero import LEDBoard
from time import sleep
from random import choice

leds = LEDBoard(17, 27, 22, 13, 19)

while True:
    led=choice(leds)
    led.on()
    sleep(1)
    led.off()
    sleep(0.5)