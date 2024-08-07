from microbit import *

pin8.write_digital(0)
pin9.write_digital(0)

while True:
    if pin0.read_digital() == 1 and pin2.read_digital() == 1:

        pin9.write_digital(0)
        pin8.write_digital(1)

    elif pin2.read_digital() == 0 and pin2.read_digital() == 0:
        pin9.write_digital(1)
        pin8.write_digital(0)
