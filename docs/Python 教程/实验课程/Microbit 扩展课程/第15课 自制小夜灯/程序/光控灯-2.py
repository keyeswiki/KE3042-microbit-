from microbit import *
display.show(Image.HAPPY)

pin1.write_digital(0)

while True:
    if pin2.read_analog() > 500:
        pin1.write_digital(1)

    else:
        pin1.write_digital(0)
