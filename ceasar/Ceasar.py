# Ceasar encrypt algorithm implementation

BASE = 26
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
EX = ""

def ceasar(plainText, k):
    cipherText = ""
    for letter in plainText:
        if letter != " ":
            index = ALPHABET.find(letter)
            nextIndex = (index + k) % BASE
            cipherText += ALPHABET[nextIndex];
        else:
            cipherText += " ";
    return cipherText

# key in range(0, 25)

def attemptDecrypt(cipherText):
    for key in range(BASE):
        plainText = ""
        for letter in cipherText:
            if letter != " ":
                index = ALPHABET.find(letter)
                prevIndex = (index - key + BASE) % BASE
                plainText += ALPHABET[prevIndex];
            else:
                plainText += " ";
        print("KEY= ", key, "TEXT= ", plainText, end="\n");

# test case

print(ceasar(EX, 18))

cipher = "HQG FY SNSM RFSL"
attemptDecrypt(cipher)


