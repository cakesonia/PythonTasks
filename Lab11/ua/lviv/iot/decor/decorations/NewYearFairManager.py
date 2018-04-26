from ua.lviv.iot.decor import decorations
from ua.lviv.iot.decor.decorations.Garland import *
from ua.lviv.iot.decor.decorations.Toys import *
from ua.lviv.iot.decor.decorations.Wreath import *
from ua.lviv.iot.decor.decorations.Lighting import *


class NewYearFairManager:
    decorations = []

    def __init__(self):
        pass

    def sort_by_decoration_type(self):
        self.decorations.sort(key=lambda x: x.type_of_decoration)

    def find_by_decoration_place(self, decoration_place):
        founded_decorations = []

        for decoration in self.decorations:
            if decoration.decoration_place == decoration_place:
                founded_decorations.append(decoration)
        return founded_decorations

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def print_list(self):
        for decoration in self.decorations:
            print(decoration.to_string())
        print("\n")


if __name__ == '__main__':
    manager = NewYearFairManager()

    garland = Garland(25)
    lighting = Lighting(15)
    wreath = Wreath(10)
    toys = Toys()

    manager.decorations = [garland, lighting, wreath, toys]
    manager.print_list()
    manager.decorations = manager.find_by_decoration_place("House")
    manager.print_list()
    manager.decorations = manager.sort_by_decoration_type()

    manager.print_list()
    pass
