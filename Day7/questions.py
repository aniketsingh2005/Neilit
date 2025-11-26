

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
# data = np.array([
#     [78, 85, 88, 92, 81],
#     [67, 74, 69, 70, 75],
#     [90, 91, 85, 95, 89],
#     [56, 60, 62, 58, 64],
#     [88, 82, 79, 90, 87],
#     [73, 70, 72, 76, 78],
#     [65, 68, 70, 72, 66],
#     [92, 89, 94, 96, 90],
#     [80, 77, 75, 82, 79],
#     [69, 72, 71, 74, 73]
# ], dtype=np.int32)

# b. Display size and shape of the array.

# print(data.size)
# print(data.shape)

# c.Print sum of each column.

# print(np.sum(data,axis=0))

# d.Print maximum element from each column.

# print(np.max(data,axis=0))

# e. Print sum of 1,4,5row.

# print(np.sum(data[[1,4,5]],axis=1))

#5.	Create an array of size (3, 4) and reshape to (4, 3).

# col = np.array([[1,2,3,5],
#                 [2,3,4,6],
#                 [5,6,7,5]])

# recol = col.reshape(4,3)
# print(recol)

#6.	Create an empty array of size (3, 3).

# emp = np.empty((3,3))
# print(emp)

#7.	Create an array using a list.

# list_python = [1,2,3,4,5]

# my_array = np.array(list_python)
# print(my_array)

# 8.Create a new array using tuple.

# my_tup = (2,3,4,5,6)

# array_tup = np.array(my_tup)
# print(array_tup)
# print(type(array_tup))

#9.	Create an array for a given range of elements between 2 to 40 step by 3.

# d = np.arange(2,40,3,dtype=int)
# print(d)

#10.	Create an evenly spaced array of 10 values between 5 to 35.

# e = np.linspace(5,35,num=10)
# print(e)

#11.

# arr = np.array([1.2345, 2.6789, 3.14159, 4.0001, 5.9999, 6.7654, 7.8901, 8.5432, 9.1111, 10.0000])

# r = np.round(arr,decimals=2)
# print(r)

#12.Write a python program to print the floor values of above array.

# my_array = np.array([-1.6, -0.3, 0.1, 1.4, 2.0, -5.7])
# fl = np.floor(my_array)
# print(fl)

# 13.	Write a python program to print the ceiling values of above array.

# my_ceil = np.array([-1.6, -0.3, 0.1, 1.4, 2.0, -5.7])
# ce = np.ceil(my_ceil)
# print(ce)

#14.

# arr = np.array([[23,45,66,76],[54,76,77,55],[23,43,44,33],[44,77,66,44]])

# mxmum = np.max(arr,axis=0)
# mxmum1 = np.max(arr,axis=1)

# print("The maximum no. in column is:",mxmum)
# print("The maximum no. in row is:",mxmum1)

# mnmum = np.min(arr,axis=0)
# mnmum1 = np.min(arr,axis=1)

# print("The minimum no. in column is:",mnmum)
# print("The minimum no. in row is:",mnmum1)

# rows, cols = arr.shape
# print(f"Array shape (rows, columns): {arr.shape}")
# print(f"Row index range: 0 to {rows - 1}")
# print(f"Column index range: 0 to {cols - 1}")

#15.	Print 10th, 30th, 60th, 75th and 90th percentile for each columns of above array. 

# Create a sample NumPy array
# data = np.array([[10, 20, 30, 40],
#                  [5, 15, 25, 35],
#                  [12, 22, 32, 42],
#                  [8, 18, 28, 38],
#                  [1, 11, 21, 31]])

# Define the percentiles to calculate
# percentiles = [10, 30, 60, 75, 90]

# Calculate the percentiles for each column (axis=0)
# column_percentiles = np.percentile(data, percentiles, axis=0)

# Print the results
# for i, p in enumerate(percentiles):
#     print(f"{p}th percentile for each column: {column_percentiles[i]}")

#16.Print median and mean of a (5,3) array. Also print the mean of each row and column.

# cd = np.array([[10, 20, 30,],
#                  [5, 15, 25,],
#                  [12, 22, 32,],
#                  [8, 18, 28,],
#                  [1, 11, 21,]])

# #Printing the mean of arrays.
# mn = np.mean(cd)
# print(mn)

# #Printing the median of arrays.
# mdn = np.median(cd)
# print(mdn)

# #Printing the mean of only rows.
# rmn = np.mean(cd,axis=1)
# print(rmn)

# #Printing the mean of only columns.
# cmn = np.mean(cd,axis=0)
# print(cmn)

# Sort the above array column wise.

# arr = np.array([[10, 20, 30,],
#                  [5, 15, 25,],
#                  [12, 22, 32,],
#                  [8, 18, 28,],
#                  [1, 11, 21,]])

# #Printing the sorted array in column wise:
# print("\nSorted array in column wise:")
# sorted_array = np.sort(arr,axis=0)
# print(sorted_array)


# #Printing the sorted array in row wise:
# print("\nSorted array in row wise:")
# sorted_array1 = np.sort(arr,axis=1)
# print(sorted_array1)

#18.

#a.	Enter 5 records randomly.

# carr = [("id",int),
#         ("name",object),
#         ("salary",int)]

# carr_data = np.array([(1,"Aniket",55000),
#                      (2,"Kunal",60000),
#                       (3,"Sujal",74000),
#                      (4,"Pawan",20000),
#                      (5,"Amit",56000)],dtype=carr)

# print("Original array :")
# print(carr_data)

# #b.	Sort the array.

# sorted_name = np.sort(carr_data,order="name")
# print("\nSorting defaultly with name.")
# print(sorted_name)

# sorted_salary = np.sort(carr_data,order="salary")
# print("\nSorting defaultly with salary.")
# print(sorted_salary)

# sorted_default = np.sort(carr_data,order="id")
# print("\nSorting defaultly with id.")
# print(sorted_default)

# # 19.Print the index of sorted array. 

# index_id = np.argsort(carr_data["id"])
# print("\nIndex of array elements after sorted through id:",index_id)

# index_name = np.argsort(carr_data["name"])
# print("\nIndex of array elements after sorted through name:",index_name)

# index_salary = np.argsort(carr_data["salary"])
# print("\nIndex of array elements after sorted through salary:",index_id)





