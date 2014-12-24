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

    test_sur = False
    test_sep = False
    test_joi = False
    test_edg = False

    for test in tests:
        if test == "sur":
            test_sur = True
        elif test == "sep":
            test_sep = True
        elif test == "joi":
            test_joi = True
        elif test == "edg":
            test_edg = True

    if test_sur == True:
        surrounded = Image.open("test_input/surrounded.bmp")
        surr_pix = surrounded.load()
        msurr = Marcher("test_input/surrounded.bmp")

        print "Start of surrounded.bmp"
        for colour in simple_test_colours:

            msurr.colour = colour
            surr_points = msurr.do_march()

            for p in surr_points:
                x = p[0]
                y = p[1]
                surr_pix[x,y] = (255,0,0)

        surrounded.save("test_output/surrtest.bmp")
        print "surrounded.bmp complete"
    
    if test_sep == True:
        separate = Image.open("test_input/separate.bmp")
        sepa_pix = separate.load()
        msepa = Marcher("test_input/separate.bmp")

        print "Start of separate.bmp"
        for colour in simple_test_colours:

            msepa.colour = colour
            sepa_points = msepa.do_march()
        
            for p in sepa_points:
                x = p[0]
                y = p[1]
                sepa_pix[x,y] = (255,0,0)

        separate.save("test_output/sepatest.bmp")
        print "separate.bmp complete"

    if test_joi == True:
        joined = Image.open("test_input/joined.bmp")
        join_pix = joined.load()
        mjoin = Marcher("test_input/joined.bmp")
        
        print "Start of joined.bmp"
        for colour in simple_test_colours:

            mjoin.colour = colour
            join_points = mjoin.do_march()

            for p in join_points:
                x = p[0]
                y = p[1]
                join_pix[x,y] = (255,0,0)
    
        joined.save("test_output/jointest.bmp")
        print "joined.bmp complete"

    if test_edg == True:
        edges = Image.open("test_input/edges.bmp")
        edge_pix = edges.load()
        medge = Marcher("test_input/edges.bmp")

        "Start of edges.bmp"
        for colour in edge_test_colours:
            print colour
            medge.colour = colour
            edge_points = medge.do_march()

            print "editing picture"
            for p in edge_points:
                x = p[0]
                y = p[1]
                #print x,y
                edge_pix[x,y] = (red)

        edges.save("test_output/edgetest.bmp")
        print "edges.bmp complete"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print "Start tests"
        test(sys.argv[1:])
        print "Tests have finished"
    else:
        print "Give some tests"
