#!/usr/bin/python
print("Content-type: text/html")
print("")

import cgitb
cgitb.enable()
import cgi
from obsoleteClasses.Score import Score, RecentScores



form = cgi.FieldStorage()

if all(x in form for x in ["win", "shots", "opponent_shots", "time", "board_size", "num_ships"]):
    winner = form.getValue("win")
    your_shots = int(form.getValue("shots"))
    opponent_shots = int(form.getValue('opponent_shots'))
    time = float(form.getValue('time'))
    board_size = int(form.getValue('board_size'))
    num_ships = int(form.getValue('num_ships'))

    recScores = None
    with open("data/lastScores.txt", "r+") as file1:
        recScores = RecentScores.load(file1.read().splitlines())

    recScores.add(Score(board_size, num_ships, winner, your_shots, opponent_shots, time))

    with open("data/lastScores.txt", "w+") as file2:
        recScores.write_to(file2)

else:
    print("<span style='border:2px outset red; color:red'>Error while saving, required fields not specified</span>")

