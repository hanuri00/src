from gpiozero import DistanceSensor
from time import sleep

#snr = DistanceSensor(echo=21, trigger=20)
ultra = DistanceSensor(23, 24)


while True:
    print(f'Distance : {ultra.distance:.8f} m')
    sleep(1)

