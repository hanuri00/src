from gpiozero import Robot
from time import sleep
import keyboard

frontWheel = Robot(left=(6, 13), right=(12, 16))

try:
    print('w : forward, s : backward')
    
    while True:
        if keyboard.is_pressed('w'):
            frontWheel.forward()
            print('going.. ')
        elif keyboard.is_pressed('s'):
            frontWheel.backward()
            print('back..backing') 
        elif keyboard.is_pressed('q'):
            frontWheel.stop()
            print("stopping....")
            break
        else:
            break

except KeyboardInterrupt:
    frontWheel.stop()
    print("finished....")