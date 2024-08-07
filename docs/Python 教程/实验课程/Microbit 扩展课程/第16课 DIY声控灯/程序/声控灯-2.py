from microbit import *
display.show(Image.HAPPY)

pin2.write_digital(0)

while True:
    if pin0.read_analog() > 300:
        pin2.write_digital(1)
        sleep(1000)

    else:
        pin2.write_digital(0)
