from gpiozero import Motor
from time import sleep
import keyboard

motor1 = Motor(forward=6, backward=13)
motor2 = Motor(forward=12, backward=16)

try:
    print('w : forward, s : backward')
    
    while True:
        if keyboard.is_pressed('w'):
            motor1.forward()
            motor2.forward()
            print('going.. ')
        elif keyboard.is_pressed('s'):
            motor1.backward()
            motor2.backward()
            print('back..backing') 
        elif keyboard.is_pressed('q'):
            motor1.stop()
            motor2.stop()
            print("stopping....")
            break
        else:
            break

except KeyboardInterrupt:
    motor1.stop()
    motor2.stop()
    print("finished....")