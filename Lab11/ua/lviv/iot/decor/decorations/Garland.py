from ua.lviv.iot.decor.decorations.Decoration import *


class Garland(Decoration):
    type_of_decoration = TypeOfDecoration.garland
    decoration_place = "House"

    def __init__(self, length):
        self.length = length
        self.color = Color.blue

    def to_string(self):
        return Decoration.to_string(self) + ", length " + str(self.length)
