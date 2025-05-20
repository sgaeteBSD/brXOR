 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal

def main():
    inp = input("Text to encrypt: ")
    k1 = 'I'
    k2 = 'C'
    k3 = 'E'
    key1 = ord(k1)
    key2 = ord(k2)
    key3 = ord(k3)
    #b = ASCIIToBytes(inp)
    print(bytesToHex(repeatXOR(inp, key1, key2, key3)))
    
    
def hexToBytes(hx):
    return list(bytes.fromhex(hx))

def bytesToHex(byts):
    return (bytes(byts)).hex()
    
def bytesToASCII(byts):
    return bytes(byts).decode("ascii", errors="ignore")

def ASCIIToBytes(stri):
    return stri.encode("ascii", errors="ignore")

def repeatXOR(data, key1, key2, key3):
    keys = [key1, key2, key3]
    z = 0
    listed = []
    for char in data:
        if (z == 3):
            z = 0
        if (z == 0):
            listed.append((ord(char) ^ keys[0]))
        elif (z == 1):
            listed.append((ord(char) ^ keys[1]))
        elif (z == 2):
            listed.append((ord(char) ^ keys[2]))
        z += 1
    return bytes(listed)
    

main()