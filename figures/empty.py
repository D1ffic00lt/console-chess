from figures.figure import Figure


class Empty(Figure):
    def __init__(self, x, y, color=None):
        super().__init__(x, y, color)

    def __str__(self):
        return "--"
