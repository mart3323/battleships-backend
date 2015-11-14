#!/usr/bin/python

import cgitb
import cgi
import misc

def obscureCell(cell):
    if cell % misc.SHOT == 0:
        return cell
    return misc.FOG


def obscure(board2):
    return [
        [obscureCell(cell) for cell in line]
        for line in board2
        ]

cgitb.enable()

fields = cgi.FieldStorage()

name, hash, gameID = (fields.getvalue("name"),
                      fields.getvalue("hash"),
                      fields.getvalue("gameID"))
if None in {name, hash, gameID}:
    misc.fail("Missing fields, one of (name, hash, gameID)")

game = misc.find_game(misc.load_games(), gameID)
if game is None:
    misc.fail("No game found")
validated_player_id = misc.validate_player(game, name, hash)
try:
    board1, board2 = misc.get_boards(gameID)
    your_board = board1 if validated_player_id == 1 else board2
    opponent_board = obscure(board2 if validated_player_id == 1 else board1)
except:
    your_board, opponent_board = [[]], [[]]

misc.succeed("Game state loaded", game=game.to_personalized_dict(validated_player_id), your_board=your_board, opponent_board=opponent_board, validated_player_id=validated_player_id)

