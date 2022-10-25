# Author: is-it-ayush
# License: MIT

import string

# Cipher History: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# Cool Name (French): le chiffrage indéchiffrable

messsage = input("Enter message: ")
key = input("Enter key: ")

def encrypt(text, key): 
    # Encrypt text with key
    # text: string
    # key: string
    # return: string
    text = text.upper()
    enc = []
    key = key.upper()
    # We want our key to be as long as the text, so we repeat it as many times as needed or shorten it to match our message length.
    key = key * (len(text) // len(key) + 1)
    key = key[:len(text)]

    # Loop through each character in the text
    for i in range(len(text)):
        # If the character is an alphabet, encrypt it and append it to the list
        if text[i].isalpha():
            t = ord(text[i])
            t += ord(key[i]) - 65
            # If the character is outside the range of A-Z, wrap it around.
            if t > 90:
                t -= 26
            enc.append(chr(t))
        else:
            enc.append(text[i])
    # Return the encrypted text
    return "".join(enc)

def decrypt(enc, key): 
    # Decrypt text with key
    # enc: string
    # key: string
    # return: string

    enc = enc.upper()
    dec = []
    key = key.upper()
    key = key * (len(enc) // len(key) + 1)
    key = key[:len(enc)]

    for i in range(len(enc)):
        if enc[i].isalpha():
            t = ord(enc[i])
            t -= ord(key[i]) - 65 # The only difference from the encrypt function
            if t < 65:
                t += 26 # The only difference from the encrypt function
            dec.append(chr(t))
        else:
            dec.append(enc[i])
    return "".join(dec)


print("Encrypted: " + encrypt(messsage, key))
print("Decrypted: " + decrypt(encrypt(messsage, key), key))