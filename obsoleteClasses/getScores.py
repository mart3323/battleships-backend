#!/usr/bin/python
# coding=utf-8
#print("Content-type: application/json")
print("Content-type: text/html")
print("")

import cgitb
cgitb.enable()

from obsoleteClasses.Score import RecentScores

recScores = None
with open("data/lastScores.txt", "r") as file1:
    recScores = RecentScores.load(file1.read().splitlines())

print("[")
for score in recScores.scores:
    print("{")
    print("""
        board_size: {board_size},
        num_ships: {num_ships},
        winner: {winner},
        player_1_shots: {player_1_shots},
        player_2_shots: {player_2_shots},
        time: {time}
        """.format(
            board_size=score.board_size,
            num_ships=score.number_of_ships,
            winner=score.winner,
            player_1_shots=score.player_1_shots,
            player_2_shots=score.player_2_shots,
            time=score.time
        )
    )
    print("}")
print("]")
