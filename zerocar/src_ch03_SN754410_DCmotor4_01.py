#-*- coding: utf-8 -*-

from zeroCar import rightWheel, leftWheel
from time import sleep

def go(speed):
    print('go!!!!!')
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=speed)

def back(speed):
    print('back.. back')
    rightWheel.backward(speed=speed)
    leftWheel.backward(speed=speed)

def turn_left(speed):
    print('left turning!!!!!')
    rightWheel.forward(speed=speed)
    leftWheel.backward(speed=speed)

def turn_right(speed):
    print('right turning!!!!!')
    rightWheel.backward(speed=speed)
    leftWheel.forward(speed=speed)
    
def go_left(speed):
    print('go and left !')
    rightWheel.forward(speed=speed)
    leftWheel.forward(speed=speed*0.5)
    
def go_right(speed):
    print('go and right !')
    rightWheel.forward(speed=speed*0.5)
    leftWheel.forward(speed=speed)

def stop():
    rightWheel.stop()
    leftWheel.stop()

try:
    while True:
        go(1)
        sleep(2)
        stop()
        sleep(0.5)
        back(1)
        sleep(2)
        stop()
        sleep(0.5)
        turn_left(1)
        sleep(2)
        stop()
        sleep(0.5)
        turn_right(1)
        sleep(2)
        stop()
        sleep(0.5)
        go_left(1)
        sleep(2)
        stop()
        sleep(0.5)
        go_right(1)
        sleep(2)
        stop()
    
        sleep(0.1)


except Exception as err:
    print(f'An Erro occured : {err}')
except KeyboardInterrupt:
    print('Keyboard Interrupted')
finally:
    stop()
    print('Finished..')