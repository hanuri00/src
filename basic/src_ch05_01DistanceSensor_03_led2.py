from gpiozero import DistanceSensor, LED
from time import sleep

#snr = DistanceSensor(echo=21, trigger=20)
ultra = DistanceSensor(23, 24)
led1 = LED(17)
led2 = LED(27)

led1.off()
led2.off()

i=0

while True:
    i+=1
    dis = ultra.distance * 100
    print(f'{i}.Distance : {dis} cm')
    sleep(0.5)

    if dis>30 or dis <0:
        led1.on()
        led2.off()
    elif dis <=30 or dis >0:
        led1.off()
        led2.on()
    else:
        led1.off()
        led2.off()

