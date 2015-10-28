#!/usr/bin/python

import cgitb
import cgi

import misc
from misc.Game import Game
cgitb.enable()


fields = cgi.FieldStorage()

name = fields.getvalue("name")
hash = fields.getvalue("hash")
num_ships = fields.getvalue("num_ships")
board_size = fields.getvalue("board_size")

try:
    num_ships = int(num_ships)
    board_size = int(board_size)
except ValueError:
    misc.fail("Required parameters board_size and num_ships must be integers")

if None in {name, hash, num_ships, board_size}:
    misc.fail("Missing parameters, one of (name, hash, num_ships, board_size")

if not 3 <= board_size <= 10 or not 1 <= num_ships < board_size:
    misc.fail("Invalid parameters, board_size must be between 3 and 10, "
              "num_ships must be at least 1 and less than board_size")

games = misc.load_games()

id = games[-1].gameID+1 if len(games) > 0 else 1
new_game = Game(dict(
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
misc.save_games(games)
data = new_game.to_dict()
del data["player_2_hash"]

misc.succeed("Game created", **data)



