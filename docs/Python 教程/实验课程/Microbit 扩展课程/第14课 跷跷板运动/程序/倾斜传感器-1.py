from microbit import *
val = 0
display.show(Image.HAPPY)
while True:
    val = pin0.read_digital()

    print("digital signals:", val)

    sleep(200)
