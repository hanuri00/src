from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(17, 27, 22, 13, 19)

while True:
    leds.on()
    sleep(1)
    leds.off()
    sleep(1)

    leds.value=(1, 0, 0, 0, 0)
    sleep(0.5)
    leds.value=(0, 1, 0, 0, 0)
    sleep(0.5)
    leds.value=(0, 0, 1, 0, 0)
    sleep(0.5)
    leds.value=(0, 0, 0, 1, 0)
    sleep(0.5)
    leds.value=(0, 0, 0, 0, 1)
    sleep(0.5)

    leds.off()
    sleep(1)