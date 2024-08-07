'''
综合实验
keyes
https://www.keyesrobot.cn/

'''
from microbit import *
import machine
import LCD1602
import TM1637
import DS1302
import time

clk = pin13
dio = pin14
cs = pin15

tm = TM1637.TM1637(clk=pin1, dio=pin2)
ds = DS1302.DS1302(clk, dio, cs)
val = LCD1602.LCD1602()
display.off()
n = 0

class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_analog(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

Servo(pin10).write_angle(0)
while True:
    # 时钟
    tm.brightness(7)
    tm.numbers(ds.hour(), ds.minute(), True)
    time.sleep(0.5)
    tm.numbers(ds.hour(), ds.minute(), False)
    time.sleep(0.5)

    # 超声波
    val.puts(str(n), 0, 1)
    pin9.write_digital(0)
    sleep(0.002)
    pin9.write_digital(1)
    sleep(0.015)
    pin9.write_digital(0)

    t = machine.time_pulse_us(pin8, 1, 35000)
    if (t <= 0 and lastEchoDuration >= 0) :
        t = lastEchoDuration
    else:
        lastEchoDuration = t

    distance = int(t * 0.017)
    val.clear()
    val.puts(str(distance), 0, 0)
    val.puts("cm", 3, 0)

    # 声音传感器
    val.puts("val:", 7, 0)
    val.puts(str(pin0.read_analog()), 11, 0)

    # 人体红外控制舵机
    if pin16.read_digital() == 1:

        Servo(pin10).write_angle(65)

        val.puts("Someone", 0, 1)

    else:
        Servo(pin10).write_angle(0)
        val.puts("unmanned", 0, 1)
