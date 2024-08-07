from microbit import *
display.show(Image.HAPPY)

pin2.write_digital(0)
vla = 0
while True:
    val = pin0.read_analog()/4
    pin2.write_analog(val)
