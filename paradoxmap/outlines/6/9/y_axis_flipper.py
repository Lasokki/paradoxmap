import os

for filename in os.listdir("."):
    if filename.endswith(".png"):
        print filename
