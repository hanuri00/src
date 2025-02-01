from gpiozero import LED
from random import randint
from time import sleep

led1 = LED(17)
led2 = LED(27)

def rand():
    yield randint(0,1)

while True:
    led1.source=rand()
    led2.source=rand()
    sleep(1)
