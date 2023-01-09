import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # length must be between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False
    # first character cann't be a number
    elif s[0:2].isnumeric() == True:
        return False
    for b in s:
        if b in string.punctuation:
            return False
    for k in range(len(s)):
        if s[k].isspace() == True:
          return False
    #first number may not be 0
    for j in range(len(s)-1):
        if s[j] == '0' and s[j-1].isalpha() == True:
            return False
    #numbers cann't be used in middle of plate, only at end
    for i in range(len(s)-1):
        if s[i].isdecimal() == True and s[i+1].isalpha() == True:
            return False
    else:
        return True


main()
