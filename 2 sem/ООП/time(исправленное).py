class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def show(self):
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        self.hours = self.hours % 24
        h = self.hours
        m = self.minutes
        if self.hours < 10:
            h = f'0{self.hours}'
        if self.minutes < 10:
            m = f'0{self.minutes}'
        print(f'{h}:{m}')


    def isMorning(self):
        if self.hours in range(4, 12):
            return True

    def isDay(self):
        if self.hours in range(12, 17):
            return True

    def isEvening(self):
        if self.hours in range(17, 23):
            return True

    def isNight(self):
        if self.hours in (23, 0, 1, 2, 3):
            return True

    def sayHello(self):
        if self.isMorning():
            print('Good morning!')
        elif self.isDay():
            print('Good afternoon!')
        elif self.isEvening():
            print('Good evening!')
        elif self.isNight():
            print('Good night!')

    def addTime(self, minute):
        self.minutes += minute



day = Time(0, 0)
day.sayHello()
day.show()
day.addTime(460)
day.show()
