#!/usr/bin/python

import cgitb, json
import misc
from misc import spec
cgitb.enable()


try:
    games = misc.load_games()

    for game in games:
        game.player_1_hash = "_"
        game.player_2_hash = "_"

    games = [game for game in games if game.player_2 is "_"]
    data = spec.getSuccessDict("Fetched {0} games".format(len(games)), games=[game.to_dict() for game in games])

    misc.start_success()
    print(json.dumps(data))
except Exception as e:
    misc.start_error()
    raise e
