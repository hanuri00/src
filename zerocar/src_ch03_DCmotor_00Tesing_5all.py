from gpiozero import Motor, Robot
from time import sleep

#motor = Motor(21, 20)       # right_front 1    OK
#motor = Motor(19, 26)       # right_rear 2     ok
#motor = Motor(24, 23)       # left_front 3     ok
#motor = Motor(27, 22)       # left_rear 4      ok

rightWheel = Robot(Motor(21, 20), Motor(19, 26))
leftWheel = Robot(Motor(24, 23), Motor(27, 22))


try:
    while True:
        #go
        rightWheel.forward()
        leftWheel.forward()
        sleep(2)

        #back
        rightWheel.backward()
        leftWheel.backward()
        sleep(2)
        
        #right turnning
        rightWheel.backward()
        leftWheel.forward()
        sleep(2)

        #left turnning
        rightWheel.forward()
        leftWheel.backward()
        sleep(2)

        #stop
        rightWheel.stop()
        leftWheel.stop()
        sleep(2)

        sleep(0.1)

except Exception as err:
    print(f'An Erro occured : {err}')
except KeyboardInterrupt:
    print('Keyboard Interrupted')
finally:
    rightWheel.stop()
    leftWheel.stop()
    print('Finished..')