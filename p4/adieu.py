import inflect
p = inflect.engine()
mylist = []
while True:
    try:
        x = input('Name: ')
        mylist.append(x)
    except EOFError:
        print('\n''Adieu, adieu, to', p.join(mylist))
        exit()