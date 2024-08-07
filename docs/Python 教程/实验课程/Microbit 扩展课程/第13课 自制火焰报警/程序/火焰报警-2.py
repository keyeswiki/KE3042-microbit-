from microbit import *
import music
display.show(Image.HAPPY)
pin1.write_digital(0)
tune = ["E5:4", "C5:4"]
while True:
    if pin2.read_digital() == 1:

        pin1.write_digital(1)
        music.play(tune)

    else:
        pin1.write_digital(0)
        pin0.write_digital(0)
