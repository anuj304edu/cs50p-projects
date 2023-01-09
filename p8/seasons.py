# calculate how old a person in minutes on today's date

from datetime import date, datetime, timedelta
import operator, inflect, sys


def main():
    dob = input("Date of Birth: ")
    minute = get_minutes(dob)
    # convert number into words
    p = inflect.engine()
    words = p.number_to_words(minute, andword="")
    words = str(words).capitalize()
    print(f"{words} minutes")

def get_days(s):
    # calculate number of days since birth
    a = date.today()
    a = datetime.strptime(str(a), '%Y-%m-%d')
    try:
        b = datetime.strptime(s, '%Y-%m-%d')
    except:
        sys.exit("invalid date")
    return operator.__sub__(a, b)

def get_minutes(s):
    # convert days into minutes
    total_time = get_days(s)
    day = total_time.days
    minute = day*24*60
    return minute

if __name__ == "__main__":
    main()
