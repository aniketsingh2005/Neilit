import pandas as pd

# d = {'one':pd.Series([1,2,3],index=['a','b','c']),
#      'two': pd.Series([1,2,3,4],index=['a','b','c','d'])}

# df = pd.DataFrame(d)
# print(df['two'])

# # addition of columns:
# df['three']=pd.Series([10,20,30],index=['a','b','c'])
# print(df)

# #addition of columns using existing columns:
# print("Adding a new column using the existing columns")
# df['four'] = df['one']+df['three']
# print(df)


# d = {'one':pd.Series([1,2,3],index=['a','b','c']),
#      'two': pd.Series([1,2,3,4],index=['a','b','c','d']),
#      'three':pd.Series([10,20,30],index=['a','b','c'])}

# df = pd.DataFrame(d)
# print("Our DataFrame is:")
# print(df)

# print("Deleting the first column using DEL function.")
# del df['one']
# print(df)

# print("Deleting another column using pop function:")
# df.pop('two')
# print(df)

# d = {'Age':[30,40,43,23,43,32,28],
#      'Color':['Blue','Green','Red','yellow','Grey','Black','White'],
#      'Food':['Steak','Pasta','Mango','Apple','Cheese','Melon','Beans'],
#      'Height':[165,154,134,167,156,189,176],
#      'Score':[4.5,5.4,5.6,8.9,8.7,7.7,6.5],
#      'State':['NY','YU','UY','UI','YU','PO','II'],
#      }
# df = pd.DataFrame(d,index=['Jane','Nick','Aaron','Penelope','Kunal','Aniket','Amit'])
# print(df)
# print("Retrieving the values for Nick")
# print(df.loc['Nick'])     





