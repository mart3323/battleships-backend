#!/usr/bin/python

import cgitb

cgitb.enable()

print("Content-type: text\n")

with open("data/index.txt", "r") as file:
    for line in file:
        print(line)
