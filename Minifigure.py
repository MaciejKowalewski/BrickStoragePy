from Root import Root


class Minifigure(Root):
    def __init__(self, name, number, price, quantity, blink, imglink, parts: list):
        super().__init__(name, number, price, quantity, blink, imglink)
        self._parts = parts

    @property
    def parts(self):
        return self._parts

    @parts.setter
    def parts(self, np):
        self._parts = np
