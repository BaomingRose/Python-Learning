import time


class MyClock:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0
            self.minute = 0
            self.second = 0

    def display(self):
        print('当前时间为：%d时%d分%d秒' % (self.hour, self.minute, self.second))


if __name__ == '__main__':
    clock = MyClock(14, 51, 30)
    clock.display()
    while 1:
        time.sleep(1)
        clock.run()
        clock.display()
