from gpiozero import Motor, Robot
from time import sleep

motor1 = Motor(26, 19)       # right_front 1    ok
motor2 = Motor(27, 22)       # right_rear 2     ok
motor3 = Motor(21, 20)       # left_front 3     ok
motor4 = Motor(24, 23)       # left_rear 4      ok

#Testing motor1, 2, 3, 4, step by step...
motor = motor1

try:
    while True:
        motor.forward(speed=1)
        sleep(2)
        motor.forward(speed=0.5)
        sleep(2)
        motor.forward(speed=0)
        sleep(1)
        motor.backward(speed=1)
        sleep(2)
        motor.backward(speed=0.5)
        sleep(2)
        motor.backward(speed=0)
        sleep(1)
        sleep(0.1)

except Exception as err:
    print(f'An Erro occured : {err}')
except KeyboardInterrupt:
    print('Keyboard Interrupted')
finally:
    motor.off()
    print('Finished..')