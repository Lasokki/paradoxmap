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


# I'm going to implement algorithm from devblog.phillipspiess.com
# This is some preliminary non-functional stuff for studying

bool upLeft = #if x-1 y-1 is of desired colour
bool upRight = #x, y-1
bool downLeft = #x-1, y
bool downRight = #x, y

prevstep = nextstep

state = 0

# do some clever binary assignments
if (upLeft):
    state |= 1
if (upRight):
    state |= 2
if (downLeft):
    state |= 4
if (downRight):
    state |= 8

# state is an integer between 1 and 15
# each number corresponds to some variant of the square
# value of state tells the direction of movement
nextstep = {
    1 : UP,
    2 : RIGHT,
    3 : RIGHT,
    4 : LEFT,
    5 : UP,
    6 : #IF-ELSE: IF UP -> LEFT, ELSE -> RIGHT
    7 : RIGHT,
    8 : DOWN,
    9 : #IF-ELSE: IF RIGHT -> UP, ELSE -> DOWN
    10 : DOWN,
    11 : DOWN,
    12 : LEFT,
    13 : UP,
    14 : LEFT,
    default: none
    }[value](state)
