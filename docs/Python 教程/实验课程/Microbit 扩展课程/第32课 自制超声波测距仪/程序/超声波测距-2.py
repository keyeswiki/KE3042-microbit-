from microbit import *
import ustruct
import machine
from time import sleep_us, ticks_us
distance = 0
LCD_I2C_ADDR = 0x27

class LCD1602():
    def __init__(self):
        self.buf = bytearray(1)
        self.BK = 0x08
        self.RS = 0x00
        self.E = 0x04
        self.setcmd(0x33)
        sleep(5)
        self.send(0x30)
        sleep(5)
        self.send(0x20)
        sleep(5)
        self.setcmd(0x28)
        self.setcmd(0x0C)
        self.setcmd(0x06)
        self.setcmd(0x01)
        self.version = '1.0'

    def setReg(self, dat):
        self.buf[0] = dat
        i2c.write(LCD_I2C_ADDR, self.buf)
        sleep(1)

    def send(self, dat):
        d = dat & 0xF0
        d |= self.BK
        d |= self.RS
        self.setReg(d)
        self.setReg(d | 0x04)
        self.setReg(d)

    def setcmd(self, cmd):
        self.RS = 0
        self.send(cmd)
        self.send(cmd << 4)

    def setdat(self, dat):
        self.RS = 1
        self.send(dat)
        self.send(dat << 4)

    def clear(self):
        self.setcmd(1)

    def backlight(self, on):
        if on:
            self.BK = 0x08
        else:
            self.BK = 0
        self.setcmd(0)

    def on(self):
        self.setcmd(0x0C)

    def off(self):
        self.setcmd(0x08)

    def shl(self):
        self.setcmd(0x18)

    def shr(self):
        self.setcmd(0x1C)

    def char(self, ch, x=-1, y=0):
        if x >= 0:
            a = 0x80
            if y > 0:
                a = 0xC0
            a += x
            self.setcmd(a)
        self.setdat(ch)

    def puts(self, s, x=0, y=0):
        if len(s) > 0:
            self.char(ord(s[0]), x , y)
            for i in range(1, len(s)):
                self.char(ord(s[i]))

display.show(Image.HAPPY)
val = LCD1602()
n = 0

while True:
    val.puts(str(n), 0, 1)
    pin2.write_digital(0)
    sleep_us(2)
    pin2.write_digital(1)
    sleep_us(15)
    pin2.write_digital(0)

    t = machine.time_pulse_us(pin1, 1, 35000)
    if (t <= 0 and lastEchoDuration >= 0) :
        t = lastEchoDuration
    else:
        lastEchoDuration = t
    distance = int(t * 0.017)
    print("distance:", distance, 'cm')
    val.puts("    keyes")
    val.puts(str(distance), 0, 1)
    val.puts("cm", 3, 1)
    sleep(600)
    val.clear()

