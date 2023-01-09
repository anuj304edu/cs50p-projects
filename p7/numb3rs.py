import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        ip1 = re.split(r"\.", ip)
        ip_1 = [x for x in ip1 if 0 <= int(x) <= 255]
        if len(ip1) and len(ip_1) == 4:
            return True
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    main()
