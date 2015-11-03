#!/usr/bin/python

import cgitb
import cgi

import misc
cgitb.enable()


fields = cgi.FieldStorage()

name = fields.getvalue("name")
hash = fields.getvalue("hash")
gameID = fields.getvalue("gameID")

if None in {name, hash, gameID}:
    misc.fail("Missing parameters, one of (name, hash, gameID")

games = misc.load_games()
found = misc.find_game(games, gameID)

if found is None:
    misc.fail("No game by that ID found")
if found.player_1 == name and found.player_1_hash == hash:
    found.game_state = "X-1"
elif found.player_2 == name and found.player_2_hash == hash:
    found.game_state = "X-2"
else:
    misc.fail("name or hash incorrect for given game")

misc.save_games(games)
misc.succeed("Left game")



