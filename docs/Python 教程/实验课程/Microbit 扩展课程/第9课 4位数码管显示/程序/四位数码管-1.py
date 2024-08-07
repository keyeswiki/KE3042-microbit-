'''
TM1637四位数码管
keyes
https://www.keyesrobot.cn/

'''
from microbit import *
import TM1637
import time
display.off()

tm = TM1637.TM1637(clk=pin1, dio=pin2)
while True:
    tm.brightness(7)
    tm.show('1234', False)
    time.sleep(2)
    tm.show('ABCD')
    time.sleep(2)
    tm.numbers(88, 88, True)
    time.sleep(2)
    tm.temperature(-9)
    time.sleep(2)
    tm.write([0, 0, 0, 0])
    time.sleep(2)
