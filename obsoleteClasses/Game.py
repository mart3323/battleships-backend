# coding=utf-8
from Exceptions import GameNotFoundException

DATA_PATH = "data/"
GAMES_PATH = DATA_PATH + "games/"

TILE = type('Shot', (), {"EMPTY": 1, "SHIP": 2, "SHOT": 3})

class Game:
    def __init__(self, props):
        print(len(props))
        self.id, self.connected_p1, self.connected_p2, \
        self.mode, self.waiting_for, self.board_size, self.number_of_ships = props
        with open(GAMES_PATH + str(self.id)) as boards:
            data = boards.read()
        data = data.split("\n\n")
        self.board_1 = Board(data[0])
        self.board_2 = Board(data[1])


class Board:
    def __init__(self, grid):
        print("---")
        print(grid.replace(" ",".").replace("\n","↓"))
        self.grid = [[int(x) for x in x.split(" ")] for x in grid.split("\n") if x is not ""]

    def getProperty(self, x, y, prop):
        return (self.grid[y][x] / prop) % 1

    def addProperty(self, x, y, prop):
        self.grid[y][x] *= prop

    def __str__(self):
        s = ""
        for line in self.grid:
            s += " ".join(str(x) for x in line)+"\n"
        return s


def save_game(game):
    with open(GAMES_PATH + str(game.id),"w") as file:
        file.write(str(game.board_1))
        file.write("\n")
        file.write(str(game.board_2))


def open_game(id):
    wanted_line = None
    with open(DATA_PATH+"index", "r") as file:
        lines = file.readlines()
        wanted_line = next((x for x in lines if x[0] == str(id)))
    if wanted_line is None:
        raise GameNotFoundException()

    return Game(wanted_line.split(" "))


