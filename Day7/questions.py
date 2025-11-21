

import numpy as np
#1.
# one = np.array([[1,2,3],[5,7,6],[9,7,8]])
# two = np.array([[1,2,3],[5,7,6],[9,7,8]])

# print(one+two)
# print(one*two)

#2.
# num = np.array([2,3,4,5,6,7,8,9,0,1])

# sqr = np.sqrt(num)
# print(sqr)

# dev = np.std(num)
# print(dev)

#3.
# print(one.itemsize)
# print(one.shape)

# print(two.itemsize)
# print(two.shape)

# print(num.itemsize)
# print(num.shape)

#4.
#a.	Insert at least 10 rows in the above array.
data = np.array([
    [78, 85, 88, 92, 81],
    [67, 74, 69, 70, 75],
    [90, 91, 85, 95, 89],
    [56, 60, 62, 58, 64],
    [88, 82, 79, 90, 87],
    [73, 70, 72, 76, 78],
    [65, 68, 70, 72, 66],
    [92, 89, 94, 96, 90],
    [80, 77, 75, 82, 79],
    [69, 72, 71, 74, 73]
], dtype=np.int32)

# b. Display size and shape of the array.

# print(data.size)
# print(data.shape)

# c.Print sum of each column.

# print(np.sum(data,axis=0))

# d.Print maximum element from each column.

# print(np.max(data,axis=0))

# e. Print sum of 1,4,5row.

print(np.sum(data[[1,4,5]],axis=1))