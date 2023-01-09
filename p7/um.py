import re


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(r"(\b[u][m]\b[^a-z0-9]*)", s, re.IGNORECASE):
        return len(matches)
    else:
        matches = []
        return len(matches)




if __name__ == "__main__":
    main()
