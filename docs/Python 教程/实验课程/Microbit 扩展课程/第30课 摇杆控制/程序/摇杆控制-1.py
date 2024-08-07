from microbit import *

display.show(Image.HAPPY)

while True:
    X = pin0.read_analog()
    Y = pin1.read_analog()
    B = pin2.read_digital()
    print("X:", X)
    print("Y:", Y)
    print("B:", B)
    sleep(100)
