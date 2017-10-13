from e_month import Month
import math


class Calendar:
    def __init__(self, year=100, month=Month.JANUARY, day=1, floatval=0.0):
        self.calendar = True

        if year < 0:
            year = 0
        elif month < 0 or month > 12:
            self.calendar = False
        elif day < 0 or day > self.getNumDays(month, year):
            self.calendar = False

        self.year = year
        if isinstance(month, int) and self.calendar:
            self.month = Month(month)
        self.month = month
        self.day = day
        if floatval < 0.0:
            floatval = 0.0
        self.floatval = floatval

        if floatval > 0.0:
            # override date with float value
            y = math.floor(floatval)
            self.year = int(y)
            r = floatval - y
            r *= 365.25
            d = int(math.floor(r))
            m = 1
            while d > self.getNumDays(m, self.year):
                d -= self.getNumDays(m, self.year)
                m += 1
            self.month = m
            self.day = d

    def __str__(self):
        return "%d/%d/%d" % (self.year, self.month, self.day)

    def __add__(self, date):
        year = self.year + date.year
        month = self.month + date.month
        while month > 12:
            year += 1
            month -= 12
        day = self.day + date.day
        while day > self.getNumDays(month, year):
            day -= self.getNumDays(month, year)
            month += 1
            if month > 12:
                year += 1
                month -= 12
        return Calendar(year, month, day)

    def getNumDays(self, month, year):
        daydist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and year % 4 == 0:
            return 29
        else:
            return daydist[month - 1]

    def increment(self):
        self.day += 1
        while self.day > self.getNumDays(self.month, self.year):
            self.day -= self.getNumDays(self.month, self.year)
            self.month += 1
            if self.month > 12:
                self.year += 1
                self.month -= 12

    def toFloat(self):
        y = self.year
        m = self.month
        d = self.day
        dd = 0.0
        tm = 1
        while tm < m:
            dd += self.getNumDays(tm, y)
            tm += 1
        fy = float(y)
        fd = float(d) + dd
        fd /= 365.25
        fy += fd
        return fy

    def getAge(self, now):
        if now.month > self.month:
            return now.year - self.year
        if now.month == self.month:
            if now.day >= self.day:
                return now.year - self.year
        return now.year - self.year - 1


if __name__ == '__main__':
    date = Calendar(4, 4, 4)
    date1 = Calendar(0, 0, 888)
    print(str(date))
    print(str(date1))
    date += date1
    print(str(date))
    date.increment()
    print(str(date))
    print(date.toFloat())
    date2 = Calendar(floatval=57.301)
    print(str(date2))
    print(date2.toFloat())
