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
        if (0 > to_x > 8) or (0 > to_y > 8):
            return False
        if desk.get_figure((to_x, to_y)).color == self.color:
            return False
        self.possible_moves = []
        self.set_true()
        for i in range(1, 8):
            print(self.x + i, self.y + i)
            if self.n:
                if (0 > self.x + i or self.x + i >= 8) or (0 > self.y + i or self.y + i >= 8):
                    self.n = False
                elif isinstance(desk.desk[self.x + i][self.y + i], Empty):
                    self.possible_moves.append((self.x + i, self.y + i))
                elif desk.desk[self.x + i][self.y + i].color == self.color:
                    self.n = False
                else:
                    self.possible_moves.append((self.x + i, self.y + i))
                    self.n = False
            if self.s:
                if (0 > self.x + i or self.x + i >= 8) or (0 > self.y - i or self.y - i >= 8):
                    self.s = False
                elif isinstance(desk.desk[self.x + i][self.y - i], Empty):
                    self.possible_moves.append((self.x + i, self.y - i))
                elif desk.desk[self.x + i][self.y - i].color == self.color:
                    self.s = False
                else:
                    self.possible_moves.append((self.x + i, self.y - i))
                    self.s = False
            if self.e:
                if (0 > self.x - i or self.x - i >= 8) or (0 > self.y - i or self.y - i >= 8):
                    self.e = False
                elif isinstance(desk.desk[self.x - i][self.y - i], Empty):
                    self.possible_moves.append((self.x - i, self.y - i))
                elif desk.desk[self.x - i][self.y - i].color == self.color:
                    self.e = False
                else:
                    self.possible_moves.append((self.x - i, self.y - i))
                    self.e = False
            if self.w:
                if (0 > self.x - i or self.x - i >= 8) or (0 > self.y + i or self.y + i >= 8):
                    self.w = False
                elif isinstance(desk.desk[self.x - i][self.y + i], Empty):
                    self.possible_moves.append((self.x - i, self.y + i))
                elif desk.desk[self.x - i][self.y + i].color == self.color:
                    self.w = False
                else:
                    self.possible_moves.append((self.x - i, self.y + i))
                    self.w = False
        if (to_x, to_y) not in self.possible_moves:
            return False
        return True

    def set_true(self):
        self.n = True
        self.w = True
        self.e = True
        self.s = True

    def __str__(self):
        return self.color + "E"
