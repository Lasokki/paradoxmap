"""
Program for generating a GeoJSON-file from provinces.bmp.

This class creates an object that uses marching squares to trace
outlines of a province.

Author: Erkki Mattila 2014-2015
"""

import Image

directions = {
    1 : 'u',
    2 : 'r',
    3 : 'r',
    4 : 'l',
    5 : 'u',
    7 : 'r',
    8 : 'd',
    10 : 'd',
    11 : 'd',
    12 : 'l',
    13 : 'u',
    14 : 'l'
}

class Marcher(object):
    
    def __init__(self, i):
        self.img = Image.open(i)
        self.pixels = self.img.load()
        self.colour = None

    def do_march(self, sp):

        #DEBUG
        #print "do_march colours:", self.colour

        if self.colour is not None:
            start_x = sp[0]
            start_y = sp[1]
            points = self.walk_perimeter(start_x, start_y)

        else:
            print "Error: no colour set for marcher!"
        return points

    def walk_perimeter(self, start_x, start_y):

        prev_step = None

        x = start_x
        y = start_y

        stop = False

        while stop == False:

            next_step = self.step(x, y, prev_step)

            if x >= 0 and x < self.img.size[0] and y >= 0 and y < self.img.size[1]:
                if next_step is not prev_step:
                    yield (x,y)

            if next_step == 'u':
                y = y-1
            elif next_step == 'l':
                x = x-1
            elif next_step == 'd':
                y = y+1
            elif next_step == 'r':
                x = x+1

            prev_step = next_step

            if x == start_x and y == start_y:
                #DEBUG
                #print x, y, start_x, start_y
                stop = True

    def is_desired_colour(self, x, y):
        output = False
        #width, height
        if x < self.img.size[0] and x >= 0 and y < self.img.size[1] and y >= 0:
            #DEBUG
            #print "currcoord", x,y
            #print "imgsize", self.img.size[0], self.img.size[1]
            if self.pixels[x,y] == self.colour:
                output = True
        #else:
            #print "DEBUG: OUT OF BOUNDS"
        return output

    def step(self, x, y, prev_step):
        
        up_left = self.is_desired_colour(x-1, y-1)
        up_right = self.is_desired_colour(x, y-1)
        down_left = self.is_desired_colour(x-1, y)
        down_right = self.is_desired_colour(x, y)

        state = 0

        #DEBUG
        #print x, y
        #print "ul", up_left
        #print "ur", up_right
        #print "dl", down_left
        #print "dr", down_right
       
        # Do some clever binary assignments
        if up_left:
            state |= 1
        if up_right:
            state |= 2
        if down_left:
            state |= 4
        if down_right:
            state |= 8

        #DEBUG
        #print "step state:", state

        # State is now an integer between 1 and 15
        # Each number corresponds to some variant of the square
        # Value of state tells the direction of next step

        next_step = None

        if state == 6:
            if prev_step == 'u':
                next_step = 'l'
            else:
                next_step = 'r'

        elif state == 9:
            if prev_step == 'r':
                next_step = 'u'
            else:
                next_step = 'd'

        else:
            next_step = directions.get(state,None)
        
        return next_step
