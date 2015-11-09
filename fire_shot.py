#!/usr/bin/python

import cgitb
import cgi

import misc

cgitb.enable()

fields = cgi.FieldStorage()

name, hash, gameID, x, y = (fields.getvalue("name"),
                            fields.getvalue("hash"),
                            fields.getvalue("gameID"),
                            fields.getvalue("x"),
                            fields.getvalue("y"))

if None in {name, hash, x, y}:
    misc.fail("Missing parameters, one of (name, hash, gameID, ships}")

try:
    x = int(x)
    y = int(y)
except ValueError:
    misc.fail("coordinates must be integers")

games = misc.load_games()
game = misc.find_game(games, gameID)
player = misc.validate_player(game, name, hash)
board1, board2 = misc.get_boards(gameID)

if player is None:
    misc.fail("Invalid name/hash/gameID")

if player == 1 and game.waiting_for != 1 \
or player == 2 and game.waiting_for != 2:
    misc.fail("The is not your turn")
if game.game_state != "G":
    misc.fail("The game is not in progress")
if player == game.waiting_for:
    if player == 1:
        board = board2
        game.waiting_for = 2
    else:
        board = board1
        game.waiting_for = 1

    if board[y][x] % misc.SHOT == 0:
        misc.fail("You've already shot that square")

    board[y][x] *= misc.SHOT
    misc.save_board(game.gameID, board, player)
    misc.save_games(games)
    misc.succeed("Shot board")

