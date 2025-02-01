import serial
from gpiozero import LED

led = LED(22)
bt = serial.Serial("/dev/ttyS0", baudrate=9600,timeout=1.0)
i=0

try:
    while True:
        i+=1
        data = bt.readline().decode('utf-8').strip()
        if data:
            try:
                if data=='1':
                    led.on()
                    print('led on!!')
                elif data=='0':
                    led.off()
                    print('led off!')
                else:
                    print('Invalid input')
            except ValueError:
                print('Invalid data received!!')
except KeyboardInterrupt:
    print('Keyboard Stopped')
finally:
    bt.close()
