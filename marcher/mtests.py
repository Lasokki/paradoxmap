"""
Tests for Marcher

Erkki Mattila, 2014
"""

import Image, sys, time
from marcher import Marcher

def find_starting_points(x, y, pixels, provs):
    start = time.time()
    print ("Begun searching for starting points")
    
    output = {}

    for colour in provs:
        print "sp", colour
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

def test(tests):

    blue = (0,0,255)
    green = (0,255,0)
    red = (255, 0, 0)
    cyan = (0, 255, 255)
    yellow = (255, 255, 0)
    purple = (255, 0, 255)
    grey = (100, 100, 100)
    white = (255, 255, 255)
    
    simple_test_colours = [blue, green]
    edge_test_colours = [blue, green, red, cyan, yellow, purple, grey, white]
    squi_test_colours = [blue, green, yellow]

    for test in tests:
        start = time.time()
        colours = simple_test_colours
        if test == "sur":
            infile = "test_input/surrounded.bmp"
            out = "test_output/surrtest.bmp"
        elif test == "sep":
            infile = "test_input/separate.bmp"
            out = "test_output/sepatest.bmp"
        elif test == "joi":
            infile = "test_input/joined.bmp"
            out = "test_output/jointest.bmp"
        elif test == "edg":
            infile = "test_input/edges.bmp"
            out = "test_output/edgetest.bmp"
            colours = edge_test_colours
        elif test == "squ":
            infile = "test_input/squiggles.bmp"
            out = "test_output/squitest.bmp"
            colours = squi_test_colours
        else:
            print("no test given")
            break

        img = Image.open(infile)
        pix = img.load()
        marcher = Marcher(infile)
        starting_points = find_starting_points(img.size[0], img.size[1], pix, colours)


        for colour in colours:
            print "gen", colour
            marcher.colour = colour
            sp = starting_points[colour]
            points = marcher.do_march(sp)
            for p in points:
                x = p[0]
                y = p[1]
                pix[x,y] = (255,0,0)

            img.save(out)

        delta = time.time() - start
        print (test + " took %.3f seconds to complete" %delta)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print ("Begun tests")
        start = time.time()
        test(sys.argv[1:])
        delta = time.time() - start
        print ("Tests have finished in ~%.3f seconds" %delta)
    else:
        print ("Give some tests: sur, sep, joi, edg, squ")
