from ua.lviv.iot.decor.decorations.Decoration import *


class Lighting(Decoration):
    type_of_decoration = TypeOfDecoration.lighting
    decoration_place = "Yard"

    def __init__(self, length):
        self.length = length
        self.color = Color.yellow

    def to_string(self):
        return Decoration.to_string(self) + ", length " + str(self.length)
