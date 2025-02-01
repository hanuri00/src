from gpiozero import LEDBarGraph
from time import sleep

ledBar = LEDBarGraph(17, 27, 22, 13, 19)

while True:
    ledBar.value=0
    sleep(1)
    ledBar.value=1/4
    sleep(1)
    ledBar.value=1/2
    sleep(1)
    ledBar.value=1
    sleep(1)
    ledBar.value=-1
    sleep(1)
    ledBar.value=-1/2
    sleep(1)
    ledBar.value=-1/4
    sleep(1)

    ledBar.value=1/10
    sleep(1)
    ledBar.value=1/4
    sleep(1)
    ledBar.value=1/2
    sleep(1)
    ledBar.value=1
    sleep(1)   