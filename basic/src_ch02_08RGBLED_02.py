from gpiozero import RGBLED
from time import sleep

rgbled = RGBLED(16, 20, 21)

while True:
    rgbled.color=(0, 0, 0)
    sleep(1)
    rgbled.color=(1, 0, 0)
    sleep(1)
    rgbled.color=(0, 1, 0)
    sleep(1)
    rgbled.color=(0, 0, 1)
    sleep(1)
    rgbled.color=(1, 0, 1)
    sleep(1)
    rgbled.color=(1, 1, 1)
    sleep(1)