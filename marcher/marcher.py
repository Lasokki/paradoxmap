"""
A class for generating a GeoJSON file from RGB-bitmap.
I'm not sure wheter to do this as class, or as a dumber script
Author: Erkki Mattila
"""

import Image

class Marcher():
    # Draft for algorithm:
    # Have all possible province colours in a stack
    # Iterate through the pixels. If pixel is non-white and in the stack, start marching.
    # After the province is traced, add the resulting path to output. Remove the colour from stack.
    # Continue iteration until the end of bitmap or when stack is empty.
    
    def __init__(self):
        self.img = Image.open(i)
        self.pixels = img.load()

    def do_march(i):
        sp = find_start_point()
        start_x = sp[0]
        start_y = sp[1]
        points = walk_perimeter(start_x, start_y)

    def find_start_point():

        output = None

        for i in range(self.img.size[0]):    # for every pixel:
            for j in range(self.img.size[1]):
                if pixels[i,j] != (255,255,255):
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

        while:
            next_step = step(x,y, prev_step)

            points.push((x,y))

            if next_step = UP:
                y = y-1
            else if next_step = LEFT:
                x = x-1
            else if next_step = DOWN:
                y = y+1
            else if next_step = RIGHT:
                x = x+1

            prev_step = next_step

        return points

    def step(x, y, prev_step):
        # I'm going to implement algorithm from devblog.phillipspiess.com
        # This is some preliminary non-functional stuff for studying
        
        bool up_left = #if x-1 y-1 is of desired colour
        bool up_right = #x, y-1
        bool down_left = #x-1, y
        bool down_right = #x, y
        
        state = 0

        # do some clever binary assignments
        if (up_left):
            state |= 1
        if (up_right):
            state |= 2
        if (down_left):
            state |= 4
        if (down_right):
            state |= 8

        # state is an integer between 1 and 15
        # each number corresponds to some variant of the square
        # value of state tells the direction of movement
        next_step = {
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

        return next_step
