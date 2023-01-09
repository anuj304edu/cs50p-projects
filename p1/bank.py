# calculate amount bank have to give if not greeted properly

x = input("Greeting:")
y = x.strip().capitalize()
if "Hello" in y:
    print("$0")
elif "H" in y:
    print("$20")
else:
    print("$100")

