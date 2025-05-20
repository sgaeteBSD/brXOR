# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    inp = input("Enter 1: ")
    inp2 = input("Enter 2: ")
    
    print("")
    
    a = hexToBytes(inp)
    b = hexToBytes(inp2)
    
    i = 0
    finBytes = []
    while (i < len(a)): #equal length buffers
        finBytes.append(a[i] ^ b[i])
        i += 1
    
    print(bytesToHex(finBytes))
    
def hexToBytes(hx):
    
    byteData = bytes.fromhex(hx)
    byteList = []
    
    i = 0
    while i < len(byteData):
        byteList.append(byteData[i])
        i += 1
    
    return byteList

def bytesToHex(byts):
    return (bytes(byts)).hex()

main()