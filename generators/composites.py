from PIL import Image
from unionset import UnionSet
import sys

def neighbours(x, y, width, mapped):
    output = [None, None, None, None]
    
    if y != 0:
        if x != 0:
            output[0] = mapped[y-1][x-1]
            output[1] = mapped[y-1][x]
            
            if not x+1 >= width:
                output[2] = mapped[y-1][x+1]

            output[3] = mapped[y][x-1]

        else:
            output[1] = mapped[y-1][x]
            output[2] = mapped[y-1][x+1]
             
    elif x != 0:
        output[3] = mapped[y][x-1]
    
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
    
    mapped_image = [[None] * width] * height
    next_label = 1

    # DEBUG DEBUG DEBUG
    herp_image = Image.new('RGB', (width, height), "white")
    herp_pix = herp_image.load()
    
    # First pass: mark each component with labels
    for y in range(height):    # for every pixel:
        for x in range(width):
            #print x, y
            px = pixels[x,y]

            if px != (255,255,255):
               
               # Search for neighbours 
                nghs = neighbours(x,y, width, mapped_image)

                nw = None
                n = None
                ne = None
                w = None

                if nghs[0] is not None and nghs[0].col == px:
                    nw = nghs[0]
                if nghs[1] is not None and nghs[1].col == px:
                    n = nghs[1]
                if nghs[2] is not None and nghs[2].col == px:
                    ne = nghs[2]
                if nghs[3] is not None and nghs[3].col == px:
                    w = nghs[3]

                if nw is None and n is None and ne is None and w is None:
                    print("WHOOP", x, y, nw, n, ne, w)
                    mapped_image[y][x] = UnionSet(next_label, px, [x,y])
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
                            if ng is not None and ng.col == px and (ng.label < min_neigh.label):
                                min_neigh = ng

                    #print (min_neigh.xy)

                    mapped_image[y][x] = min_neigh

                    for ng in nghs:
                        if ng is not None and ng.col == px and min_neigh is not None:
                            union(min_neigh, ng)


                    for y in range(height):
                        for x in range(width):
                            if mapped_image[y][x] is not None:
                                herp_pix[x,y] = mapped_image[y][x].col
                            else:
                                herp_pix[x,y] = (255,255,255)

                            if (y % 100 == 0):
                                herp_image.save("lol/" + str(y) + "_" + str(x) + ".bmp")

    for y in range(height):    # for every pixel:
        for x in range(width):
            px = pixels[x,y]
            
            if px != (255,255,255):
                mapped_image[y][x] = find(mapped_image[y][x])


    """
    DEBUG OUTPUT INTO A PIC
    """

    debug_image = Image.open(sys.argv[1])
    debug_pix = debug_image.load()

    for y in range(height):
        for x in range(width):
            if mapped_image[y][x] is not None:
                #if (y==0):
                #    print (x,y)
                debug_pix[x,y] = mapped_image[y][x].col
                #debug_pix[x,y] = (0,0,0)
            else:
                debug_pix[x,y] = (255,255,255)

    debug_image.save("debug.bmp")

    out = {}
    for y in range(height):
        for x in range(width):
            col = pixels[x,y]

            if col != (255,255,255):
                arr = out.get(col)
                #print(arr)
                if arr is not None:
                    #print ("YOINK!")
                    if mapped_image[y][x] not in arr:
                        #print ("APPENDING! " + str(x) + " " + str(y) + " " + str(col) + " " + str(mapped_image[y][x]) + " " + str(mapped_image[x][y].col))
                        arr.append(mapped_image[y][x])
                        out[col] = arr

                else:
                    #print("empty arr, adding stuff ", col, mapped_image[y][x].xy, mapped_image[y][x].col)
                    out[col] = [mapped_image[y][x]]
    return out

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img = Image.open(sys.argv[1])
        print (img.size[0], img.size[1])
        
        pix = img.load()
        mapped = map_image(img.size[0], img.size[1], pix)
        
        #print (mapped)

        for col in mapped:
            print (col)
            for group in mapped[col]:
                print(group.xy)
        

    else:
        print ("Give a target file, please")
