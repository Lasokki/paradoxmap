"""
Tests for Marcher

Erkki Mattila, 2014
"""

import Image, sys
from marcher import Marcher

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
        colours = simple_test_colours
        if test == "sur":
            img = Image.open("test_input/surrounded.bmp")
            pix = img.load()
            marcher = Marcher("test_input/surrounded.bmp")
            out = "test_output/surrtest.bmp"
        elif test == "sep":
            img = Image.open("test_input/separate.bmp")
            pix = img.load()
            marcher = Marcher("test_input/separate.bmp")
            out = "test_output/sepatest.bmp"
        elif test == "joi":
            img = Image.open("test_input/joined.bmp")
            pix = img.load()
            marcher = Marcher("test_input/joined.bmp")
            out = "test_output/jointest.bmp"
        elif test == "edg":
            img = Image.open("test_input/edges.bmp")
            pix = img.load()
            marcher = Marcher("test_input/edges.bmp")
            out = "test_output/edgetest.bmp"
            colours = edge_test_colours
        elif test == "squ":
            img = Image.open("test_input/squiggles.bmp")
            pix = img.load()
            marcher = Marcher("test_input/squiggles.bmp")
            out = "test_output/squitest.bmp"
            colours = squi_test_colours

        for colour in colours:
            marcher.colour = colour
            points = marcher.do_march()
            for p in points:
                x = p[0]
                y = p[1]
                print x,y
                pix[x,y] = (255,0,0)

            img.save(out)
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print "Start tests"
        test(sys.argv[1:])
        print "Tests have finished"
    else:
        print "Give some tests: sur, sep, joi, edg, squ"
