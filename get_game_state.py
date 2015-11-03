#!/usr/bin/python

import cgitb
import cgi
import misc

cgitb.enable()

fields = cgi.FieldStorage()

name, hash, gameID = (fields.getvalue("name"),
                      fields.getvalue("hash"),
                      fields.getvalue("gameID"))
if None in {name, hash, gameID}:
    misc.fail("Missing fields, one of (name, hash, gameID)")

game = misc.find_game(misc.load_games(), gameID)
board1, board2 = misc.get_boards(gameID)


dct = game.to_dict()


def obscureCell(cell):
    if cell % misc.SHOT == 0:
        return cell
    return misc.FOG


def obscure(board2):
    return [
        [obscureCell(cell) for cell in line]
        for line in board2
    ]


if name == game.player_1 and hash == game.player_1_hash:
    del dct["player_2_hash"]
    misc.succeed("Game state loaded", game=dct, your_board=board1, opponent_board=obscure(board2))
elif name == game.player_2 and hash == game.player_2_hash:
    del dct["player_1_hash"]
    misc.succeed("Game state loaded", game=dct, your_board=board2, opponent_board=obscure(board1))
else:
    misc.fail("Invalid name, hash, or gameID")

