from Root import Root


class Set(Root):
    def __init__(self, name, number, price, quantity, blink, imglink, theme: str, year: int, mylist: str, parts: list, year_of_purchase: int):
        super().__init__(name, number, price, quantity, blink, imglink)
        self._theme = theme
        self._year = year
        self._mylist = mylist
        self._parts = parts
        self._year_of_purchase = year_of_purchase

    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, t):
        self._theme = t

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, y):
        self._year = y

    @property
    def mylist(self):
        return self._mylist

    @mylist.setter
    def mylist(self, ml):
        self._mylist = ml

    @property
    def parts(self):
        return self._parts

    @parts.setter
    def parts(self, p):
        self._parts = p

    @property
    def year_of_purchase(self):
        return self._year_of_purchase

    @year_of_purchase.setter
    def year_of_purchase(self, yop):
        self._year_of_purchase = yop
