#!/usr/bin/python

import cgitb
import cgi
from datetime import datetime

import misc
from misc import board_checker
cgitb.enable()

def make_board(board_size, ships):
    board = [[misc.EMPTY for _ in range(board_size)] for __ in range(board_size)]
    for i, v in enumerate(ships):
        y = i // game.board_size
        x = i % game.board_size
        if v == "2":
            board[y][x] *= misc.SHIP
    return board

fields = cgi.FieldStorage()

name, hash, gameID, ships = (fields.getvalue("name",None),
                             fields.getvalue("hash",None),
                             fields.getvalue("gameID",None),
                             fields.getvalue("ships",None))

if None in {name, hash, gameID, ships}:
    misc.fail("Missing parameters, one of (name, hash, gameID, ships}")

games = misc.load_games()
game = misc.find_game(games, gameID)
player = misc.validate_player(game, name, hash)

if player is None:
    misc.fail("Invalid name/hash/gameID")

board = make_board(game.board_size, ships)


board_checker.check(board, game)
past_layout_phase = game.game_state != "L" and game.game_state != "W"
waiting_for_opponent_only = player == 1 and game.waiting_for == 2 or game.waiting_for == 1 and player == 2
if waiting_for_opponent_only or past_layout_phase:
    misc.fail("You have already submitted your board")


if player == game.waiting_for:
    misc.save_board(game.gameID, board, player)
    game.game_state = "G"
    game.started_at = misc.get_unix_timestamp()
    game.waiting_for = 1
if game.waiting_for == 3:
    misc.save_board(game.gameID, board, player)
    if player == 1:
        game.waiting_for = 2
    elif player == 2:
        game.waiting_for = 1

misc.save_games(games)

misc.succeed("Saved board")

