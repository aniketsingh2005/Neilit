import pandas as pd
import numpy as np

#1. Create a Pandas Series from a Python list: [10, 20, 30, 40, 50]. Print the series.

# lst = [10,20,30,40,]
# a = pd.Series(lst,index=[1,2,3,4])
# print(a)

# 2. Create a Series with custom indexes: values [100, 200, 300], index ['a', 'b', 'c'].

# d = pd.Series([100,200,300],index=['a','b','c'])
# print(d)

# 3.Print the first 2 and last 2 elements of a Series s.

# data = np.arange(10,20)
# s = pd.Series(data,index = [f'Index {i}' for i in range(10)])

# print("\nThe first two element is :")
# print(s.head(2))

# print("\nThe last two element is :")
# print(s.tail(2))

# 4. Given a Series s = pd.Series([5, 10, 15, 20, 25]), find the max, min, and sum.

# s = pd.Series([5, 10, 15, 20, 25])

# print("\nThe maximum no in series is:")
# print(max(s))

# print("\nThe minimum no in series is:")
# print(min(s))

# print("\nThe sum of elements of series is:")
# print(sum(s))


# 5. Convert a dictionary {'Math': 90, 'Science': 85, 'English': 88} into a Series.

# dic = {'Math': 90, 'Science': 85, 'English': 88}
# s = pd.Series(dic)

# print(s)

# 6. Create a DataFrame with: name ['Amit', 'Riya', 'Kiran'], age [20, 19, 21], marks [85, 92, 76].

# data = {'name': ['Amit','Riya','Kiran'],
#         'age': [20,19,21],
#         'marks' : [85,92,76]}

# data_frame = pd.DataFrame(data,index=[1,2,3])
# # print(data_frame)

# 7. From the above DataFrame, select only the name and marks columns.

# selected_columns_df = data_frame[['name','marks']]
# print('\n',selected_columns_df)

#8. Add a column 'grade' with values ['A', 'A+', 'B'].

# data_frame['grade'] = ['A','A+','B']
# print('\n',data_frame)

#9. Filter rows where marks > 80.

# filtered_df = data_frame[data_frame['marks'] > 80]
# print("\nFiltered DataFrame (marks > 80):")
# print(filtered_df)


# 10. Sort the DataFrame by age in descending order.

# print(data_frame.sort_values('age',ascending=False))


# 11. Load a CSV file named 'students.csv' and print the first 5 rows.

# data = pd.read_csv('Day12/student.csv')
# print(data.head(5))
# print(data.head(2))

# 12. After loading 'students.csv', check the column names using df.columns.

# print(data.columns)

# 13. Load a CSV and check how many rows & columns it has.

# print(data.shape,"The first one is row and the another one is column .")

# 14. Load a CSV and rename column marks ® score.

# data = data.rename(columns={'Marks':'Score'})
# print(data)

# 15.Load a CSV and drop a column called 'age'.
# data.drop('Age', axis=1,inplace=True)
# print(data)
