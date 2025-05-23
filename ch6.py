 # -*- coding: utf-8 -*-
"""
Santiago Gaete
Break Repeating XOR (Set 1 Challenge 6)
5/23/2025
"""

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
CHARS = " !#$%&\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]\^_`abcdefghijklmnopqrstuvwxyz{|}~"

def main():
    inp1 = input("base64 file: ")
    f = open(inp1, 'r')
    content = f.read()
    
    KS = 2 #from 2 to 40
    leastKS = 0 #init
    leastDis = 100 #init
    content = cleanB64(content) #CLEAN OUT NEWLINES & NON-B64
    c = B64ToBytes(content) #bytes
    
    while (KS <= 40):
        #chop up into 4 blocks
        c1 = c[0:KS]
        c2 = c[KS:KS*2]
        c3 = c[KS*2:KS*3]
        c4 = c[KS*3:KS*4]
        
        #average hamming distance
        dis = (compHam(c1,c2) + compHam(c1,c3) + 
                compHam(c2,c3) + compHam(c1,c4) + 
                    compHam(c2,c4)+compHam(c3,c4)) / KS / 6
        
        #print for fun
        print(KS, dis)
        
        #update leastDis and leastKS if its smallest
        if (dis < leastDis):
            leastDis = dis
            leastKS = KS
        KS += 1 #increment
    
    #print final least
    print(leastKS, leastDis)
    
    #pre-transpose blocks of leastKS size
    bc = []
    for i in range(len(c) // leastKS): #integer division
        if (i > 0):
            bc.extend([c[(leastKS * i):(leastKS * i) + leastKS]])
        else: #for the first case
            bc.extend([c[0:leastKS]])
    
    #transpose blocks
    tp = []
    for i in range(leastKS):
        block = [b[i] for b in bc if i < len(b)]
        tp.append(block)
    
    key = []
    for i in range(len(tp)):
        bk, _, _ = scoreConvert(tp[i])
        key.append(bk) #add found key character
    
    print()
    print(key)
    print(bytesToASCII(key)) #key found to be Terminator X: Bring the noise
    print()
    
    decrypt = repeatXOR(c, *key)
    print(bytesToASCII(decrypt))
    
def compHam(h1, h2):
    inc = 0
    for i in range(len(h1)):
        xor = h1[i] ^ h2[i]
        while xor:
            inc += xor & 1
            xor >>= 1
    return inc
           
def cleanB64(b64):
    cleaned = ''
    for c in b64:
        if c in BASE64 or c == '=':
            cleaned += c
    return cleaned
    
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
                val = 0
                for k in range(64):
                    if (BASE64[k] == c):
                        val = k
                        break
            bits |= val << (18 - 6 * j)
            
        for j in range (chars - 1):
            byte = (bits >> (16 - 8 * j)) & 0xFF
            byts.append(byte)
            
    return bytes(byts)
    
def bytesToASCII(byts):
    return bytes(byts).decode("ascii", errors="ignore")

def ASCIIToBytes(stri):
    return stri.encode("ascii", errors="ignore")

def repeatXOR(data, *keys):
    z = 0
    listed = []
    for char in data:
        key = keys[z % len(keys)]
        listed.append(char ^ key)
        z += 1
    return bytes(listed)

def scoreConvert(byts):
    highScore = 0
    bestResult = []
    bestKey = None
    
    for char in CHARS:
        key = ord(char)
        xored = singleXOR(byts, key)
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
    return bestKey, bestResult, highScore 

def singleXOR(data, key):
    return bytes([b ^ key for b in data])

main()