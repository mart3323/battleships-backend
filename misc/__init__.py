import json
import Game


def load_games():
    with open("data/index", "r") as index_file:
        lines = [line for line in index_file.readlines() if not(line.replace(" ","") == "" or line.replace(" ","")[0] is "#")]
    return [Game.Game(Game.parse(line)) for line in lines]


def save_games(games_list):
    lines = [Game.stringify(**game.to_dict()) for game in games_list]
    with open("data/index", "wb") as index_file:
        index_file.write("\n".join([Game.stringify(**x.to_dict()) for x in games_list]))
        index_file.write("\n")


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
