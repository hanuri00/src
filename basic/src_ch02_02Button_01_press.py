from gpiozero import Button
from time import sleep

btn = Button(16)

while True:
    btn.wait_for_press()
    print('Button was pressed')
