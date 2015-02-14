# -*- coding: utf-8 -*-

"""This script will output a JSON which contains information about holders of provinces.
Folders to check:
/history/provinces/
/history/characters/
/history/titles
"""
from os import listdir, path
import time, re, json

def read_provinces():
    date_re = re.compile('\Aculture')

    cultures = {}

    for prov in listdir("history/provinces"):
        prov_id = (prov.split(' '))[0]
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

    for key in cultures:
        print (key, cultures[key])

    with open('cultures.js', 'w') as f:
        json.dump(cultures, f)

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
    read_provinces()
    #read_characters()
    #read_titles()

    #Add them all together
    pass

if __name__ == "__main__":
    start = time.clock()
    generate()
    delta = time.clock() - start
    print ("Generating history took %.3f seconds" %delta)
