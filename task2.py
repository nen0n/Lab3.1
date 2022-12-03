MAX_MONTH_IN_YEAR = 12


class Calendar:
    days_in_months = (29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, day, month, year) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong value type")
        if not 0 < value <= self.days_in_months[self.define_month()]:
            raise ValueError("Wrong day value")
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong value type")
        if not 0 < value <= MAX_MONTH_IN_YEAR:
            raise ValueError("Can`t be less than zero or more than 12")
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong value type")
        if value < 0:
            raise ValueError("Can`t be less than zero or more than 12")
        self.__year = value

    def isleap(self):
        """Return True for leap years, False for non-leap years."""
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def define_month(self):
        """Returns current month number

        Returns 0 if it is February in Leap year"""
        return self.month if not (self.isleap() and self.month == 2) else 0

    def add_months(self, value):
        """Increases the number of month by the specified value

        Also changes the year, if needed"""
        if not isinstance(value, int):
            raise TypeError("Wrong type, should be int")
        self.year += value // MAX_MONTH_IN_YEAR
        value = value % MAX_MONTH_IN_YEAR
        if MAX_MONTH_IN_YEAR - self.month < value:
            self.year += 1
            self.month = value - (MAX_MONTH_IN_YEAR - self.month)
        else:
            self.month += value

    def add_days(self, value):
        """Increases the number of days by the specified value

        Also changes the month, if needed"""
        if not isinstance(value, int):
            raise TypeError("Wrong type, should be int")

        if (self.days_in_months[self.define_month()] - self.day) < 0:
            self.day = self.days_in_months[self.define_month()]

        while value >= self.days_in_months[self.define_month()] - self.day + 1:
            value -= self.days_in_months[self.define_month()] - self.day + 1
            self.day = 1
            self.add_months(1)
        self.day += value

    def __iadd__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Operations with Calendar only allowed")
        self.year += other.year
        self.add_months(other.month)
        self.add_days(other.day)
        return self

    def sub_months(self, value):
        """Increases the number of month by the specified value

        Also changes the year, if needed"""
        if not isinstance(value, int):
            raise TypeError("Wrong type, should be int")
        self.year -= value // MAX_MONTH_IN_YEAR
        value = value % MAX_MONTH_IN_YEAR
        if self.month <= value:
            self.year -= 1
            self.month = MAX_MONTH_IN_YEAR - (value - self.month)
        else:
            self.month -= value

    def sub_days(self, value):
        """Decreases the number of days by the specified value

        Also changes the month, if needed"""
        if not isinstance(value, int):
            raise TypeError("Wrong type, should be int")

        if (self.days_in_months[self.define_month()] - self.day) < 0:
            self.day = self.days_in_months[self.define_month()]

        while value >= self.day:
            value -= self.day
            self.sub_months(1)
            self.day = self.days_in_months[self.month if not (self.isleap() and self.month == 2) else 0]
        self.day -= value

    def __isub__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("Operations with Calendar only allowed")
        self.year -= other.year
        self.sub_months(other.month)
        self.sub_days(other.day)
        return self

    def __eq__(self, other) -> bool:
        if not isinstance(other, Calendar):
            raise TypeError("Comparing with Calendar only allowed")
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __ne__(self, other) -> bool:
        if not isinstance(other, Calendar):
            raise TypeError("Comparing with Calendar only allowed")
        return self.year != other.year or self.month != other.month or self.day != other.day

    def __lt__(self, other) -> bool:
        if not isinstance(other, Calendar):
            raise TypeError("Comparing with Calendar only allowed")
        if not self.year == other.year:
            return self.year < other.year
        if not self.month == other.month:
            return self.month < other.month
        if not self.day == other.day:
            return self.day < other.day
        return False

    def __gt__(self, other) -> bool:
        if not isinstance(other, Calendar):
            raise TypeError("Comparing with Calendar only allowed")
        if not self.year == other.year:
            return self.year > other.year
        if not self.month == other.month:
            return self.month > other.month
        if not self.day == other.day:
            return self.day > other.day
        return False

    def __le__(self, other) -> bool:
        if not isinstance(other, Calendar):
            raise TypeError("Comparing with Calendar only allowed")
        if not self.year == other.year:
            return self.year < other.year
        if not self.month == other.month:
            return self.month < other.month
        if not self.day == other.day:
            return self.day < other.day
        return True

    def __ge__(self, other) -> bool:
        if not isinstance(other, Calendar):
            raise TypeError("Comparing with Calendar only allowed")
        if not self.year == other.year:
            return self.year > other.year
        if not self.month == other.month:
            return self.month > other.month
        if not self.day == other.day:
            return self.day > other.day
        return True


if __name__ == "__main__":
    x = Calendar(1, 1, 2025)
    y = Calendar(1, 2, 3)

    x += y
    print(x)

    for i in range(10):
        x -= y
        print(x)

    print(f"{x == y = }")
    print(f"{x != y = }")
    print(f"{x > y = }")
    print(f"{x < y = }")
    print(f"{x >= y = }")
    print(f"{x <= y = }")