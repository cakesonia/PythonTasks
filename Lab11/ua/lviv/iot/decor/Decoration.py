from enum import *


class Color(Enum):
    blue = "blue"
    green = "green"
    yellow = "yellow"
    red = "red"


class TypeOfDecorations(Enum):
    garland = "garland"
    wreath = "wreath"
    toys = "toys"
    lighting = "lighting"


class Decoration:

    def __init__(self, decoration_place, type_of_decoration, color):
        self.decoration_place = decoration_place
        self.type_of_decoration = type_of_decoration
        self.color = color

    def __str__(self):
        return "Type of decorations " + str(self.type_of_decoration) + ", decoration place " + \
               str(self.decoration_place) + ", color " + str(self.color) + ", "
