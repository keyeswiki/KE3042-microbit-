from microbit import *
pin2.write_digital(0)
pin9.write_digital(0)

while True:
    if pin0.read_analog() > 400:
        pin9.write_digital(1)
        pin2.write_digital(1)
        display.show(Image.CONFUSED)
        sleep(1000)

    else:
        pin2.write_digital(0)
        pin9.write_digital(0)
        display.show(Image.HAPPY)
