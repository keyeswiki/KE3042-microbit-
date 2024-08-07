"""
电子时钟-1
keyes
https://www.keyesrobot.cn/

"""
from microbit import *
import DS1302
import time

display.off()
clk = pin13
dio = pin14
cs = pin15

ds = DS1302.DS1302(clk, dio, cs)
# ds.date_time() # returns the current datetime.
# ds.date_time([2022, 3, 9, 4, 23, 0, 1, 0]) # set datetime.
# ds.hour() # returns hour.
# ds.second(10) # set second to 10.
while True:
    print(ds.year(), end="-")
    print(ds.month(), end="-")
    print(ds.day(), end=" ")
    print(ds.hour(), end=":")
    print(ds.minute(), end=":")
    print(ds.second(), end=" ")
    print(ds.weekday())
    time.sleep(1)
