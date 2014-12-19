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
    
    def __init__(self, i):
        self.img = Image.open(i)
        self.pixels = img.load()

    def do_march():
        sp = find_start_point()
        start_x = sp[0]
        start_y = sp[1]
        points = walk_perimeter(start_x, start_y)

        return points

    def find_start_point():

        output = None

        for i in range(self.img.size[0]):    # for every pixel:
            for j in range(self.img.size[1]):
                if self.pixels[i,j] != (255,255,255):
                    output = (i,j)
                    # jump out
                    i = self.img.size[0] + 1
                    j = self.img.size[1] + 1

        return output

    def walk_perimeter(start_x, start_y):
        points = None
        prev_step = None

        x = start_x
        y = start_y

        stop = False

        while stop == False:
            next_step = step(x,y, prev_step)

            points.push((x,y))

            if next_step == 'u':
                y = y-1
            else if next_step == 'l':
                x = x-1
            else if next_step == 'd':
                y = y+1
            else if next_step == 'r':
                x = x+1

            prev_step = next_step

            if x == start_x and y == start_y:
                stop = True

        return points

    def is_desired_colour(x, y, colour):
        output = False
        if self.pixels[x,y] == colour:
            output = True

    def step(x, y, prev_step):
        
        bool up_left = is_desired_colour(x-1, y-1)
        bool up_right = is_desired_colour(x, y-1)
        bool down_left = is_desired_colour(x-1, y)
        bool down_right = is_desired_colour(x, y)
        
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

        # State is now an integer between 1 and 15
        # Each number corresponds to some variant of the square
        # Value of state tells the direction of movement

        next_step = None

        if state == 6:
            if prev_step == 'u':
                next_step = 'l'
            else:
                next_step = 'r'

        else if state == 9:
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
        
        # else if state == 2 or state == 3 or state == 7:
        #     next_step = 'r'
        
        # else if state == 4 or state == 12 or state == 14:
        #     next_step = 'l'

        # else if state == 6:
        #     if prev_step == 'u':
        #         next_step = 'l'
        #     else:
        #         next_step = 'r'

        # else if state == 8 or state == 10 or state == 11:
        #     next_step = 'd'

        # else if state == 9:
        #     if prev_step == 'r':
        #         next_step = 'u'
        #     else:
        #         next_step = 'd'

        return next_step
