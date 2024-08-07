'''
电子时钟-2
keyes
https://www.keyesrobot.cn/

'''
from microbit import *
import TM1637
import DS1302
import time
display.off()

tm = TM1637.TM1637(clk=pin1, dio=pin2)
display.off()
clk = pin13
dio = pin14
cs = pin15

ds = DS1302.DS1302(clk, dio, cs)
while True:
    tm.brightness(7)
    tm.numbers(ds.hour(), ds.minute(), True)
    time.sleep(0.5)
    tm.numbers(ds.hour(), ds.minute(), False)
    time.sleep(0.5)
