from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)

while True:
    led1.blink()
    led2.blink()
    sleep(2)