"""
Some testing for Marcher
"""

import Image
from marcher import Marcher

def test():


    surrounded = Image.open("surrounded.bmp")
    surr_pix = surrounded.load()

    separate = Image.open("separate.bmp")
    sepa_pix = separate.load()

    joined = Image.open("joined.bmp")
    join_pix = joined.load()

    # blue
    colours = [(0,0,255)]

    msepa = Marcher("separate.bmp", colours)
    msurr = Marcher("surrounded.bmp", colours)
    mjoin = Marcher("joined.bmp", colours)

    sepa_points = msepa.do_march()
    surr_points = msurr.do_march()
    join_points = mjoin.do_march()

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

    separate.show()
    surrounded.show()
    joined.show()

if __name__ == "__main__":
    print "Start tests"
    test()
    print "Tests have finished"
