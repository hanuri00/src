from gpiozero import Motor, Robot
from time import sleep

#motor = Motor(21, 20)       # right_front 1    ok
#motor = Motor(26, 19)       # right_rear 2     ok
#motor = Motor(23, 24)       # left_front 3     ok
#motor = Motor(22, 27)       # left_rear 4      ok

rightWheel = Robot(Motor(21, 20), Motor(26, 19))
leftWheel = Robot(Motor(23, 24), Motor(22, 27))

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