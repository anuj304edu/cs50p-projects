def main():
    x, y, z = input("expression: ").split()
    x = int(x)
    z = int(z)
    if z == 0:
        exit()
    match y:
        case "+":
            a = x + z
            print("%.1f" % a)
        case "-":
            a = x - z
            print("%.1f" % a)
        case "*":
            a = x * z
            print("%.1f" % a)
        case "/":
            a = x / z
            print("%.1f" % a)
        case _:
            print("invalid format")


main()
