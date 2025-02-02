import serial

port = '/dev/ttyS0'
#port = '/dev/serial0'
baudrate = 9600
timeout=1.0

bleSerial = serial.Serial(port, baudrate)

try:
    while True:
        data = bleSerial.read()
        print(data)

except Exception as err:
    print(f'An Erro occured : {err}')
except KeyboardInterrupt:
    print('Keyboard Interrupted')
finally:
    bleSerial.close()
    print('Finished..')