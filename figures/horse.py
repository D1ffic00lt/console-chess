from figures.figure import Figure


class Horse(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.possible_moves = []

    def check_move(self, to_x, to_y, desk):
        if self.position == (to_x, to_y):
            return False
        if (0 > to_x > 8) or (0 > to_y > 8):
            print(1)
            return False
        if desk.get_figure((to_x, to_y)).color == self.color:
            return False
        self.possible_moves = [
            (self.x - 1, self.y + 2),
            (self.x - 2, self.y + 1),
            (self.x - 2, self.y - 1),
            (self.x - 1, self.y - 2),
            (self.x + 1, self.y - 2),
            (self.x + 2, self.y - 1),
            (self.x + 2, self.y + 1),
            (self.x + 1, self.y - 2),
        ]
        if (to_x, to_y) not in self.possible_moves:
            return False
        return True

    def __str__(self):
        return self.color + "H"
