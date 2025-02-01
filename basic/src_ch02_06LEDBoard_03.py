from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(17, 27, 22, 13, 19, pwm=True)

while True:
    leds.on()
    sleep(0.5)
    leds.off()
    sleep(0.5)

    leds.value = (1,0,0,0,0)
    sleep(0.5)
    leds.value = (0.8,1,0,0,0)
    sleep(0.5)
    leds.value = (0.6,0.8,1, 0, 0)
    sleep(0.5)
    leds.value = (0.4,0.6,0.8,1,0)
    sleep(0.5)
    leds.value = (0.2,0.4,0.6,0.8,1)
    sleep(0.5)

    leds.off()
    sleep(0.5)