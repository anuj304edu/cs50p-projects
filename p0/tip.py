# tip calculator

def main():
    dollars = dollars_to_float()
    percent = percent_to_float()
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#convert cost of meal into float
def dollars_to_float():
    x = input("How much was the meal? ")
    x = x.replace("$"," ")
    x = float(x)
    return x

# convert tip percentage into float
def percent_to_float():
    y = input("What percentage would you like to tip? ")
    y = y.replace("%","")
    y = float(y)
    y = y/100
    return y

if __name__=="__main__":
    main()