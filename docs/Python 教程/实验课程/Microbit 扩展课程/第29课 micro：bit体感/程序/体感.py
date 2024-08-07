from microbit import *
from random import randint
redVal = randint(0, 255)
greenVal = 0
blueVal = 0

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "up":
        display.show("1")
        redVal = randint(0, 255)
        blueVal = 0
        greenVal = 0
        pin2.write_analog(redVal)
        pin1.write_analog(greenVal)

    if gesture == "down":
        display.show("2")
        redval = 0
        blueVal = randint(0, 255)
        greenVal = 0
        pin2.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin0.write_analog(blueVal)

    if gesture == "face up":
        display.show("3")
        redval = 0
        blueVal = 0
        greenVal = randint(0, 255)
        pin2.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin0.write_analog(blueVal)
    if gesture == "face down":
        display.show("4")
        redval = randint(0, 255)
        blueVal = randint(0, 255)
        greenVal = 0
        pin2.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin0.write_analog(blueVal)

    if gesture == "left":
        display.show("5")
        redval = randint(0, 255)
        blueVal = 0
        greenVal = randint(0, 255)
        pin2.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin0.write_analog(blueVal)
