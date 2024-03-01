#!/usr/bin/env python
print('-----------------------pandas projects-----------------')
import pandas as pd
import numpy as np
series = pd.Series([10,20,30,40],['A','B','C','D'])
print(series)
print(series['C'])
print(series[1])

#  CONVERTING DICTIONARIES
myDict = { 'E':10,'F':50,'G':90}
s1 = pd.Series(myDict,index=['X','Y','Z'])
print(s1)

#  PANDAS DATA FRAME
#  while series is one dimentional,data frame is a multidimentional and looks like a table eg
data = {'Name':['Anna','Bob','Carol','Daniel','Evan','Fiona','Gerald','Henry'],
        'Age':[20,23,34,45,33,54,55,25],
        'Height':[176,150,175,182,176,189,165,187]}
df = pd.DataFrame(data)
print('a complete dataframe becomes:\n',df)

# To acccess various columns and rows
print('accessing Bob details:\n',df[['Name','Age','Height']])
# Basic Functions and Attributes
print('Transpossing our datarame:\n',df.T)
#print('Displaying the types:\n',df.type)
print('Displaying the number of dimentions:\n',df.ndim)
print('Displaying the shape:\n',df.shape)
print('Displaying the size:\n',df.size)
print('Displaying the first Two rows:\n',df.head(2))
print('Displaying the last two rows:\n',df.tail(2))

# STSTISTICAL FUNCTIONS
print('Counting the number of non-null elements:\n',df.count())
print('returning the sum of values elements:\n',df.sum())
print('Counting the arithmetic mean of  elements:\n',df.mean())
print('returning the arithmetic median elements:\n',df.median())
print('returning the arithmetic mode of elements:\n',df.mode())
print('returning the standard deviation of elements:\n',df.std())
print('returning the minimum of elements:\n',df.min())
print('returning the maximum element:\n',df.max())
print('returning the absolute value among elements:\n',df['Height'].abs())
print('returning the product of selected elements Height {}:'.format(df['Height'].prod()))
print('returning all statistical setails of elements:\n',df.describe())



#  APPLYING NUMPY FUNCTIONS
print(df['Age'].apply(np.sin))

# APPLYING LAMBDA EXPRESSIONS
print(df['Age'].apply(lambda x:x*100))
# Lambda is a very powerful library they can be thought of as nameless function that we pass as a parameter
# By using the keyword lambda we create a temporary variable that represents the individual values that we are applying the operation into.After the colon,we define whta we want to do.In this case we multiply all values of column age by 100

df_comb = df[['Age','Height']]
print(df_comb.apply(lambda x:x.max() - x.min()))



# ITERATING OVER DATA FRAMES
for x in df['Age']:
    print(x)

# others
# iteritems() ->iterator for key-value pairs
# iterrows() ->iterator for the rows(index,series)
# itertuples() ->iterator for the rows as named tuples

for key,value in df.iteritems():
    print('{}: {}'.format(key,value))

# we use the iteritems function to iterate over key-value pairs

for index,value in df.iterrows():
    print(index,value)


# SORTING
# SORT NY INDEX
df_rand = pd.DataFrame(np.random.rand(10,2),
        index = [1,5,3,6,7,2,8,9,0,4],
        columns = ['A','B'])
print(df_rand.sort_index())


# INPLACE PARAMETER
# When we use functions that manipulate our data frame,we dont't actually change it but we return a manipulated copy.If we wanted to apply the changes on the actual data frame,we need to

df_sorted = df_rand.sort_index()

# pandas offers us another alternatives as well.This alternative is the parameter inplace.When this parameter is set to TRUE,the changes get applied in our actual data frame

df_sorted.sort_index(inplace = True)


# SORT BY COLUMNS
data = {'Name':['Anna','Bob','Carol','Daniel','Evan','Fiona','Gerald','Henry'],
                'Age':[20,23,34,45,33,54,55,25],
                        'Height':[176,150,175,182,176,189,165,187]}
df = pd.DataFrame(data)
print('a complete dataframe becomes:\n',df)
df.sort_values(by=['Age','Height'],inplace=True)
print(df)


#  JOINING AND MERGING
names = pd.DataFrame({
    'id':[1,2,3,4,5,6],
    'name':['Ann','Bob','Charles','Daniel','Evan','Fiona'],
    })
ages = pd.DataFrame({
    'id':[1,2,3,4,5,7],
    'age':[20,30,40,50,60,70]
    })
# when we have two separate data frames which are related to one another,we can combine them into one data frame.Important that we have a common column that we can merge on.In this case this is id
df_merged = pd.merge(names,ages,on='id')
df_merged.set_index('id',inplace=True)

#we use the method merge and specify the column to merge on.We then have a new data frame with the combined data but we also want our id column to be the index.For this,we use the set_index method
print('merged dataframe now becomes:\n',df_merged)

# JOINS
# left join()->uses all keys from left object and merges with right
# right join() ->uses all keys from right object and merges with left
# outer join() ->uses all keys from both objects and merges them
# inner join() ->uses only the keys which both objects have and merges them

# when we use the left join,we get all the keys from the names data frame but not the additional index 7 from ages.This also means that Fiona wount be assigned any age
df_leftjoin = pd.merge(names,ages,on='id',how='left')
df_leftjoin.set_index('id',inplace=True)
print('left joined dataframe becomes:\n',df_leftjoin)

# if we now perform the default inner join,we end up with same data frame as in the beginning.
df_innerjoin = pd.merge(names,ages,on='id',how='inner')
df_innerjoin.set_index('id',inplace=True)
print('inner jointed dataframe becomes:\n',df_innerjoin)

# if we now perform the default inner join,we end up with same data frame as in the beginning.

df_rightjoin = pd.merge(names,ages,on='id',how='right')
df_rightjoin.set_index('id',inplace=True)
print('right jointed dataframe becomes:\n',df_rightjoin)

# performed the right join

df_outerjoin = pd.merge(names,ages,on='id',how='outer')
df_outerjoin.set_index('id',inplace=True)
print('outer jointed dataframe becomes:\n',df_outerjoin)

# QUERYING DATA
#like in databases with SQL,we can also query data from our data frames in pandas.For this,
data = {'Name':['Anna','Bob','Carol','Daniel','Evan','Fiona','Gerald','Henry'],
                'Age':[20,23,34,45,33,54,55,25],
                        'Height':[176,150,175,182,176,189,165,187]}
df = pd.DataFrame(data)
print('a complete dataframe becomes:\n',df)
print(df.loc[df['Age'] == 34])
print(df.loc[(df['Age'] >34) & (df['Height'] >180)])
print(df.loc[df['Age'] >40]['Name'])


