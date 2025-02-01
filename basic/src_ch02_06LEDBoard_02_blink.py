from gpiozero import LEDBoard
from time import sleep
from random import choice

leds = LEDBoard(17, 27, 22, 13, 19, pwm=True)

while True:
    led = choice(leds)
    led.on()
    sleep(0.3)