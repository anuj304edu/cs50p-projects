import sys, csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

def main():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            print(tabulate(reader,
            headers='firstrow',
            tablefmt='grid'))
    except FileNotFoundError:
        print("File does not exist")
        exit(1)

if __name__ == "__main__":
    main()