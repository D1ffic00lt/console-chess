from figures.figure import Figure


class Queen(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def check_move(self, to_x, to_y, desk):
        if (0 > to_x > 8) or (0 > to_y > 8):
            return False
        if desk.get_figure((to_x, to_y)).color == self.color:
            return False
        if (abs(self.x - to_x) == abs(self.y - to_y)) or \
                (((self.x != to_x) and (self.y == to_y)) or ((self.x == to_x) and (self.y != to_y))):
            return True
        return False

    def __str__(self):
        return self.color + "Q"
