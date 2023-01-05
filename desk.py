from typing import List, Any, Tuple

from figures import *


class Desk(object):
    def __init__(self):
        self.figure = None
        self.desk: list = self.get_clear_desk()
        self.figures = []
        self.all = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def do_move(self, from_position, to_position):
        self.figure = self.get_figure(from_position)
        self.desk[to_position[0]][to_position[1]] = self.figure
        self.desk[from_position[0]][from_position[1]] = Empty(*from_position)

    def refactor_position(self, position: str) -> Tuple[int, int]:
        if position[0] in self.all:
            return 8 - int(position[1]), self.all.index(position[0])
        return 8 - int(position[0]), self.all.index(position[1])

    def get_figure(self, position):
        return self.desk[position[0]][position[1]]

    def check_self_figure(self, position, color):
        if not isinstance(self.get_figure(position), Empty):
            if color == self.desk[position[0]][position[1]].color:
                return True
        return False

    def show(self):
        print("-------------------------------------")
        for x in range(len(self.desk)):
            print(f"{7 - x + 1}|\t", end="")
            for y in range(len(self.desk[0])):
                print(self.desk[x][y], sep="\t", end="\t")
            print("|")
        print("-------------------------------------")
        print(*["\ta", "b", "c", "d", "e", "f", "g", "h"], sep="\t")

    @staticmethod
    def get_clear_desk():
        desk_full: List[List[Any]] = []
        for y in range(8):
            desk_line = []
            for x in range(8):
                desk_line.append(Empty(y, x, "e"))
            desk_full.append(desk_line)
        for i in range(8):
            desk_full[1][i] = Pawn(1, i, "b")
            desk_full[6][i] = Pawn(6, i, "w")
        desk_full[0][1] = Horse(0, 1, "b")
        desk_full[0][6] = Horse(0, 6, "b")
        desk_full[7][1] = Horse(7, 1, "w")
        desk_full[7][6] = Horse(7, 6, "w")

        desk_full[0][2] = Elephant(0, 2, "b")
        desk_full[0][5] = Elephant(0, 5, "b")
        desk_full[7][2] = Elephant(7, 2, "w")
        desk_full[7][5] = Elephant(7, 5, "w")

        desk_full[0][0] = Rook(0, 0, "b")
        desk_full[0][7] = Rook(0, 7, "b")
        desk_full[7][0] = Rook(7, 0, "w")
        desk_full[7][7] = Rook(7, 7, "w")

        desk_full[0][3] = Queen(0, 3, "b")
        desk_full[7][3] = Queen(7, 3, "w")

        desk_full[0][4] = King(0, 4, "b")
        desk_full[7][4] = King(7, 4, "w")
        print(*desk_full, sep="\n")
        return desk_full
