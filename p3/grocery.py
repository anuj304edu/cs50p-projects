d = {}

while True:
    try:
        x = input().upper()
        if x in d:
            d[x]=d[x]+1
        else:
            d[x]=1
    except EOFError:
        for _ in sorted(d):
            print(d[_], _)
        break
