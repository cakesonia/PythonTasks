from ua.lviv.iot.decor.decorations.Decoration import *
from enum import Enum


class MaterialOfToys(Enum):
    glass = 1
    textile = 2
    paper = 3


class TypeOfToys(Enum):
    round = 1
    animals = 2
    angels = 3
    stars = 4


class Toys(Decoration):
    type_of_decoration = TypeOfDecoration.toys
    decoration_place = "Xmas Tree"

    def __init__(self):
        self.color = Color.red
        self.material_of_toys = MaterialOfToys.glass
        self.type_of_toys = TypeOfToys.angels

    def to_string(self):
        return Decoration.to_string(self) + ", material of toys " + str(self.material_of_toys) + ", type of toys " + str(
            self.type_of_toys)
