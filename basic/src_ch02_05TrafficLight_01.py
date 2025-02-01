from gpiozero import TrafficLights
from time import sleep

light = TrafficLights(17, 27, 22)

while True:
    light.red.on()
    sleep(1)
    light.red.off()
    sleep(0.5)

    light.amber.on()
    sleep(1)
    light.amber.off()
    sleep(0.5)

    light.green.on()
    sleep(1)
    light.green.off()
    sleep(0.5)