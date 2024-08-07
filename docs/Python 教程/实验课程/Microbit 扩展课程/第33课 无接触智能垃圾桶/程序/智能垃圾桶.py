'''
智能垃圾桶
keyes
https://www.keyesrobot.cn/

'''
from microbit import *
import machine
import LCD1602

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

while True:
    # 超声波
    val.puts(str(n), 0, 1)
    pin1.write_digital(0)
    sleep(0.002)
    pin1.write_digital(1)
    sleep(0.015)
    pin1.write_digital(0)

    t = machine.time_pulse_us(pin2, 1, 35000)
    if (t <= 0 and lastEchoDuration >= 0) :
        t = lastEchoDuration
    else:
        lastEchoDuration = t

    distance = int(t * 0.017)
    val.puts("    keyes")
    val.puts(str(distance), 0, 1)
    val.puts("cm", 3, 1)

    if distance <= 15 :
        Servo(pin12).write_angle(90)
        sleep(5000)

    else:
        Servo(pin12).write_angle(0)

    sleep(600)
    val.clear()
