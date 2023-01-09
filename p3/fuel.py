
def main():
    a = cap()
    if a <= 1:
        print('E')
    elif 100 >= a >= 99:
        print('F')
    elif a > 100:
        cap()
    else:
        print(str(a)+'%')




def cap():
    while True:
        try:
            x = input('fraction: ')
            x, y = x.split(sep='/')
            xp = (int(x)/int(y))*100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return round(xp)


main()