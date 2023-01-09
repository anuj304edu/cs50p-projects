import random


while True:
    x = input('Level: ')
    if x.isnumeric() == False:
        continue
    else:
        break

x = int(x)
r = random.randint(0, x)
while True:
    try:
        y = int(input('Guess: '))
        if y == r:
            print('Just right! ')
            break
        elif 0 <= y < r:
            print('Too small! ')
        elif y > r:
            print('Too large! ')
    except :
        pass