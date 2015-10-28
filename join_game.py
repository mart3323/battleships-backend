#!/usr/bin/python

import cgitb
import json
import cgi

import misc

cgitb.enable()


fields = cgi.FieldStorage()
gameID = int(fields.getvalue("gameID"))
hash = fields.getvalue("hash")
name = fields.getvalue("name")

games = misc.load_games()

found = None
for game in games:
    if game.gameID == gameID:
        found = game
        break

if None in {gameID, hash, name}:
    misc.fail("Missing parameter, one of gameID, hash, name")
if found is None:
    misc.fail("No game with that ID found")
if found.game_state != "W":
    misc.fail("That game is no longer open")

found.player_2 = name
found.player_2_hash = hash
found.game_state = "L"

del found.player_1_hash
misc.save_games(games)

misc.succeed("Joined game", game=found.to_dict())
