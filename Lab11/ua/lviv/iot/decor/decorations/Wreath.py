from ua.lviv.iot.decor.decorations.Decoration import *
from enum import Enum


class MaterialOfWreath(Enum):
    branches = 1
    cones = 2
    tapes = 3


class Wreath(Decoration):
    type_of_decoration = TypeOfDecoration.wreath
    decoration_place = "House"

    def __init__(self, radius):
        self.material_of_wreath = MaterialOfWreath.branches
        self.radius = radius
        self.color = Color.green

    def to_string(self):
        return Decoration.to_string(self) + ", material of wreath " + str(self.material_of_wreath) + ", radius " + str(
            self.radius)
