from microbit import *
pin2.write_digital(0)
pin8.write_digital(0)
pin9.write_digital(0)

while True:
    if pin0.read_analog() < 400:
        pin9.write_digital(1)
        pin8.write_digital(0)
        pin2.write_digital(0)

    elif 400 < pin0.read_analog() < 700:
        pin9.write_digital(0)
        pin8.write_digital(1)
        pin2.write_digital(0)
    elif pin0.read_analog() > 700:
        pin9.write_digital(0)
        pin8.write_digital(0)
        pin2.write_digital(1)
