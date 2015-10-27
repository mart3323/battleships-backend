#!/usr/bin/python

import cgitb
import json
import cgi

from misc import *
cgitb.enable()


try:
    fields = cgi.FieldStorage()
    name = fields.getvalue("name")
    hash = fields.getvalue("hash")
    num_ships = int(fields.getvalue("num_ships"))
    board_size = int(fields.getvalue("board_size"))

    if None in {name, hash, num_ships, board_size}:
        raise KeyError

    games = load_games()

    id = games[-1].gameID+1 if len(games) > 0 else 1
    new_game = Game.Game(dict(
        gameID=id,
        player_1 = name,
        player_1_hash = hash,
        player_2="_", player_2_hash="_",
        game_state = "W",
        waiting_for = 3,
        board_size=board_size,
        num_ships=num_ships,
        started_at=0
    ))

    games.append(new_game)
    save_games(games)
    data = new_game.to_dict()
    del data["player_2_hash"]

    start_success()
    print(json.dumps(data))
except KeyError as e:
    start_error()
    print("<h3>Missing fields, could not satisfy request</h3>")
except ValueError as e:
    start_error()
    print("<h3>Invalid fields</h3>")



