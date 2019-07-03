# CREATED BY 0Bon100    ~2019
# PYTHON 2.7

INPUT_FILE = "image.png" #INPUT IMAGE PATH
OUTPUT_FILE = "out.svg" #OUTPUT IMAGE PATH (YOU CAN LEAVE IT LIKE THAT)

from PIL import Image
import os
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)
file = open(OUTPUT_FILE, "a")
img = Image.open(INPUT_FILE)
pixels = img.load()
size = img.size

file.write('<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" version="1.1">')

for x in xrange(size[0]):
    for y in xrange(size[1]):
        color = pixels[x,y]
        rgb = "rgb({0},{1},{2})".format(color[0],color[1],color[2])
        file.write('<rect fill-opacity="{0}" x="{1}" y="{2}" fill="{3}" width="1" height="1"/>'.format(color[3]/255.0, x, y, rgb))

file.write('</svg>')
print "Done!"