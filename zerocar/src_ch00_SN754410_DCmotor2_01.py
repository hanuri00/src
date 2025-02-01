from gpiozero import Robot, Motor
from time import sleep
import keyboard

frontWheel = Robot(left=(6, 13), right=(12, 16))

def go():
    frontWheel.forward()

def back():
    frontWheel.backward()

def left():
    frontWheel.left()

def right():
    frontWheel.right()

def stop():
    frontWheel.stop()


try:
    print('w : forward, s : backward, a : leftturn, d : rightturn')
    
    while True:
        if keyboard.is_pressed('w'):
            go()
            print('going.. ')
        elif keyboard.is_pressed('s'):
            back()
            print('back..backing')
        elif keyboard.is_pressed('a'):
            left()
            print('back..backing')
        elif keyboard.is_pressed('d'):
            right()
            print('back..backing')    
        elif keyboard.is_pressed('q'):
            stop()
            print("stopping....")
            break
        else:
            stop()

except KeyboardInterrupt:
    stop()
    print("finished....")