# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

CHARS = " !#$%&\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]\^_`abcdefghijklmnopqrstuvwxyz{|}~"

def main():
    inp = input("Enter string: ")

    print("")
    
    a = hexToBytes(inp)
    
    key, result = scoreConvert(a)
     
    print(bytesToASCII(result))
    
def hexToBytes(hx):
    return list(bytes.fromhex(hx))

def bytesToHex(byts):
    return (bytes(byts)).hex()
    
def bytesToASCII(byts):
    return bytes(byts).decode("ascii")
    
def scoreConvert(byts):
    highScore = 0
    bestResult = []
    bestKey = None
    
    for char in CHARS:
        key = ord(char)
        xored = [b ^ key for b in byts]
        decoded = bytesToASCII(xored)
    
        score = 0
        for c in decoded:
            if c.islower():
                score += 2
            elif c.isupper():
                score += 1
            elif c == ' ':
                score += 1
            elif c in ".,!?":
                score += 0.5
            elif c.isdigit():
                score -= 1
            else:
                score -= 0.5
        if score > highScore:
            highScore = score
            bestResult = xored
            bestKey = key
    return bestKey, bestResult

main()