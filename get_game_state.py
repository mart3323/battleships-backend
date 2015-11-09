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
try:
    board1, board2 = misc.get_boards(gameID)
except:
    board1, board2 = False, False


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


validated_player_id = misc.validate_player(game, name, hash)
if validated_player_id == 1:
    misc.succeed("Game state loaded", game=game.to_personalized_dict(1), your_board=board1, opponent_board=obscure(board2))
elif validated_player_id == 2:
    misc.succeed("Game state loaded", game=game.to_personalized_dict(2), your_board=board2, opponent_board=obscure(board1))
else:
    misc.fail("Invalid name, hash, or gameID")

