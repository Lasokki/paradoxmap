import Image
 
#img = Image.open("/home/lasokki/projects/paradoxmap/imgs/provinces.bmp")
img = Image.open("surrounded.bmp")

pixels = img.load() # create the pixel map
counter = 0
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        if pixels[i,j] != (255,255,255):
            counter = counter + 1
print "non-white pixels: %d" % counter
print img.format, img.size, img.mode
