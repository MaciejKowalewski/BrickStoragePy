import math


class Money:
    def __init__(self, cash: float, currency="PLN"):
        self._cash = cash
        self._currency = currency

    def __str__(self):
        return str(self._cash) + " " + self._currency

    @property
    def value(self):
        return self._cash

    def scalar(self, s):
        return Money(self.value * float(s))

    def digits_after_decimal(self):
        return len(str(self._cash).split('.')[1])

    def __add__(self, other):
        digits = max(self.digits_after_decimal(), other.digits_after_decimal())
        s1 = int(round(self.value * math.pow(10, digits)))
        s2 = int(round(other.value * math.pow(10, digits)))
        return Money((s1 + s2) / math.pow(10, digits), self._currency)
