import serial
from time import sleep

#port = '/dev/ttyS0'
port = '/dev/serial0'
baudrate = 9600

bt = serial.Serial(port, baudrate)

try:
    while True:
        #data sending
        msg = 'Hello.. from pi4...'
        bt.write(msg.encode())
        print(f'Send : {msg}')

        #data receive
        received = bt.readline().decode().strip()
        print(f'Received : {received}')

        sleep(1)
    
except Exception as err:
    print(f'An Erro occured : {err}')
except KeyboardInterrupt:
    print('Keyboard Interrupted')
finally:
    bt.close()
    print('Finished..')
