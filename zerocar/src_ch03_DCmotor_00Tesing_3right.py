from gpiozero import Motor, Robot
from time import sleep

#motor = Motor(26, 19)       # right_front 1    ok
#motor = Motor(27, 22)       # right_rear 2     ok
#motor = Motor(21, 20)       # left_front 3     ok
#motor = Motor(24, 23)       # left_rear 4      ok

rightWheel = Robot(Motor(26, 19), Motor(27, 22))
leftWheel = Robot(Motor(21, 20), Motor(24, 23))


try:
    while True:
        rightWheel.forward(speed=1)
        sleep(2)
        rightWheel.forward(speed=0.5)
        sleep(2)
        rightWheel.forward(speed=0)
        sleep(1)
        rightWheel.backward(speed=1)
        sleep(2)
        rightWheel.backward(speed=0.5)
        sleep(2)
        rightWheel.backward(speed=0)
        sleep(1)
        
        sleep(0.1)

except Exception as err:
    print(f'An Erro occured : {err}')
except KeyboardInterrupt:
    print('Keyboard Interrupted')
finally:
    rightWheel.stop()
    print('Finished..')