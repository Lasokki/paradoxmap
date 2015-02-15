# -*- coding: utf-8 -*-

"""This script will parse data from history files
Folders to check:
/history/characters/
/history/titles
"""
from os import listdir, path
import time, re, json

def read_characters():
    pass

def read_titles():
    
    date_re = re.compile('\d{3}.\d{2}.\d{2}')

    for title in listdir("history/titles"):
        derp = path.join("history/titles", title)

        try:
            f = open(derp)
            for line in f:
                if re.search(date_re, line):
                    print(line)
        except UnicodeDecodeError:
            f = open(derp, encoding="utf-8")
            for line in f:
                if re.search(date_re, line):
                    print(line)


def generate():
    #Collect data
    #read_characters()
    #read_titles()
    pass

if __name__ == "__main__":
    start = time.clock()
    generate()
    delta = time.clock() - start
    print ("Generating history took %.3f seconds" %delta)
