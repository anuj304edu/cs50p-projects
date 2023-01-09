import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")


def main():
    try:
        with open(sys.argv[1]) as file:
            list_ = file.readlines()
        list_1 = [s.lstrip() for s in list_]
        list_2 = [x for x in list_1 if x.startswith('#') == False]
        list_3 = [i for i in list_2 if i]
        print(len(list_3))
    except FileNotFoundError:
        print("File does not exist")

if __name__ == "__main__":
    main()