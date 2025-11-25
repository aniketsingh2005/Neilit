import numpy as np
import pandas as pd

# s = pd.Series([1,2,3,4,5],index= ['a','b','c','d','e'])
# #retrieve the first element
# print(s['b'])

# s = pd.DataFrame()
# print(s)

# data = [1,2,3,4,5]
# df = pd.DataFrame(data)
# print(df)

# data ={'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,56,42]}
# df = pd.DataFrame(data)
# print(df)

# data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
# df = pd.DataFrame(data)
# print(df)

# d = {'one': pd.Series([1,2,3],index=['a','b','c']),
#      'two': pd.Series([1,2,3,4],index=['a','b','c','d'])}

# df =pd.DataFrame(d)
# print(df)

subject_marks_dict = {
        'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Math': [90, 75, 95, 60, 88],
        'Science': [85, 80, 90, 65, 92],
        'English': [92, 78, 88, 70, 85],
        'History': [88, 82, 91, 62, 90],
        'Art': [95, 70, 93, 68, 87]
    }
df_student_centric = pd.DataFrame(subject_marks_dict)
print(df_student_centric)

# d = { 'Students': pd.Series(['Pawan','Kunal','Indrajeet','Aniket','Sameer'],index=['1','2','3','4','5']),
#      'Maths': pd.Series([25,45,65,76,55],index=['1','2','3','4','5']),
#      'Hindi': pd.Series([25,47,65,76,55],index=['1','2','3','4','5']),
#      'Science': pd.Series([25,48,65,76,55],index=['1','2','3','4','5']),
#      'SST': pd.Series([25,49,65,76,55],index=['1','2','3','4','5']),
#      'English': pd.Series([25,49,65,76,55],index=['1','2','3','4','5'])}

# df = pd.DataFrame(d)
# print(df)