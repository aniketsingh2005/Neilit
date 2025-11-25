import numpy as np

# Numpy Broadcasting :

# a = np.array([[1,2,3,4],[2,4,5,6],[7,8,9,0]])
# b = np.array([1,2,3,4])
# sum= a+b
# print(sum)

# Numpy array Broadcasting :

a = np.array([[1,2,3,4],[4,5,6,7],[6,7,8,9]])
print("Printing array:")
print(a)

print("Iterating over the array:")
for x in np.nditer(a):
    print(x,end = ' ')



