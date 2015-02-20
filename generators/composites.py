def neighbors(x, y, mapped):
    output = [None, None, None, None]
    
    if y != 0:
        if x != 0:
            output[0] = mapped[y-1][x-1]
            output[1] = mapped[y-1][x]
            
            if not (x >= width):
                output[2] = mapped[y-1][x+1]
                
            output[3] = mapped[y][x-1]

        else:
            output[1] = mapped[y-1][x]
            output[2] = mapped[y-1][x+1]
             
        elif(x != 0):
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
