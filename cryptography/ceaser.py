# Author: is-it-ayush
# License: MIT

import pwn # pip install pwntools (Not required, but recommended)
import string

def encrypt(text, key):
    # Encrypt text with key
    # text: string
    # key: int (0-25)
    # return: string
    text = text.upper()
    enc = []

    # If the key is outside the range of 0-25, wrap it around.
    if(key > 25):
        key = key % 26
        print("[Info] Key is too large, using key %d" % key)

    # Loop through each character in the text
    for i in range(len(text)):
        # If the character is an alphabet, encrypt it and append it to the list
        if text[i].isalpha():
            t = ord(text[i])
            t += key
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
    # key: int (0-25)
    # return: string

    # The only difference between this and the encrypt function is that we subtract the key instead of adding it.

    enc = enc.upper()
    dec = []

    # If the key is outside the range of 0-25, wrap it around.
    if(key > 25):
        key = key % 26
        print("[Info] Key is too large, using key %d" % key)

    # Loop through each character in the text
    for i in range(len(enc)):
        # If the character is an alphabet, decrypt it and append it to the list
        if enc[i].isalpha():
            t = ord(enc[i])
            t -= key
            # If the character is outside the range of A-Z, wrap it around.
            if t < 65:
                t += 26
            dec.append(chr(t))
        else:
            dec.append(enc[i])
    # Return the decrypted text
    return "".join(dec)

# Parameters
message = "Hello, World!"
key = 5

print("Message: %s" % message)
print("Key: %d" % key)

enc = encrypt(message, key)
print("Encrypted: %s" % enc)

dec = decrypt(enc, key)
print("Decrypted: %s" % dec)
