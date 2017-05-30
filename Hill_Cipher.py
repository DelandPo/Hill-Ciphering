import numpy as np
a = [int(x) for x in input().split()]
y = np.array(a).reshape(2,2)
print(np.linalg.det(y))
print(np.linalg.inv(y))