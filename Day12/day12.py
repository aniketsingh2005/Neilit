import pandas as pd

dataset = pd.read_csv('Day12/Dataset.csv')
print(dataset)

# #printing the first five rows:
# print(dataset.head())

# #printing the last five rows:
# print(dataset.tail())

# #printing the info of our dataset:
# print(dataset.info())

# #printing the overall statistical data of dataset:
# print(dataset.describe())

# #printing the name of columns:
# print(dataset.columns)

# #printing the shape of dataset:
# print(dataset.shape)

# #printing the datatypes of columns:
# print(dataset.dtypes)

# #printing the index info of dataset:
# print(dataset.index)

# #printing the unique values in series:"column2 means the column name like 'land' , 'price'"
# print('\n',dataset["land"].unique())

# #printing the no. of occurances of unique values:
# print('\n',dataset["land"].value_counts())

# #print the mean value:
# print('\n',dataset["land"].mean())

# #print the median value:
# print('\n',dataset["land"].median())

print("hello world")