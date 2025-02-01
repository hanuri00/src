from gpiozero import DistanceSensor
from time import sleep

#ultra = DistanceSensor(echo=23, trigger=24)
ultra = DistanceSensor(23, 24)

while True:
    print(f'Distance : {ultra.distance:.8f} m')
    sleep(1)