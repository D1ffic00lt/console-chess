from typing import Tuple


class Figure(object):
    def __init__(self, x, y, color):
        self.position = (x, y)
        self.color = color

    @property
    def x(self):
        return self.position[0]

    @x.setter
    def x(self, value: int):
        self.position = (value, self.position[1])

    @x.deleter
    def x(self):
        self.position = (-1, -1)

    @property
    def y(self):
        return self.position[0]

    @y.setter
    def y(self, value: int):
        self.position = (value, self.position[1])

    @y.deleter
    def y(self):
        self.position = (-1, -1)
