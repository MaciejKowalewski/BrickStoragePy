from Root import Root


class Part(Root):
    def __init__(self, name, number, price, quantity, blink, imglink, part_type: str, color: str):
        super().__init__(name, number, price, quantity, blink, imglink)
        self._color = color
        self._type = part_type

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color: str):
        self._color = new_color

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type: str):
        self._type = new_type
