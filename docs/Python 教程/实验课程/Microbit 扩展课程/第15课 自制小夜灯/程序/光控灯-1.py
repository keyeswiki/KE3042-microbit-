from microbit import *

display.show(Image.HAPPY)

while True:
    val = pin2.read_analog()
    print("value:", val)
    sleep(100)
