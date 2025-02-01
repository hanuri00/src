from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(17)
led2 = PWMLED(27)

while True:
    for i in range(256):
        led1.value=i/255
        led2.value=i/255
        sleep(0.05)