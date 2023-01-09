
def main():
    while True:
        try:
            i_fra = input('fraction: ')
            int_per = convert(i_fra)
            if int_per > 100:
                pass
            elif gauge(int_per):
                _ = gauge(int_per)
                print(_)
                exit()
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
            x, y = fraction.split(sep='/')
            if y == 0:
                raise ZeroDivisionError("division by zero")
            xp = (int(x)/int(y))*100
            if xp > 100:
                raise ValueError()
            return round(xp)

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif 100 >= percentage >= 99:
        return 'F'
    else:
        return str(percentage)+'%'


if __name__ == "__main__":
    main()
