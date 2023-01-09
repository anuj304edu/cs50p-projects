import sys
from PIL import Image, ImageOps
import os

argv_f = os.path.splitext(sys.argv[1])
argv_s = os.path.splitext(sys.argv[2])

if len(sys.argv) != 3:
    sys.exit("invalid command-line arguments")
elif argv_f[1] != argv_s[1]:
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")
before = Image.open(sys.argv[1])
size = shirt.size
before = ImageOps.fit(before, size)
before.paste(shirt, (0, 0), shirt)
before.save(sys.argv[2])
