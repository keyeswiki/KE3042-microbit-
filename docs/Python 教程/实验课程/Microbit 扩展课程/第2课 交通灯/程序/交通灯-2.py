from microbit import *
while True:
    pin9.write_digital(1)
    sleep(5000)
    pin9.write_digital(0)
    for index in range(3):
        sleep(500)
        pin9.write_digital(1)
        sleep(500)
        pin9.write_digital(0)
    sleep(500)
    pin2.write_digital(1)
    sleep(5000)
    pin2.write_digital(0)
