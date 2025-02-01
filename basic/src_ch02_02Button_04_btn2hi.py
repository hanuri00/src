from gpiozero import Button
from time import sleep

btn1 = Button(16)
btn2 = Button(20)

def hi():
    print('Hi. everyone!!')

def bye():
    print('Bye. see you again')

while True:
    btn1.when_pressed = hi
    btn2.when_pressed = bye
