from gpiozero import RGBLED
from time import sleep

rgbled = RGBLED(16, 20, 21)

while True:
    rgbled.red = 1
    sleep(1)
    rgbled.green = 1
    sleep(1)
    rgbled.blue = 1
    sleep(1)