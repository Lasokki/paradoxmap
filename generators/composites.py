from PIL import Image

def neighbours(x, y, mapped):
    output = [None, None, None, None]
    
    if y != 0:
        if x != 0:
            output[0] = mapped[x-1][y-1]
            output[1] = mapped[x][y-1]
            
            if not (x >= width):
                output[2] = mapped[x+1][y-1]
                
            output[3] = mapped[x-1][y]

        else:
            output[1] = mapped[x][y-1]
            output[2] = mapped[x+1][y-1]
             
        elif(x != 0):
            output[3] = mapped[x-1][y]
    
    return output

def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root != b_root:
        
        if a_root.rank < b_root.rank:
            a_root.parent = b_root

        elif a_root.rank > b_root.rank:
            b_root.parent = a_root

        else:
            b_root.parent = a_root
            a_root.rank = a_root.rank + 1

def find(s):

    if s.parent is not s:
        s.parent = find(s.parent)
    
    return s.parent

def map_image(width, height, pixels):
    
    mapped_image = [[None] * height] * width
    next_label = 1

    for i in range(width):    # for every pixel:
        for j in range(height):
           px = pixels[i,j]

           if px is not (255,255,255):
               
               nghs = neighbours(x,y, mapped_image)
               nw = nghs[0]
               n = nghs[1]
               ne = nghs[2]
               w = nghs[3]

               if nw is None and n is None and ne is None and w is None:
                   mapped_image[x][y] = Set(next_label, px)
                   next_label = next_label + 1
                
               else:
                   min_neigh = None

                   if nw is not None:
                       min_neigh = nw
                   elif n is not None:
                       min_neigh = n
                   elif ne is not None:
                       min_neigh = ne
                   elif w is not None:
                       min_neigh = w

                    if min_neigh is not None:
                        for ng in nghs:
                            if ng is not None and (ng.label < min_neigh.label):
                                min_neigh = ng
                        
