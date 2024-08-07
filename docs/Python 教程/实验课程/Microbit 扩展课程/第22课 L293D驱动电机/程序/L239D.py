from microbit import *

display.show(Image.HAPPY)
while True:
    pin0.write_analog(800)
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(2000)
    pin0.write_analog(0)
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(1000)
    pin0.write_analog(800)
    pin1.write_digital(0)
    pin2.write_digital(1)
    sleep(2000)
