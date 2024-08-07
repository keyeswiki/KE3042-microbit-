from microbit import *
def initialization():
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(0)
    pin8.write_digital(0)

def Fourturns():
    # 单四拍正转
    pin0.write_digital(1)
    pin8.write_digital(0)
    sleep(10)
    pin0.write_digital(0)
    pin1.write_digital(1)
    sleep(10)
    pin1.write_digital(0)
    pin2.write_digital(1)
    sleep(10)
    pin2.write_digital(0)
    pin8.write_digital(1)
    sleep(10)

def Fourantipodes():
    # 单四拍反转
    pin1.write_digital(1)
    pin8.write_digital(0)
    sleep(10)
    pin0.write_digital(0)
    pin2.write_digital(1)
    sleep(10)
    pin1.write_digital(0)
    pin8.write_digital(1)
    sleep(10)
    pin0.write_digital(0)
    pin2.write_digital(1)
    sleep(10)

def Bazheng():
    # 单八拍正转
    pin8.write_digital(0)
    sleep(10)
    pin1.write_digital(1)
    sleep(10)
    pin0.write_digital(0)
    sleep(10)
    pin2.write_digital(1)
    sleep(10)
    pin1.write_digital(0)
    sleep(10)
    pin8.write_digital(1)
    sleep(10)
    pin2.write_digital(0)
    sleep(10)

def Bafan():
    # 单八拍反转
    pin1.write_digital(0)
    sleep(10)
    pin8.write_digital(1)
    sleep(10)
    pin0.write_digital(0)
    sleep(10)
    pin2.write_digital(1)
    sleep(10)
    pin8.write_digital(0)
    sleep(10)
    pin1.write_digital(1)
    sleep(10)
    pin2.write_digital(0)
    sleep(10)
    pin0.write_digital(1)
    sleep(10)

val = 0
while True:
    initialization()
    sleep(500)
    for val in range(1, 100):
        Fourturns()
        sleep(10)

    for val in range(1, 100):
        Fourantipodes()
        sleep(10)

    for val in range(1, 100):
        Bazheng()
        sleep(30)

    for val in range(1, 100):
        Bafan()
        sleep(30)
