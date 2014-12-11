"""
A program for generating a GeoJSON file from RGB-bitmap.
Author: Erkki Mattila
"""

import Image

# Draft for algorithm:
# Have all possible province colours in a stack
# Iterate through the pixels. If pixel is non-white and in the stack, start marching.
# After the province is traced, add the resulting path to output. Remove the colour from stack.
# Continue iteration until the end of bitmap or when stack is empty.
 
#img = Image.open("/home/lasokki/projects/map_project/imgs/provinces.bmp")
img = Image.open("surrounded.bmp")

pixels = img.load() # create the pixel map
counter = 0
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        if pixels[i,j] != (255,255,255):
            counter = counter + 1
print "non-white pixels: %d" % counter
print img.format, img.size, img.mode
