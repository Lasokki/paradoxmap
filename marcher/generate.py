"""
Program for generating a GeoJSON-file from provinces.bmp.

This file runs Marchers.

Erkki Mattila, 2014
"""

import Image, time
from marcher import Marcher

def generate(tests):

    img = Image.open("provinces.bmp")
    pix = img.load()
    marcher = Marcher("provinces.bmp")
    out = "test_output/prov_out.bmp"
    colours = [(42,3,128)]

    for colour in colours:
        marcher.colour = colour
        points = marcher.do_march()
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
