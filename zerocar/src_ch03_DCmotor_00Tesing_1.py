from gpiozero import Motor
from time import sleep

motor = Motor(21, 20)       # right_front 1    OK
#motor = Motor(19, 26)       # right_rear 2     ok
#motor = Motor(24, 23)       # left_front 3     ok
#motor = Motor(27, 22)       # left_rear 4      ok

try:
    while True:
        motor.forward()
        sleep(2)
        motor.forward(speed=0.5)
        sleep(1)
        sleep(0.1)

except Exception as err:
    print(f'An Erro occured : {err}')
except KeyboardInterrupt:
    print('Keyboard Interrupted')
finally:
    motor.off()
    print('Finished..')