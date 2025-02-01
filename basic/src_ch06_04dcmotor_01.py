from gpiozero import Motor
from time import sleep

frontWheel = Motor(forward=12, backward=16)

while True:
    frontWheel.forward()
    sleep(3)
    frontWheel.backward()
    sleep(1)