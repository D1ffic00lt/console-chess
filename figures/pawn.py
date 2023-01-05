from figures.figure import Figure
from figures.empty import Empty


class Pawn(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.first = True
        self.possible_moves = []

    def check_move(self, to_x, to_y, desk):
        print(to_x, to_y)
        if desk.get_figure((to_x, to_y)).color == self.color:
            return False
        return True
        # elif self.x + 1 == to_x and self.y + 1 == to_y:
        #     if not isinstance(desk[to_x][to_y], Empty):
        #         return True
        #     print(6)
        #     return False
        # elif self.x - 1 == to_x and self.y + 1 == to_y:
        #     if not isinstance(desk[to_x][to_y], Empty):
        #         return True
        #     print(7)
        #     return False
        # else:
        #     if isinstance(desk[to_x][to_y], Empty):
        #         return True
        #     print(8)
        #     return False

    def __str__(self):
        return self.color + "P"
