# -*- coding: utf-8 -*-

"""
Program for generating a GeoJSON-file from provinces.bmp.

This is the main file responsible for running the show.

Author: Erkki Mattila, 2014-2015
"""

import Image, time, csv
from marcher import Marcher

def read_definition(definition):

    start = time.time()
    print "Reading definition.csv"

    provs = []

    # Stuff to skip
    seas_and_rivers = ["Gulf", "Sea", "SEA", "Golf", "Biscay", "Donegal", "Galway", "Coast", "Cabo", 
                       "Strait", "Cote", "Atlantic", "Faroya", "Hav", "bukten", "Occe", "Channel",
                       "Firth", "Lake", "Saimaa", "The ", "bank", "Manche", "Islas", "Ponant",
                       "Indus", "Ganges", "Brahmaputra", "Seine", "Loire", "Garonne", "Danube", 
                       "Iskender", "Western", "East", "Nile Delta", "Levant", "Elbe", "Rhine", 
                       "Vistula", "Kattegat", "Waddenzee", "Daugava", "Volga1", "Volga2", "Volga3", 
                       "Volga4", "Volga5", "Volga6", "Volga7", "Volga8", "Volga9", "Svir", "Neva", "Don1",
                       "Don2", "Don3", "Don4", "Desna", "Oka", "Lovat", "Volkhov", "Dniester", 
                       "Dnieper1", "Dnieper2", "Dnieper3", "Dnipro", "Dny", "Dne", "Pripyat", "Dwina", "Kallavesi", "Bodensee"]

    #Näsijärvi, Oulujärvi, Mälaren, Hjälmaren, Vättern, Vänern, Onega, Päijänne, some lake in Siberia, spots in the Indian Ocean
    skip_id = [943, 957, 959, 961, 962, 963, 997, 1018, 1293, 1305, 1412]

    csv.register_dialect('ckii', delimiter=';', quoting=csv.QUOTE_NONE)

    with open(definition, 'rb') as f:
        reader = csv.reader(f, 'ckii')

        for row in reader:
            if len(row) > 3 and row[0] != '':
                try:
                    prov_id = int(row[0])
                    prov_name = row[4]
                    allow = True

                    for skip_name in seas_and_rivers:
                        if prov_id in skip_id or prov_name.find(skip_name) != -1:
                            allow = False
                            break

                    if allow:    
                        r = int(row[1])
                        g = int(row[2])
                        b = int(row[3])
                        provs.append(row)
                except ValueError:
                    pass

    delta = time.time() - start
    print ("Reading definition.csv took %.3f seconds" %delta)
    return provs

def find_starting_points(x, y, pixels):
    start = time.time()
    print ("Begun searching for starting points")

    terrain = Image.open("terrain.bmp").convert("RGB")
    terrain_pix = terrain.load()

    water = (69,91,186)
    output = {}

    stop = False
    
    for i in range(x):    # for every pixel:
        for j in range(y):
            try:
                output[pixels[i,j]]
            except KeyError:                
                output[pixels[i,j]] = (i,j)

    delta = time.time() - start
    print ("Finding starting points took %.3f seconds" %delta)   
    
    return output

def generate():

    print ("Begun generating image")
    start = time.time()

    img = Image.open("provinces.bmp")
    #print img.format, img.mode
    pix = img.load()

    marcher = Marcher("provinces.bmp")

    out = "prov_out.bmp"
    provs = read_definition("definition.csv")
    starting_points = find_starting_points(img.size[0], img.size[1], pix)

    i = 0
    prov_count = len(provs)

    max_perimeter = 0
    min_perimeter = 0
    pix_count = 0


    f = open("ckii_provdata.js", 'w')
    f.write('var ckii_provdata = {"type":"FeatureCollection", "features":[') 

    for prov in provs:
        i = i + 1
        
        colour = (int(prov[1]), int(prov[2]), int(prov[3]))
        prov_id = int(prov[0])
        prov_name = prov[4]
        
        print ("{}/{} {} {} {}".format(i, prov_count, colour, prov_name, prov_id))
        marcher.colour = colour

        try:
            sp = starting_points[colour]
            points = marcher.do_march(sp)
            perimeter = 0
            points_string = ""
            
            for p in points:
                x = p[0]
                y = -p[1]
                
                if points_string == "":
                    points_string = points_string + '[{}, {}]'.format(x, y)
                else:
                    points_string = points_string + ',[{}, {}]'.format(x,y)

                pix_count = pix_count + 1
                perimeter = perimeter + 1

            prov_string = '{"type":"Feature","id":"' + str(prov_id) + '","properties":{"name":"' + prov_name + '"},"geometry":{"type":"Polygon","coordinates":[[' + points_string + ']]}}'

            if i == 1:
                f.write(prov_string)
            else:
                f.write(',' + prov_string)

            if perimeter < min_perimeter:
                min_perimeter = perimeter
            if perimeter > max_perimeter:
                max_perimeter = perimeter
            if i == 1:
                min_perimeter = max_perimeter

        except KeyError:
            pass

    f.write(']};')
    f.close
    print("Pixels in outlines: {}\nLongest perimeter: {}\nShortest perimeter: {}".format(pix_count, max_perimeter, min_perimeter))

if __name__ == "__main__":
    start = time.clock()
    generate()
    delta = time.clock() - start
    print ("Generating GeoJSON took %.3f seconds" %delta)
