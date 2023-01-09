
def main():
    print(shorten(input('input: ')))


def shorten(word):
    char_to_replace = {'a': '', 'e': '', 'i': '', 'o': '', 'u': '',
                   'A': '', 'E': '', 'I': '', 'O': '', 'U': '',}
# Iterate over all key-value pairs in dictionary
    for key, value in char_to_replace.items():
        # Replace key character with value character in string
        word = word.replace(key, value)
    return word


if __name__ == "__main__":
    main()
