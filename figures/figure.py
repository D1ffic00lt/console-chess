from typing import Tuple


class Figure(object):
    def __init__(self, x, y, color):
        self.position = (x, y)
        self.color = color
        # print(self.x, self.y)

    @property
    def x(self):
        return self.position[0]

    @x.setter
    def x(self, value: int):
        self.position = (value, self.position[0])

    @property
    def y(self):
        return self.position[1]

    @y.setter
    def y(self, value: int):
        self.position = (value, self.position[1])

    def __repr__(self):
        return f"{self.__module__}({self.x}, {self.y}, {self.color})"