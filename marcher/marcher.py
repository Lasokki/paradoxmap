from PIL import Image

# Dict of 14 of the 16 possible directions. Cases 6 and 9 are in step()
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
    """
    Program for generating a GeoJSON-file from provinces.bmp.
    
    This class creates an object that uses marching squares to trace
    outlines of a province.
    
    Author: Erkki Mattila 2014-2015
    """
    
    def __init__(self, i):
        """Note: colour is initially set to None. 
        Clients are expected to set it after initialization with marcher.colour

        Arguments:
        i -- the path to target image
        """

        self.img = Image.open(i)
        self.pixels = self.img.load()
        self.colour = None

    def do_march(self, sp):
        """Returns a generator which yields points along the perimeter of a province.
        The points are tuples (x,y) and designate start- and end-points.
        
        Arguments:
        sp -- the starting point for a colour (province)
        """
        
        #DEBUG
        #print "do_march colours:", self.colour

        if self.colour is not None:
            start_x = sp[0]
            start_y = sp[1]
            points = self.walk_perimeter(start_x, start_y)

        else:
            print ("Error: no colour set for marcher!")
        return points

    def walk_perimeter(self, start_x, start_y):
        """Yields points along the perimeter of a province until it reaches starting point.
        See do_march()

        Arguments:
        start_x and start_y -- coordinates of the starting point
        """

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
        """Checks if pixels at x,y is of the correct colour.
        Returns True, if it is and False, if not.

        Arguments:
        x and y -- coordinates of the pixel
        """

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
        """Calculates direction of next step.
        Four pixels are examined, with pixel at x,y is at the down-right corner of the square.
        These four fields are assigned a boolean value and from them an integer is calculated.
        The integer is then matched with a direction in dict directions.
        Two edge cases are in a separate conditional.

        Returns a character (u, d, r, or l).

        Arguments:
        x and y -- down right coordinate of the square
        prev_step -- direction of previous step (char [u,d,r,l])
        """
        
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
