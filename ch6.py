 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def main():
    inp1 = input("base64 file: ")
    f = open(inp1)
    content = f.read()
    KS = 2
    leastKS = 0
    leastDis = 100
    c = B64ToBytes(content)
    while (KS <= 40):
        c1 = c[0:KS]
        c2 = c[KS:KS*2]
        c3 = c[KS*2:KS*3]
        c4 = c[KS*3:KS*4]
        
        dis = (compHam(c1,c2)+compHam(c1,c3)+compHam(c2,c3)+compHam(c1,c4)+compHam(c2,c4)+compHam(c3,c4))/KS
        print(KS, dis)
        if (dis < leastDis):
            leastDis = dis
            leastKS = KS
        KS += 1
    print(leastKS, leastDis)
    
    
def compHam(h1, h2):
    inc = 0
    for i in range(len(h1)):
        xor = h1[i] ^ h2[i]
        while xor:
            inc += xor & 1
            xor >>= 1
    return inc
            
def B64ToBytes(b64):
    byts = bytearray()
    i = 0
    while i < len(b64):
        chunk = b64[i:i+4]
        i += 4
        
        while len(chunk) < 4:
            chunk += '='
        
        bits = 0
        chars = 0
        
        for j in range(4):
            c = chunk[j]
            if c == '=':
                val = 0
            else:
                chars += 1
                for k in range(64):
                    if (BASE64[k] == c):
                        val = k
                        break
            bits |= val << (18 - 6 * j)
        for j in range (chars - 1):
            byte = (bits >> (16 - 8 * j)) & 0xFF
            byts.append(byte)
    return byts
    
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