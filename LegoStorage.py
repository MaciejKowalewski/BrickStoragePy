from Part import Part
from Minifigure import Minifigure
from Money import Money
import csv
import pathlib


class Storage:
    def __init__(self, name: str, purpose: int, content: int):
        purposes = {1: 'Private', 2: 'Wish list', 3: 'Store'}
        contents = {1: 'Parts', 2: 'Minifigures', 3: 'Sets'}
        self._name = name
        self._purpose = purposes[purpose]
        self._content = contents[content]
        self._collection = []

    def __str__(self):
        s = self._name + " | " + self._purpose + ' | ' + self._content + ' | ' + "theme" + ' | Liczba elementów: ' + str(
            self.total_quantity) + ' | Wartość listy: ' + self.storage_value.__str__()
        return s

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def collection(self):
        return self._collection

    @property
    def content(self):
        return self._content

    @property
    def storage_value(self):
        value = Money(0.0)
        for item in self._collection:
            value = value + Money(item.price).scalar(item.quantity)
        return value

    @property
    def total_quantity(self):
        quantity = 0
        for each in self._collection:
            quantity += each.quantity
        return quantity

    def add(self, item):
        item_exists = False
        el = ''
        if self._content == 'Parts':
            for each in self._collection:
                if item.id == each.id and item.color == each.color:
                    item_exists = True
                    el = each
            if item_exists:
                el.quantity += item.quantity
            else:
                self._collection.append(item)
        elif self._content == 'Minifigures':
            for each in self._collection:
                if item.id == each.id and item.name == each.name:
                    item_exists = True
                    el = each
            if item_exists:
                el.quantity += item.quantity
            else:
                self._collection.append(item)

    def del_item(self, index):
        self._collection.pop(index)

    def edit(self):
        pass

    def read(self):
        self._collection = []
        arr = []
        storage_csv = pathlib.Path('Storages/' + self._name + ".csv").open(newline='')
        CSVreader = csv.reader(storage_csv, delimiter=',')
        for item in CSVreader:
            arr.append(item)
        for each in arr[2:]:
            if self._content == "Parts":
                self._collection.append(
                    Part(each[0], each[1], float(each[2]), int(each[3]), each[4], each[5], each[6], each[7]))
            elif self._content == "Minifigures":
                parts_csv = pathlib.Path('Storages/' + self.name + '-' + each[1] + '-parts.csv').open(newline='')
                CSVreader = csv.reader(parts_csv, delimiter=',')
                list_of_parts = []
                for el in list(CSVreader)[2:]:
                    list_of_parts.append(Part(el[0], el[1], el[2], el[3], el[4], el[5], el[6], el[7]))
                self._collection.append(
                    Minifigure(each[0], each[1], float(each[2]), int(each[3]), each[4], each[5], list_of_parts))
        storage_csv.close()

    def save_parts(self, CSVwriter):
        CSVwriter.writerow(["Nazwa", "ID", "Cena", "Ilość", "Bricklink", "Img", "Typ", "Kolor"])
        for each in self._collection:
            CSVwriter.writerow(
                [each.name, each.id, each.price, each.quantity, each.blink, each.img, each.type, each.color])

    def save_minifigures(self, CSVwriter):
        CSVwriter.writerow(["Nazwa", "ID", "Cena", "Ilość", "Bricklink", "Img"])
        for each in self._collection:
            CSVwriter.writerow(
                [each.name, each.id, each.price, each.quantity, each.blink, each.img])
        for each in self._collection:
            filename = 'Storages/' + self._name + '-' + each.id + "-parts.csv"
            storage_csv = pathlib.Path(filename).open(mode="w+", newline="")
            CSVwriter = csv.writer(storage_csv, delimiter=",")
            CSVwriter.writerow(["sep=,"])
            CSVwriter.writerow(["Nazwa", "ID", "Cena", "Ilość", "Bricklink", "Img", "Typ", "Kolor"])
            for part in each.parts:
                CSVwriter.writerow(
                    [part.name, part.id, part.price, part.quantity, part.blink, part.img, part.type, part.color])

    def save_sets(self, CSVwriter):
        pass

    def save(self):
        filename = 'Storages/' + self._name + ".csv"
        storage_csv = pathlib.Path(filename).open(mode="w+", newline="")
        CSVwriter = csv.writer(storage_csv, delimiter=",")
        CSVwriter.writerow(["sep=,"])
        if self._content == "Parts":
            self.save_parts(CSVwriter)
        elif self._content == "Minifigures":
            self.save_minifigures(CSVwriter)
        elif self._content == "Sets":
            self.save_sets(CSVwriter)
        storage_csv.close()
