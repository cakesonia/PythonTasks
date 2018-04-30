from ua.lviv.iot.decor.Garland import *
from ua.lviv.iot.decor.Lighting import *
from ua.lviv.iot.decor.Toys import *
from ua.lviv.iot.decor.Wreath import *


class Manager:
    decoration_list = []

    def find_by_decoration_place(self, decoration_place):
        founded_decorations = []

        for decoration in self.decoration_list:
            if decoration.decoration_place == decoration_place:
                founded_decorations.append(decoration)
        return founded_decorations

    def sort_by_type_of_decoration(self):
        self.decoration_list.sort(key=lambda decoration: decoration.type_of_decoration)
        return self.decoration_list

    @staticmethod
    def print_list(printed_list):
        for decoration in printed_list:
            print(decoration)
        print("\n")


if __name__ == "__main__":
    garland = Garland("house", TypeOfDecorations.garland.value, Color.blue.value, 15)
    toys = Toys("house", TypeOfDecorations.toys.value, Color.green.value, MaterialOfToys.glass.value,
                TypeOfToys.angels.value)
    wreath = Wreath("house", TypeOfDecorations.wreath.value, Color.yellow.value, MaterialOfWreath.branches.value, 10)
    lighting = Lighting("house", TypeOfDecorations.lighting.value, Color.red.value, 20)

    manager = Manager()
    manager.decoration_list = [garland, toys, wreath, lighting]
    manager.print_list(manager.decoration_list)
    manager.decoration_list = manager.find_by_decoration_place("house")
    manager.print_list(manager.decoration_list)
    manager.decoration_list = manager.sort_by_type_of_decoration()
    manager.print_list(manager.decoration_list)
