from ua.lviv.iot.decor.Decoration import *


class Lighting(Decoration):
    def __init__(self, decoration_place, type_of_decoration, color, length):
        super().__init__(decoration_place, type_of_decoration, color)
        self.length = length

    def __str__(self):
        return Decoration.__str__(self) + str(self.length)
