from gpiozero import Motor
from time import sleep
import keyboard

motor = Motor(forward=6, backward=13)

try:
    print('w : forward, s : backward')
    
    while True:
        if keyboard.is_pressed('w'):
            motor.forward()
            print('going.. ')
        elif keyboard.is_pressed('s'):
            back()
            print('back..backing') 
        elif keyboard.is_pressed('q'):
            motor.stop()
            print("stopping....")
            break
        else:
            motor.stop()

except KeyboardInterrupt:
    motor.stop()
    print("finished....")