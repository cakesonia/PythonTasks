from enum import Enum


class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value

        return NotImplemented


class TypeOfDecoration(OrderedEnum):
    garland = 1
    wreath = 2
    lighting = 3
    toys = 4


class Color(Enum):
    blue = 1
    green = 2
    red = 3
    yellow = 4


class Decoration:
    decoration_place = ""
    type_of_decoration = None
    color = None

    def to_string(self):
        return "Decoration place " + str(self.decoration_place) + ", type of decoration " + str(self.type_of_decoration) \
               + ", color " + str(self.color)
