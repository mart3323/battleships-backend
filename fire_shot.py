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

if None in {name, hash, gameID, x, y}:
    misc.fail("Missing parameters, one of (name, hash, x, y}")

try:
    x = int(x)
    y = int(y)
except ValueError:
    misc.fail("coordinates must be integers")

games = misc.load_games()
game = misc.find_game(games, gameID)
player = misc.validate_player(game, name, hash)
opponent = 2 if player == 1 else 1
board = misc.get_boards(gameID)[opponent-1]

if player is None:
    misc.fail("Invalid name/hash/gameID")

if player == 1 and game.waiting_for != 1 \
or player == 2 and game.waiting_for != 2:
    misc.fail("It is not your turn")
if game.game_state != "G":
    misc.fail("The game is not in progress")

if board[y][x] % misc.SHOT == 0:
    misc.fail("You've already shot that square")

shot_was_hit = board[y][x]%misc.SHIP == 0

if not shot_was_hit:
    game.waiting_for = opponent

board[y][x] *= misc.SHOT

if misc.hasLost(board):
    misc.save_as_score(games, game)
    misc.succeed("You win!")
else:
    misc.save_board(game.gameID, board, opponent)
    misc.save_games(games)
    misc.succeed("Shot board")

