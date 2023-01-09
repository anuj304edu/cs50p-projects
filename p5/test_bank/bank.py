
def main():
    x = input("Greeting: ")
    print("$", value(x), sep="")

def value(greeting):
    greeting = greeting.strip().capitalize()
    if "Hello" in greeting:
        return 0
    elif "H" in greeting:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()