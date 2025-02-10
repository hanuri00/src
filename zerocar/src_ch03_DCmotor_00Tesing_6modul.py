from zeroCar import rightWheel, leftWheel
from time import sleep

try:
    while True:
        #go
        print('go!!!!!')
        rightWheel.forward()
        leftWheel.forward()
        sleep(2)

        #back
        print('back!!!!!')
        rightWheel.backward()
        leftWheel.backward()
        sleep(2)

        #left turnning
        print('left turnning')
        rightWheel.forward()
        leftWheel.backward()
        sleep(2)

        #right turnning
        print('right turnning')
        rightWheel.backward()
        leftWheel.forward()
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