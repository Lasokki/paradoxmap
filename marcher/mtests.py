"""
Some testing for Marcher
"""

import Image

def test():
    #msurr = Marcher("surrounded.bmp"
    #mjoin = Marcher("joined.bmp")

    separate = Image.open("separate.bmp")
    pixels = separate.load()
    msepa = Marcher("separate.bmp")

    points = msepa.do_march()
    
    for p in points:
        x = p[0]
        y = p[1]
        pixles[x,y] = (255,0,0)

    separate.show()
    
if __name__ == "main":
    tests()
