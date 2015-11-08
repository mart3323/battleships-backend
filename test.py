#!/usr/bin/python
import os

def ensureWorkingDirectoryCorrect(file):
    trim = "/".join(file.split("/")[0:-1])
    os.chdir(trim)

