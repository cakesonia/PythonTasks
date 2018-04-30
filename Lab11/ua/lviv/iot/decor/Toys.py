from ua.lviv.iot.decor.Decoration import *
from enum import *


class TypeOfToys(Enum):
    round = "round"
    animals = "animals"
    angels = "angels"
    stars = "stars"


class MaterialOfToys(Enum):
    glass = "glass"
    textile = "textile"
    paper = "paper"


class Toys(Decoration):
    def __init__(self, decoration_place, type_of_decoration, color, type_of_toys, material_of_toys):
        super().__init__(decoration_place, type_of_decoration, color)
        self.material_of_toys = material_of_toys
        self.type_of_toys = type_of_toys

    def __str__(self):
        return Decoration.__str__(self) + "material of toys " + str(self.material_of_toys) + ", type of toys " + \
               str(self.type_of_toys)
