def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
       yield ("🍪"*i)

main()