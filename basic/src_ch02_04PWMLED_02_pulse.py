from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(17)
led2 = PWMLED(27)

while True:
    led1.pulse()
    led2.pulse()
    sleep(5)