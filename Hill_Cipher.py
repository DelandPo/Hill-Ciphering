import numpy as np
keySize = int(input("Enter the size of the N X N Matrix for the Key :: "))
a = [int(x) for x in input().split()]
while(len(a) != keySize * keySize):
    print("Please enter the key")
    a = [int(x) for x in input().split()]
y = np.array(a).reshape(2,2)
print(np.linalg.det(y))
print(np.linalg.inv(y))
print(keySize)