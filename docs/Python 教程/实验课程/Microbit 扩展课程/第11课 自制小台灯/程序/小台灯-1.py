from microbit import *
while True:
    if pin0.is_touched():
        display.show(0)
        pin2.write_digital(0)
    else:
        display.show(1)
        pin2.write_digital(1)
