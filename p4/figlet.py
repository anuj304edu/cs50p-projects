import sys

import random

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 2 or len(sys.argv)> 3:
    sys.exit('invalid usage')

# for no command-line argument

elif len(sys.argv) == 1:
    x = input('input: ')
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print("output:")
    print(figlet.renderText(x))
    print(f)

elif sys.argv[1] != '-f' or sys.argv[1] != '--font' and sys.argv[2] not in figlet.getFonts():
    sys.exit('invalid usage')

else:
    x = input('input: ')
    figlet.setFont(font=sys.argv[2])
    print("output:")
    print(figlet.renderText(x))