"""This script will output a JSON which contains information about holders of provinces.
Folders to check:
/history/provinces/
/history/characters/
/history/titles
"""

def read_provinces():
    pass

def read_characters():
    pass

def read_titles():
    pass

def generate():
    #Collect data
    read_provinces()
    read_characters()
    read_titles()

    #Add them all together
    pass

if __name__ == "__main__":
    start = time.clock()
    generate()
    delta = time.clock() - start
    print ("Generating history took %.3f seconds" %delta)
