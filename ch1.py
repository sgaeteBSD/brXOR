# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import base64
import binascii

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def main():
    inp = input("Enter hex: ")
    print("")
    a = hexToBytes(inp)
    print(''.join(bytesToBase64(a)))
    
def hexToBytes(hx):
    byteData = bytes.fromhex(hx)
    return byteData

#def base64ToBytes(b64):


#def bytesToHex(byts):


def bytesToBase64(byts):
    b64 = []
    i = 0
    while i < len(byts):
        #modbyt = byte & 0x0F
        #modlit.append(modbyt)
        chunk = byts[i:i+3]
        i += 3
        bits = 0
        squash = 3 - len(chunk)
        
        for j in range(len(chunk)): #
            bits = bits | (chunk[j] << (16 - 8 * j)) 
        bits = bits << (squash * 8) #shift to fit 24-bit
        
        for j in range(4):
            #if j >= len(chunk) + 1:
             #   b64.append('=')
            #Get 6-bit alone
            sixbit = (bits >> (18 - 6*j)) & 63
            #Convert to base64 index
            b64.append(BASE64[sixbit])
    return b64

main()
