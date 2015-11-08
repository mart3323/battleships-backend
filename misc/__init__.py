import json
import random
import Game
import os

BOARDS_FILE = "data/boards/{0}{1}.txt"
INDEX_FILE = "data/index.txt"

EMPTY = 1
SHIP = 2
SHOT = 3
FOG = 5

# Set working directory to "../"
trim = "/".join(__file__.split("/")[0:-2])
os.chdir(trim)

def load_games():
    with open(INDEX_FILE, "r") as index_file:
        lines = [line for line in index_file.readlines() if not(
            line.replace(" ", "") == "" or
            line.replace(" ", "")[0] is "#")]
    return [Game.Game(Game.parse(line)) for line in lines]


def find_game(games, gameID):
    for game in games:
        if str(game.gameID) == str(gameID):
            return game


def save_games(games_list):
    lines = [Game.stringify(**game.to_dict()) for game in games_list]
    with open(INDEX_FILE, "wb") as index_file:
        index_file.write("\n".join([Game.stringify(**x.to_dict()) for x in games_list]))
        index_file.write("\n")


def get_boards(gameID):
    with open(BOARDS_FILE.format(gameID, 1), "r") as file:
        board1 = file.read().split("\n")
    with open(BOARDS_FILE.format(gameID, 2), "r") as file:
        board2 = file.read().split("\n")
    board1 = [[int(x) for x in line.split(" ")] for line in board1]
    board2 = [[int(x) for x in line.split(" ")] for line in board2]
    return board1, board2


def save_board(gameID, board, index):
    board = [[str(cell) for cell in line] for line in board]
    with open(BOARDS_FILE.format(gameID, index), "w") as file:
        file.write("\n\n".join([
            "\n".join([" ".join(line) for line in board]),
        ]))


def succeed(message, **data):
    d = dict()
    d["message"] = message
    d["data"] = data
    print("Content-type: application/json\n")
    print(json.dumps(d))


def fail(message):
    print("Status:403 Forbidden\n")
    print("Content-type: application/json\n")
    print('{{"reason":{message}}}'.format(message=message))
    exit()


def validate_player(game, name, hash):
    if name == game.player_1 and hash == game.player_1_hash:
        return 1
    if name == game.player_2 and hash == game.player_2_hash:
        return 2
    return None

def make_hash():
    hashchars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    length = 8
    return "".join([random.choice(hashchars) for _ in range(length)])