import validators

value = input("what's your email address? ")
if validators.email(value):
    print("Valid")
else:
    print("Invalid") 
