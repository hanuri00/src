from gpiozero import Button
from time import sleep

btn = Button(16)

while True:
    if btn.is_pressed:
        print('Button is pressed')
    else:
        print('Button is not pressed')
    sleep(2)
