# -*- coding: utf-8 -*-

"""This script parses culture related data
Folders to check:
/history/provinces
"""
from os import listdir, path
import time, re, json

def read_culture_colours():

    colours = {}

    f = open("00_cultures.txt")
    graph_re = re.compile('graphical')
    curly_re = re.compile('\s}')
    color_re = re.compile('color');

    for line in f:
        tabs = len(line) - len(line.lstrip('\t'))
        colour = None
        if tabs == 1 and not re.search(graph_re, line) and not re.match(curly_re, line):
            tmp = line.split(' = ')
            culture = tmp[0].strip()

        if tabs == 2 and re.search(color_re, line):
            tmp = line.split(' = ')
            s = tmp[1].strip()
            s = s.strip('{} ')
            cl = s.split(' ')
            colour = "rgb("
            colour = colour + str((int(255 * float(cl[0]))))
            colour = colour + "," + str((int(255 * float(cl[1]))))
            colour = colour + "," + str((int(255 * float(cl[2])))) + ")"
            print colour

        if colour is not None:
            colours[culture] = colour

    with open('cultures.js', 'w') as f:
        f.write("var culture_colours = ") 
        json.dump(colours, f, separators=(',',':'))

def read_cultures_from_provinces():
    date_re = re.compile('\Aculture')

    cultures = {}

    for prov in listdir("history/provinces"):
        prov_id = int((prov.split(' '))[0])
        provp = path.join("history/provinces", prov)

        f = open(provp)

        culture = None
        for line in f:
            if re.search(date_re, line):
                tmp = line.split(' = ')
                tmp = tmp[1].split('#')
                culture = tmp[0].strip()
                break

        if culture is not None:
            cultures[prov_id] = culture

    with open('cultures.js', 'a') as f:
        f.write(";var cultures = ") 
        json.dump(cultures, f, separators=(',',':'))

def generate():
    read_culture_colours()
    read_cultures_from_provinces()

if __name__ == "__main__":
    start = time.clock()
    generate()
    delta = time.clock() - start
    print ("Generating cultures.js took %.3f seconds" %delta)
