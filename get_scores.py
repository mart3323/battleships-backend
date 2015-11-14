#!/usr/bin/python
# coding=utf-8

import cgitb
import cgi
import misc

cgitb.enable()
fields = cgi.FieldStorage()
sort_by = fields.getvalue("sortby")
name = fields.getvalue("name")
reverse = fields.getvalue("reverse") == "true"

scores = misc.load_scores()

if name != "" and name != None and name != "false" and name != "undefined":
    scores = [score for score in scores if name.lower() in score.player_1.lower() or name.lower() in score.player_2.lower()]

if sort_by == "player_1":
    scores.sort(key=lambda x: x.player_1)
if sort_by == "player_2":
    scores.sort(key=lambda x: x.player_2)
if sort_by == "winner":
    scores.sort(key=lambda x: x.winner)
if sort_by == "player_1_shots":
    scores.sort(key=lambda x: x.player_1_shots)
if sort_by == "player_1_hits":
    scores.sort(key=lambda x: x.player_1_hits)
if sort_by == "player_2_shots":
    scores.sort(key=lambda x: x.player_2_shots)
if sort_by == "player_2_hits":
    scores.sort(key=lambda x: x.player_2_hits)
if sort_by == "time":
    scores.sort(key=lambda x: x.time)
if sort_by == "date":
    scores.sort(key=lambda x: x.date, reverse=True)

if reverse:
    scores.reverse()

for score in scores:
    score.date = score.date.replace("T"," ")

misc.succeed("Got scores", scores=[s.to_dict() for s in scores][0:10])
