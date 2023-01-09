

import sys, csv
from tabulate import tabulate

if len(sys.argv) != 3:
    sys.exit("invalid command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
students = []
def main():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for i in reader:
                    last, first= i['name'].split(",")
                    house = i['house']
                    students.append({"first": first.strip(),
                     "last": last.strip(),
                      "house": house.strip()})
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first",
                 "last", "house"])
                writer.writeheader()     
                writer.writerows(students)
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        exit(1)


if __name__ == "__main__":
    main()