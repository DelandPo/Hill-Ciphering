import numpy as np

def convertingString(b,keySize,y):
    encryptedString = ""
    plainText = np.array(b).reshape(keySize,1)
    finalResult = np.matmul(y,plainText)
    for x in np.nditer(finalResult):
        a = x%26
        encryptedString += d[a]
    return encryptedString
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def matrix_cofactor(matrix):
    return np.linalg.inv(matrix).T * np.linalg.det(matrix)

def charArray(j):
    list1 = []
    codelist = "abcdefghijklmnopqrstuvwxyz"     # add it later on 0123456789!\"#$%&\'()*
    text = [q.lower() for q in j]
    try:
        for i in text:
            x = codelist.index(i)
            list1.append(x)
        return list1
    except:
        print("\n"*60)
        print("\nThat is not a valid input, try again. An Illegal Character Was Detected!\n")
        value = input("Press any key to return to the main menu...")

l = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
r = [l.index(val) for val in l]
d = dict(zip(r, l))
keySize = int(input("Enter the size of the N X N Matrix for the Key :: "))
nValue = keySize
a = input().split()
while(len(a) != keySize * keySize):
    print("Please enter the valid key")
    a = input().split()
a = charArray(a)
y = np.array(a).reshape(keySize,keySize)
b = input().split()
if len(b)% keySize != 0 :
    for i in range(0,keySize - len(b)% keySize):
        b.append('K')
i = 0
cipheredText = ""
while keySize <= len(b):
    c = charArray(b[i:keySize])
    cipheredText = cipheredText + convertingString(c,nValue,y)
    i = keySize
    keySize = keySize + nValue 
print(cipheredText)
print(y)
## Decryption Part
keyDeterminant = np.linalg.det(y)
print(keyDeterminant)
ax = matrix_cofactor(y)

print(b)
a = modinv(int(keyDeterminant),26)
b = np.array(ax).reshape(2,2)
print(3 * b)

keySize = nValue
j = 0
decipheredText = ""
while keySize <= len(keyInverse):
    c = charArray(b[j:keySize])
    decipheredText = decipheredText + convertingString(c,nValue,keyInverse)
    j = keySize
    keySize = keySize + nValue 
print(decipheredText)


