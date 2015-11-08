#!/usr/bin/python

import cgitb
import json
from operator import itemgetter
import os
import cgi
from datetime import datetime, timedelta

cgitb.enable()
# Ensure working directory is in this folder
trim = "/".join(__file__.split("/")[0:-1])
os.chdir(trim)

fields = cgi.FormContentDict() #Something weird was happening with FieldStorage.., it was claiming to not be indexable
#fields = cgi.FieldStorage()

UNIX_EPOCH = datetime(year=1970, month=1, day=1)

# startTime, name, score1, score2, winner, time
with open("scores.txt", "r") as scores_file:
    data = scores_file.read().replace("\x00", "").split("\n")
    data = [p.split(" ") for p in data if p != ""]


for item in data:
    item[0] = int(item[0])
    item[2] = int(item[2])
    item[3] = int(item[3])
    item[4] = item[4] == "True"
    item[5] = float(item[5])


sorting = fields["sorting"][0] if "sorting" in fields else None
name = fields["name"][0] if "name" in fields else None

if sorting == "name":
    data.sort(key=itemgetter(1))
elif sorting == "score1":
    data.sort(key=itemgetter(2), reverse=True)
elif sorting == "score2":
    data.sort(key=itemgetter(3), reverse=True)
elif sorting == "winner":
    data.sort(key=itemgetter(4))
elif sorting == "time":
    data.sort(key=itemgetter(5), reverse=True)
else:
    data.sort(key=itemgetter(0), reverse=True)

if name is not None:
    data = filter(lambda x: name in x[1], data)

data = data[:10]

to_print = []
for item in data:
    to_print.append(dict(
        date=str(UNIX_EPOCH+timedelta(seconds=item[0])),
        name=item[1],
        player_shots=item[2],
        opponent_shots=item[3],
        winner=item[4],
        time=item[5]
    ))

print("Content-type: application/json\n")
print(json.dumps(to_print))
