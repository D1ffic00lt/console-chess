from figures.figure import Figure


class Rook(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def check_move(self, to_x, to_y, desk):
        if (0 > to_x > 8) or (0 > to_y > 8):
            return False
        if to_y != self.y and to_x != self.x:
            return False

    def __str__(self):
        return self.color + "R"
