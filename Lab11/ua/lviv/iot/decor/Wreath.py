from ua.lviv.iot.decor.Decoration import *
from enum import *


class MaterialOfWreath(Enum):
    branches = "branches"
    cones = "cones"
    tapes = "tapes"


class Wreath(Decoration):
    def __init__(self, decoration_place, type_of_decoration, color, material_of_wreath, radius):
        super().__init__(decoration_place, type_of_decoration, color)
        self.material_of_wreath = material_of_wreath
        self.radius = radius

    def __str__(self):
        return Decoration.__str__(self) + "material of wreath " + str(self.material_of_wreath) + ", radius " + \
               str(self.radius)
