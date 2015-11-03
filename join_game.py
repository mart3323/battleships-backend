#!/usr/bin/python

import cgitb
import cgi
import misc
cgitb.enable()


fields = cgi.FieldStorage()
gameID = fields.getvalue("gameID")
hash = misc.make_hash()
name = fields.getvalue("name")

games = misc.load_games()
found = misc.find_game(games, gameID)

if None in {gameID, hash, name}:
    misc.fail("Missing parameter, one of gameID, hash, name")
if found is None:
    misc.fail("No game with that ID found")
if found.game_state != "W":
    misc.fail("That game is no longer open")

found.player_2 = name
found.player_2_hash = hash
found.game_state = "L"

misc.save_games(games)

game = found.to_dict()
del game["player_1_hash"]
misc.succeed("Joined game", **game)
