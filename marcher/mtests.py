"""
Some testing for Marcher
"""

import Image

def test():
    #msurr = Marcher("surrounded.bmp"
    #mjoin = Marcher("joined.bmp")

    separate = Image.open("separate.bmp")
    pixels = separate.load()

    # blue
    s_colours = [(0,0,255)]

    msepa = Marcher("separate.bmp", s_colours)

    points = msepa.do_march()
    
    for p in points:
        x = p[0]
        y = p[1]
        pixels[x,y] = (255,0,0)

    separate.show()
    
if __name__ == "main":
    test()
