import sys, csv
from tabulate import tabulate

if len(sys.argv) != 3:
    sys.exit("invalid command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

def main():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file,
                 fieldnames=["first", "last", "house"])
                writer.writeheader()
                for i in reader:
                    last, first= i['name'].split(",")
                    house = i['house']
                    writer.writerow({"first": first.strip(),
                     "last": last.strip(),
                      "house": house.strip()})
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        exit(1)


if __name__ == "__main__":
    main()