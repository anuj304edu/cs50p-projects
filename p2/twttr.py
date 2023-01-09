
x1 = input('input: ')
char_to_replace = {'a': '', 'e': '', 'i': '', 'o': '', 'u': '',
                   'A': '', 'E': '', 'I': '', 'O': '', 'U': '',}
# Iterate over all key-value pairs in dictionary
for key, value in char_to_replace.items():
    # Replace key character with value character in string
    x1 = x1.replace(key, value)
print(x1)