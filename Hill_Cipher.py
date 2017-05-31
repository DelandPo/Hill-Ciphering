import numpy as np
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
a = input().split()
while(len(a) != keySize * keySize):
    print("Please enter the valid key")
    a = input().split()
a = charArray(a)
y = np.array(a).reshape(keySize,keySize)
b = input().split()
if len(b)% keySize != 0 :
    for i in range(0,keySize - len(b)% keySize):
        b.append('#')
b = charArray(b[0:keySize])

plainText = np.array(b).reshape(keySize,1)
finalResult = np.matmul(y,plainText)
encryptedString = ""

for x in np.nditer(finalResult):
    a = x%26
    encryptedString += d[a]
print(encryptedString)

#def convertingString():


