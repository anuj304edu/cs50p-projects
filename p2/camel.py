test_str = input("camelCase: ")
if test_str.islower():
    print(test_str)
else:
    while test_str.islower() == False:
        res = [char for char in test_str if char.isupper()]
        for re in res:
            test_str2 = test_str.replace(re, '_'+re.lower())
            test_str = test_str2
    print('snake_case: '+test_str)