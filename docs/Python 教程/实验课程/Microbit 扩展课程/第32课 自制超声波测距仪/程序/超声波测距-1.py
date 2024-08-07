from microbit import *
import ustruct
import machine
from time import sleep_us, ticks_us
distance = 0

while True:
    pin2.write_digital(0)
    sleep_us(2)
    pin2.write_digital(1)
    sleep_us(15)
    pin2.write_digital(0)

    t = machine.time_pulse_us(pin1, 1, 35000)
    if (t <= 0 and lastEchoDuration >= 0) :
        t = lastEchoDuration
    else:
        lastEchoDuration = t
    distance = int(t * 0.017)
    print("distance:", distance, 'cm')
    sleep(0.3)

