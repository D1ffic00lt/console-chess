from figures.empty import Empty
from figures.figure import Figure


class Elephant(Figure):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.possible_moves = []
        self.n = True
        self.w = True
        self.e = True
        self.s = True

    def check_move(self, to_x, to_y, desk):
        if self.x == to_x and self.y == to_y:
            return False
        if (0 > to_x > 8) or (0 > to_y > 8):
            return False
        if desk.get_figure((to_x, to_y)).color == self.color:
            return False
        self.possible_moves = []
        self.set_true()
        for i in range(1, 8):
            if self.n:
                print(self.x + i, self.y + i)
                if (0 > self.x + i or self.x + i >= 8) or (0 > self.y + i or self.y + i >= 8):
                    self.n = False
                elif isinstance(desk.get_figure((self.x + i, self.y + i)), Empty):
                    self.possible_moves.append((self.x + i, self.y + i))
            if self.s:
                print(self.x - i, self.y - i)
                if (0 > self.x - i or self.x - i >= 8) or (0 > self.y - i or self.y - i >= 8):
                    self.s = False
                elif isinstance(desk.get_figure((self.x - i, self.y - i)), Empty):
                    self.possible_moves.append((self.x - i, self.y - i))
            if self.e:
                print(self.x - i, self.y + i)
                if (0 > self.x - i or self.x - i >= 8) or (0 > self.y + i or self.y + i >= 8):
                    self.e = False
                elif isinstance(desk.get_figure((self.x - i, self.y + i)), Empty):
                    self.possible_moves.append((self.x - i, self.y + i))
            if self.w:
                print(self.x + i, self.y - i)
                if (0 > self.x + i or self.x + i >= 8) or (0 > self.y - i or self.y - i >= 8):
                    self.w = False
                elif isinstance(desk.get_figure((self.x + i, self.y - i)), Empty):
                    self.possible_moves.append((self.x + i, self.y - i))
        print(self.possible_moves)
        if (to_x, to_y) not in self.possible_moves:
            print(3)
            return False
        return True

    def set_true(self):
        self.n = True
        self.w = True
        self.e = True
        self.s = True

    def __str__(self):
        return self.color + "E"
