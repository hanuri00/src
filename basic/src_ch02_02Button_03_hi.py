from gpiozero import Button
from time import sleep

btn = Button(16)

def hi():
    print('Hi. everyone!!')

def bye():
    print('Bye. see you again')

while True:
    btn.when_pressed = hi
    btn.when_released = bye
    sleep(1)
