# -*- coding: utf-8 -*-

"""This script parses culture related data
Folders to check:
/history/provinces
"""
from os import listdir, path
import time, re, json

def read_colours():
    start = time.clock()

    colours = find_colours("00_cultures.txt")

    f = open('cultures_and_religions.js', 'w')
    f.write("var culture_colours = ") 
    json.dump(colours, f, separators=(',',':'))

    colours = find_colours("00_religions.txt")

    f.write(";var religion_colours = ") 
    json.dump(colours, f, separators=(',',':'))

    f.close()

    delta = time.clock() - start
    print ("Colour parsing took %.3f seconds" %delta)

def find_colours(txt):

    colours = {}
    f = open(txt)
    skip = re.compile('graphical|_names|ai_|has_|playable|hostile|crusade|Names|\s}')
    color_re = re.compile('color')

    for line in f:
        tabs = len(line) - len(line.lstrip('\t'))
        colour = None

        if tabs == 1 and not re.search(skip, line):
            tmp = line.split(' = ')
            key = tmp[0].strip()

        if tabs == 2 and re.search(color_re, line):
            tmp = line.split(' = ')
            s = tmp[1].strip()
            s = s.strip('{} ')
            cl = s.split(' ')
            colour = "rgb("
            colour = colour + str((int(255 * float(cl[0]))))
            colour = colour + "," + str((int(255 * float(cl[1]))))
            colour = colour + "," + str((int(255 * float(cl[2])))) + ")"

        if colour is not None:
            colours[key] = colour

    return colours

def read_default_cultures():
    start = time.clock()

    cult_re = re.compile('culture')
    
    cultures = {}

    for prov in listdir("history/provinces"):
        prov_id = int((prov.split(' '))[0])
        provp = path.join("history/provinces", prov)

        f = open(provp)

        culture = None

        for line in f:

            if re.search(cult_re, line):
                tmp = line.split(' = ')
                tmp = tmp[1].split('#')
                culture = tmp[0].strip()
                break

        if culture is not None:
            cultures[prov_id] = culture

    with open('cultures_and_religions.js', 'a') as f:
        f.write(";var cultures = ") 
        json.dump(cultures, f, separators=(',',':'))

    delta = time.clock() - start
    print ("Culture parsing took %.3f seconds" %delta)

def read_default_religions():
    start = time.clock()

    reli_re = re.compile('religion')
    
    religions = {}

    for prov in listdir("history/provinces"):
        prov_id = int((prov.split(' '))[0])
        provp = path.join("history/provinces", prov)

        f = open(provp)

        religion = None

        for line in f:

            if re.search(reli_re, line):
                tmp = line.split(' = ')
                tmp = tmp[1].split('#')
                religion = tmp[0].strip()
                break

        if religion is not None:
            religions[prov_id] = religion

    with open('cultures_and_religions.js', 'a') as f:
        f.write(";var religions = ") 
        json.dump(religions, f, separators=(',',':'))

    delta = time.clock() - start
    print ("Religion parsing took %.3f seconds" %delta)

def parse_stuff_by_starting_date(starting_date, regx):
    """This function will parse cultures and religions for provinces by a given starting date.
    Mode (culture|religion) is defined with a regex.

    It seems that if a date changes multiple values attributes of the province, changes are split on multiple lines like this:
    1430.1.1 {
    \tculture = ottoman
    \treligion = sunni
    }

    If there is only one change, it sometimes is on a single line:
    790.1.1 { culture = dutch }

    params:

    starting date -- datetime
    regx -- culture or religion
    
    """
    out = {}
    date_re = re.compile('\A\d')

    for prov in listdir("history/provinces"):
        prov_id = int((prov.split(' '))[0])
        provp = path.join("history/provinces", prov)

        f = open(provp)

        for line in f:

            if not go_in:
                if re.match(date_re, line):
                    tmp = line.split('=')
                    dstr = tmp[0].rstrip()
                    
                    if dstr[4] != '.':
                        dstr = '0' + dstr
                    
                    date = time.strptime(dstr,"%Y.%m.%d")
                
                    if date < starting_date:
                        if re.search(regx, tmp[1]):
                            xs = tmp[1].split(' = ')
                            xs = xs[1].split('#')
                            cr = xs[0].strip()

                        else:
                            go_in = True

            else:
                tabs = len(line) - len(line.lstrip('\t'))
                if re.search(regx, line):
                    xs = line.split(' = ')
                    xs = xs[1].split('#')
                    cr = xs[0].strip()
                        
def generate():
    testderp()
    #read_colours()
    #read_cultures()
    #read_religions()

if __name__ == "__main__":
    start = time.clock()
    generate()
    delta = time.clock() - start
    print ("Generating cultures.js took %.3f seconds" %delta)
