"""
Tests for Marcher

Erkki Mattila, 2014
"""

import Image
from marcher import Marcher

def test():

    surrounded = Image.open("test_input/surrounded.bmp")
    surr_pix = surrounded.load()

    separate = Image.open("test_input/separate.bmp")
    sepa_pix = separate.load()

    joined = Image.open("test_input/joined.bmp")
    join_pix = joined.load()

    edges = Image.open("test_input/edges.bmp")
    edge_pix = edges.load()

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

    msurr = Marcher("test_input/surrounded.bmp")
    msepa = Marcher("test_input/separate.bmp")
    mjoin = Marcher("test_input/joined.bmp")
    medge = Marcher("test_input/edges.bmp")

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

    "Start of edges.bmp"
    for colour in edge_test_colours:
        
        medge.colour = colour
        edge_points = medge.do_march()

        for p in edge_points:
            x = p[0]
            y = p[1]
            edge_pix[x,y] = (175,175,175)

    edges.save("test_output/edgetest.bmp")
    print "edges.bmp complete"

if __name__ == "__main__":
    print "Start tests"
    test()
    print "Tests have finished"
