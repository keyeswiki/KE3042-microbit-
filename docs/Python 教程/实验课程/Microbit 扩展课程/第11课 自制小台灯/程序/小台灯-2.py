from microbit import *

display.show(Image.HAPPY)

pin2.write_digital(0)
State = 0
while True:
    if pin0.read_digital() == 1 :
        sleep(50)

        if pin0.read_digital() == 1 and State == 0 :
            pin2.write_digital(1)
            State = 1

        elif pin0.read_digital() == 1 and State == 1 :
            pin2.write_digital(0)
            State = 0
