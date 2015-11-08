#!/usr/bin/python

import cgitb
import os
import cgi
from datetime import datetime
cgitb.enable()

UNIX_EPOCH = datetime(year=1970, month=1, day=1)

fields = cgi.FieldStorage()

# Ensure working directory is in this folder
trim = "/".join(__file__.split("/")[0:-1])
os.chdir(trim)

name = fields.getvalue("name")
score1 = fields.getvalue("score1")
score2 = fields.getvalue("score2")
winner = fields.getvalue("winner") == "true"
time = fields.getvalue("time")

timestamp = int(round((datetime.now() - UNIX_EPOCH).total_seconds()))
# startTime, name, score1, score2, time
with open("scores.txt", "a") as scores_file:
    scores_file.write("{} {} {} {} {} {}".format(timestamp, name, score1, score2, winner, time)+"\n")
