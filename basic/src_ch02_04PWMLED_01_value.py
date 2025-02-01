from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(17)
led2 = PWMLED(27)

while True:
    led1.value= 0
    led2.value= 0
    sleep(0.3)

    led1.value= 0.5
    led2.value= 0.5
    sleep(0.3)

    led1.value= 1.0
    led2.value= 1.0
    sleep(0.3)
