from desk import Desk
from IPython.display import clear_output

color = "w"

if __name__ == "__main__":
    desk = Desk()
    while True:
        desk.show()
        pos_from, pos_to = input("input: ").split()
        pos_to = desk.refactor_position(pos_to)
        pos_from = desk.refactor_position(pos_from)
        if desk.check_self_figure(pos_from, color):
            if desk.get_figure(pos_from).check_move(*pos_to, desk):
                desk.do_move(pos_from, pos_to)
                clear_output()
                # color = "b" if color == "w" else "w"
            else:
                clear_output()
                print("NO")
        else:
            clear_output()
            print("NO!")

