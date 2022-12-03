from math import gcd


class Rational:

    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator
        self.reduce()

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not (isinstance(value, int)):
            raise TypeError("Wrong value type")
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not (isinstance(value, int)):
            raise TypeError("Wrong value type")
        if not value:
            raise ZeroDivisionError("Denominator cant be Zero")
        self.__denominator = value

    def floated(self):
        return self.numerator / self.denominator

    def reduce(self):
        k = gcd(self.numerator, self.denominator)
        self.numerator //= k
        self.denominator //= k
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            new_num, new_denom = self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator
        elif isinstance(other, int):
            new_num, new_denom = self.numerator + other * self.denominator, self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        return Rational(new_num, new_denom)

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_num, new_denom = self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator
        elif isinstance(other, int):
            new_num, new_denom = self.numerator - other * self.denominator, self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        return Rational(new_num, new_denom)

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_num, new_denom = self.numerator * other.numerator, self.denominator * other.denominator
        elif isinstance(other, int):
            new_num = self.numerator * other
            new_denom = self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        return Rational(new_num, new_denom)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            new_num, new_denom = self.numerator * other.denominator, self.denominator * other.numerator
        elif isinstance(other, int):
            new_num = self.numerator
            new_denom = self.denominator * other
        else:
            raise TypeError("Should be Rational or Integer")
        return Rational(new_num, new_denom)

    def __eq__(self, other) -> bool:
        if isinstance(other, Rational):
            return self.numerator * other.denominator == other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator == other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __ne__(self, other) -> bool:
        if isinstance(other, Rational):
            return self.numerator * other.denominator != other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator != other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __lt__(self, other) -> bool:
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __gt__(self, other) -> bool:
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator > other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __le__(self, other) -> bool:
        if isinstance(other, Rational):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator <= other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __ge__(self, other) -> bool:
        if isinstance(other, Rational):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator >= other * self.denominator
        else:
            raise TypeError("Wrong type, should be Rational or int")

    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            self.numerator, self.denominator = self.numerator + other * self.denominator, self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        self.reduce()
        return self

    def __isub__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            self.denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            self.numerator, self.denominator = self.numerator - other * self.denominator, self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        self.reduce()
        return self

    def __imul__(self, other):
        if isinstance(other, Rational):
            self.numerator, self.denominator = self.numerator * other.numerator, self.denominator * other.denominator
        elif isinstance(other, int):
            self.numerator = self.numerator * other
            self.denominator = self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        self.reduce()
        return self

    def __itruediv__(self, other):
        if isinstance(other, Rational):
            self.numerator, self.denominator = self.numerator * other.denominator, self.denominator * other.numerator
        elif isinstance(other, int):
            self.numerator = self.numerator * other
            self.denominator = self.denominator
        else:
            raise TypeError("Should be Rational or Integer")
        self.reduce()
        return self


if __name__ == "__main__":
    x = Rational(7, 6)
    y = Rational(3, 5)

    x += y
    print(x)

    x -= y
    print(x)

    print("Z:")
    z = x + y
    print(z)

    z = x - y
    print(z)

    z = x * y
    print(z)

    z = x / y
    print(z)

    z = y + 1
    print(z)

    z = y - 1
    print(z)

    z = y * 2
    print(z)

    z = y / 2
    print(z)

    print("СРАВНЕНИЯ")
    print(f"{x == y = }")
    print(f"{x != y = }")
    print(f"{x > y = }")
    print(f"{x < y = }")
    print(f"{x >= y = }")
    print(f"{x <= y = }")

    print("СРАВНЕНИЯ")
    print(f"{x == 1 = }")
    print(f"{x != 1 = }")
    print(f"{x > 1 = }")
    print(f"{x < 1 = }")
    print(f"{x >= 1 = }")
    print(f"{x <= 1 = }")