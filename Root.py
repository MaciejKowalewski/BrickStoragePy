class Root:
    def __init__(self, name: str, number: str, price: float, quantity: int, blink: str, imglink: str):
        self._name = name
        self._id = number
        self._price = price
        self._quantity = quantity
        self._blink = blink
        self._imglink = imglink

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._name = new_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, q):
        self._quantity = q

    @property
    def blink(self):
        return self._blink

    @blink.setter
    def blink(self, new_blink):
        self._imglink = new_blink

    @property
    def img(self):
        return self._imglink

    @img.setter
    def img(self, new_img):
        self._imglink = new_img
