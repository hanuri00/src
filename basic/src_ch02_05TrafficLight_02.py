from gpiozero import TrafficLights
from time import sleep

light = TrafficLights(17, 27, 22)

def traffic_light():
    
    yield (0, 0, 1)
    sleep(10)
    yield (0, 1, 0)
    sleep(1)
    yield (1, 0, 0)
    sleep(10)
    yield (1, 1, 0)
    sleep(1)
    
light.source = traffic_light