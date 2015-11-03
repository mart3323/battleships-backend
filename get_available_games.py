#!/usr/bin/python

import cgitb
import misc
cgitb.enable()


games = misc.load_games()
games = [game.to_dict() for game in games if game.game_state is "W"]


for game in games:
    del game["player_1_hash"]
    del game["player_2_hash"]


misc.succeed("Fetched {0} games".format(len(games)), games=games)
