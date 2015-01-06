"""
Program for generating a GeoJSON-file from provinces.bmp.

This file runs Marchers.

Erkki Mattila, 2014
"""

import Image, time, csv
from marcher import Marcher

def read_definition(definition):

    start = time.time()
    print "Reading definition.csv"

    provs = []

    csv.register_dialect('ckii', delimiter=';', quoting=csv.QUOTE_NONE)

    with open(definition, 'rb') as f:
        reader = csv.reader(f, 'ckii')

        for row in reader:
            if len(row) > 3 and row[0] != '':
                try:
                    r = int(row[1])
                    g = int(row[2])
                    b = int(row[3])
                    provs.append((r,g,b))
                except ValueError:
                    pass

    delta = time.time() - start
    print ("Reading definition took %.3f seconds" %delta)
    return provs

def find_starting_points(x, y, pixels, provs):
    start = time.time()
    print ("Begun searching for starting points")
    
    output = {}

    for colour in provs:

        stop = False

        for i in range(x):    # for every pixel:
            for j in range(y):
                if pixels[i,j] == colour:
                    output[colour] = (i,j)
                    # jump out
                    stop = True
                    break
            if stop == True:
                break

    delta = time.time() - start
    print ("Finding starting points took %.3f seconds" %delta)   
    
    return output

def generate():

    print ("Begun generating image")
    start = time.time()

    img = Image.open("provinces.bmp")
    pix = img.load()
    marcher = Marcher("provinces.bmp")
    out = "test_output/prov_out.bmp"
    provs = read_definition("definition.csv")
    starting_points = find_starting_points(img.size[0], img.size[1], pix, provs)

    for colour in provs:
        print colour
        marcher.colour = colour
        sp = starting_points[colour]
        points = marcher.do_march(sp)
        for p in points:
            x = p[0]
            y = p[1]
            pix[x,y] = (255,0,0)

    img.save(out)

if __name__ == "__main__":
    start = time.clock()
    generate()
    delta = time.clock() - start
    print ("Generating image took %.3f seconds" %delta)
