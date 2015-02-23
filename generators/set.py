class Set(object):

    def __init__(self, l, c):
        self.parent = self
        self.rank = 0
        self.label = l
        self.col = c
