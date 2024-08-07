from microbit import *

display.show(Image.HAPPY)
while True:
    X = pin0.read_analog()
    Y = pin1.read_analog()
    B = pin2.read_digital()
    print("X:", X)
    print("Y:", Y)
    print("B:", B)
    if 0 < X < 500:
        pin13.write_analog(800)
        pin14.write_digital(1)
        pin15.write_digital(0)
        sleep(2000)

    elif 550 < X < 1024:
        pin13.write_analog(800)
        pin14.write_digital(0)
        pin15.write_digital(1)
        sleep(2000)

    elif B == 1:
        pin13.write_analog(0)
        pin14.write_digital(0)
        pin15.write_digital(0)

    else:
        pin13.write_analog(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
