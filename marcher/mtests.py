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

    edges = Image.open("test_input/complex.bmp")
    edge_pix = edges.load()

    blue = (0,0,255)
    green = (0,255,0)

    colours = [blue, green]

    msurr = Marcher("test_input/surrounded.bmp")
    msepa = Marcher("test_input/separate.bmp")
    mjoin = Marcher("test_input/joined.bmp")
    medge = Marcher("test_input/complex.bmp")

    for colour in colours:

        msurr.colour = colour
        msepa.colour = colour
        mjoin.colour = colour
        medge.colour = colour

        sepa_points = msepa.do_march()
        surr_points = msurr.do_march()
        join_points = mjoin.do_march()
        edge_points = medge.do_march()

        for p in sepa_points:
            x = p[0]
            y = p[1]
            sepa_pix[x,y] = (255,0,0)

        for p in surr_points:
            x = p[0]
            y = p[1]
            surr_pix[x,y] = (255,0,0)

        for p in join_points:
            x = p[0]
            y = p[1]
            join_pix[x,y] = (255,0,0)

        for p in edge_points:
            x = p[0]
            y = p[1]
            edge_pix[x,y] = (175,175,175)

    separate.save("test_output/sepatest.bmp")
    surrounded.save("test_output/surrtest.bmp")
    joined.save("test_output/jointest.bmp")
    edges.save("test_output/edgetest.bmp")
    
if __name__ == "__main__":
    print "Start tests"
    test()
    print "Tests have finished"
