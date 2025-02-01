from gpiozero import LEDCharDisplay
from time import sleep
from random import randint

display = LEDCharDisplay(24, 25, 22, 27, 17, 23, 18, dp=5)


while True:
    num=randint(0,10)
    display.source=str(num)
    sleep(2)