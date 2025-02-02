from gpiozero import Motor
from time import sleep

#motor = Motor(21, 20)       # right_front 1    ok
#motor = Motor(26, 19)       # right_rear 2     ok
#motor = Motor(23, 24)       # left_front 3     ok
#motor = Motor(22, 27)       # left_rear 4      ok

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