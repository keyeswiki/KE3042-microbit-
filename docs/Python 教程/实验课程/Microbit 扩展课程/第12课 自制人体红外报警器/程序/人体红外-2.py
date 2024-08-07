from microbit import *

display.show(Image.HAPPY)

pin2.write_digital(0)

while True:
    if pin1.read_digital() == 1:

        pin2.write_digital(1)

    else:
        pin2.write_digital(0)
