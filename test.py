import os 
from PIL import Image

#infile=Image.open("deer.jpg")
#file, ext = os.path.splitext(infile)
im = Image.open("x.png").convert("RGB")         # any png to jpg 

im.save("modified" + ".webp","WEBP")
im = Image.open("modified.webp")

im.save("result1.jpg","jpeg")              # consitency file image jpg or png you want 
