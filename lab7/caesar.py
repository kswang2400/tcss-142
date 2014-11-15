


def caesar(userInput,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    crypt = ""

    if not len(key) == len(alphabet):
        return None

    for char in userInput:
        if char in alphabet:
                i = alphabet.index(char)
                crypt += key[i]
        else:
            crypt += char
    
    return crypt

# remove a caesar shift from a string
def decaesar(cShift,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    retVal = ''

    if not len(key) == len(alphabet):
        return None

    for char in cShift:
        if char in alphabet:
                retVal += alphabet[key.index(char)]
        else:
            retVal += char
                

    return retVal

def main():
    userString = input("Enter a string to encrypt: ")
    key = "lmnopqrstuvwxyzabcdefghijk"

    cShift = caesar(userString.lower(), key)
    print(cShift)
    original = decaesar(cShift, key)
    print(original)

if __name__== "__main__":
    main()
