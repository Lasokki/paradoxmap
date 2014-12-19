"""
A class for generating a GeoJSON file from RGB-bitmap.
I'm not sure wheter to do this as class, or as a dumber script
Author: Erkki Mattila
"""

import Image

class Marcher(object):
    # Draft for algorithm:
    # Have all possible province colours in a stack
    # Iterate through the pixels. If pixel is non-white and in the stack, start marching.
    # After the province is traced, add the resulting path to output. Remove the colour from stack.
    # Continue iteration until the end of bitmap or when stack is empty.
    
    def __init__(self, i, c):
        self.img = Image.open(i)
        self.pixels = self.img.load()
        self.colours = c

    def do_march(self):
        # At this point we shall search only for one colour.

        #DEBUG
        print self.colours[0]

        sp = self.find_start_point(self.colours[0])
        start_x = sp[0]
        start_y = sp[1]
        points = self.walk_perimeter(start_x, start_y)

        return points

    def find_start_point(self, colour):

        output = None
        stop = False

        for i in range(self.img.size[0]):    # for every pixel:
            for j in range(self.img.size[1]):
                if self.pixels[i,j] == colour:
                    output = (i,j)
                    # jump out
                    stop = True
                    break
            if stop == True:
                break

        print output
        return output

    def walk_perimeter(self, start_x, start_y):
        points = []
        prev_step = None

        x = start_x
        y = start_y

        stop = False

        while stop == False:
            points.append((x,y))
            next_step = self.step(x, y, prev_step)

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
                stop = True

        return points

    def is_desired_colour(self, x, y, colour):
        output = False
        if self.pixels[x,y] == colour:
            output = True

    def step(self, x, y, prev_step):
        
        up_left = self.is_desired_colour(x-1, y-1, self.colours[0])
        up_right = self.is_desired_colour(x, y-1, self.colours[0])
        down_left = self.is_desired_colour(x-1, y, self.colours[0])
        down_right = self.is_desired_colour(x, y, self.colours[0])
        
        state = 0

        # Do some clever binary assignments
        if (up_left):
            state |= 1
        if (up_right):
            state |= 2
        if (down_left):
            state |= 4
        if (down_right):
            state |= 8

        #DEBUG
        print state

        # State is now an integer between 1 and 15
        # Each number corresponds to some variant of the square
        # Value of state tells the direction of movement

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
            # It might be smart to initialize this dict somewhere else, if this implementation does it every
            # time when this function is called.
            next_step = {
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
            }.get(state, None)


        # If code above doesn't work, this if-else monster should do the job

        # next_step = None

        # if state == 1 or state == 5 or state == 13:
        #     next_step = 'u'
        
        # elif state == 2 or state == 3 or state == 7:
        #     next_step = 'r'
        
        # elif state == 4 or state == 12 or state == 14:
        #     next_step = 'l'

        # elif state == 6:
        #     if prev_step == 'u':
        #         next_step = 'l'
        #     else:
        #         next_step = 'r'

        # elif state == 8 or state == 10 or state == 11:
        #     next_step = 'd'

        # elif state == 9:
        #     if prev_step == 'r':
        #         next_step = 'u'
        #     else:
        #         next_step = 'd'

        return next_step
