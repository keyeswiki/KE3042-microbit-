"""
红外遥控-1
keyes
https://www.keyesrobot.cn/

"""
from machine import time_pulse_us
from microbit import *
display.off()
class IRremote():
    def __init__(self, pin):
        self.pin = pin
        self.pin.set_pull(self.pin.PULL_UP)

    def getIR(self):
        vlist = []
        while True:
            x = time_pulse_us(self.pin, 1, 100000)
            if x >= 0:
                vlist.append(x)
            if x == -1 and len(vlist) > 3:
                return self.unlock(vlist)

    def unlock(self, vlist):
        start = 0
        addr = 0
        cmd = 0

        # 截取有效信号
        for i in range(len(vlist)):
            if vlist[i] > 3000 and vlist[i] < 5000 and vlist[i + 1] < 2000:
                start = i + 1
        if (start + 31) > len(vlist):
            return -1
        vlist = vlist[start : start + 32]
        # print(vlist)
        # 转码
        for i in range(16):
            if vlist[i] > 1000:
                addr = addr + 2**i
            if vlist[i + 16] > 1000:
                cmd = cmd + 2**i
        # return [bin(addr),bin(cmd)]
        return [hex(addr), hex(cmd)]

ir = IRremote(pin16)
while True:
    r = ir.getIR()
    if r != -1:
        print("CMD=", r[1])   # [/i][/i][/i]
