import numpy as np
# a = np.array([1,2,3,4,5])
# print(a)

# b = np.array([[[1,2,3,],[4,5,6]],[[2,3,5],[3,5,6]]])
# print(b)

c = np.array([[1,2,3,8],[4,5,6,7],[9,2,4,5]])
print(c.itemsize)
print(c.dtype)
print(c.shape)
print(c.size)
print(c.reshape(4,3)) 