from PIL import Image
from set import Set

def neighbours(x, y, width, mapped):
    output = [None, None, None, None]
    
    if y != 0:
        if x != 0:
            output[0] = mapped[x-1][y-1]
            output[1] = mapped[x][y-1]
            
            if not x+1 >= width:
                output[2] = mapped[x+1][y-1]
                
            output[3] = mapped[x-1][y]

        else:
            output[1] = mapped[x][y-1]
            output[2] = mapped[x+1][y-1]
             
    elif x != 0:
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

    # First pass: mark each component with labels
    for x in range(width):    # for every pixel:
        for y in range(height):
            #print x, y
            px = pixels[x,y]

            if px != (255,255,255):
               
               # Search for neighbours 
                nghs = neighbours(x,y, width, mapped_image)
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
                    else:
                        min_neigh = w
                       
                    if min_neigh is not None:
                        for ng in nghs:
                            if ng is not None and (ng.label < min_neigh.label):
                                min_neigh = ng
                        

                    mapped_image[x][y] = min_neigh

                    for ng in nghs:
                        if ng is not None and min_neigh is not None:
                            union(min_neigh, ng)


    for x in range(width):    # for every pixel:
        for y in range(height):
            px = pixels[x,y]
            
            if px != (255,255,255):
                mapped_image[x][y] = find(mapped_image[x][y])


    return mapped_image

if __name__ == "__main__":
    img = Image.open("provinces.bmp")
    print img.size[0], img.size[1]
    
    pix = img.load()
    mapped = map_image(img.size[0], img.size[1], pix)
    
