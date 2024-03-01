#!/usr/bin/env python
print("--------------------python data science------------")
#important libraries
#  numpy ->allows us to efficiently work with vectors,matrices and multidimential arrays.Crucial for linear algebra and numerical analysis.Basically replaces the primitive and inefficient python list.
# scipy ->very powerful library for scientific computing
# matplotlib ->used for plotting graphs and visualizing our data.It offers numerous types of plotting,styles and graphs.Visualizing is a key step in data science
# pandas ->This is the most high-level.It offers us a powerful data structure dataframe.we can use it to merge,reshape,filter and query our data.We can iterate over it and we can read and write into files like CSV,XLSV.Can work with databases

#   numpy arrays
import numpy as np
# creating arrays
a = np.array([10,20,30])
b = np.array([34,56,67])
print(a[0])
print(b[1])

aa = np.array([
    [10,34,45],
    [12,13,14]
    ])
print(aa)
print(aa[0][1])
print(aa[1][2])

mu = np.array([[
    [10,20,30,40],[8,8,2,1],[1,1,1,2]],
    [
        [9,9,2,39],[1,2,3,4],[0,0,3,2]],
    [
        [12,33,22,1],[22,1,22,2],[0,2,3,1]]
    ],dtype = float)
print('an example of a multidimentional 3X3X4 array:\n',mu)
# but we can print an array programmatically using the full function.An wxample of a 3x5x4 matrix
mu2 = np.full((3,5,4),7)
print('programmatically dimentional 3x5x4 array:\n',mu2)

zer = np.zeros((3,3))
print('zero array:\n',zer)
one = np.ones((2,3,4,2))
print('one array:\n',one)
emp = np.empty((4,4))
print('an empty array:\n',emp)
rand = np.random.random((2,3))
print('a random array:\n',rand)
# Ranges->instead of just filling arrays with the same values,we can fill create sequence of values by specifying the boundaries.we can use two different functions namely arange and linspace
ra = np.arange(10,50,5)
# function arange creates a list with values that range the minimum to maximum
print(ra)

#using linspace
# by using linspace we also create a list from a minimum value to a maximum value.But instead of specifying the step-size we specify the amout of values that we want to have in our list.They will spread evenly and have the same distance to their neighbors

rb = np.linspace(0,100,11)
print(rb)

#  NOT A NUMBER
# when importing big data packets into our application,there will sometimes be mussing data.Instead of just setting these values to zero we set them to NaN and then filter these data sets out
# attributes of arrays
# a.shape ->returns the shape of array(3,3) or (3,4,7)
# a.ndim ->returns how many dimensions our array has
# a.size ->returns the amount of elements an array has
# a.dtype ->returns the data type of the values in the array

# ARITHMETIC OPERATIONS IN ARRAYS
eg_arr = np.array([
    [1,4,2],
    [8,8,2]
    ])
print("The current array before any function is:{}\n".format(eg_arr))
print("Incrementing our array by 2 {}:\n".format(eg_arr +2))
print("decrementing our array by 2 {}:\n".format(eg_arr -2))
print("multiplying our array by 2 {}:\n".format(eg_arr * 2))
print("dividing the array by 2 {}:\n".format(eg_arr /2))

arr_1 = np.array([
    [1,2,3],
    [3,4,5]
    ])
arr_2 = np.array(
        [2,5,8])
print("combining two arrays becomes:{}\n".format(arr_1 + arr_2))

#  MATHEMATICAL FUNCTIONS
#  np.exp(a) ->Takes e to the power of each value
#  np.sin(a) ->returns the sine of each value
# np.cos(a) ->returns the cosine of each value
# np.tan(a) ->returns the tangent of each value
# np.log(a) ->returns the logarithm of each value
# np.sqrt(a) ->returns the square root of each value

# AGGREGATE FUNCTIONS
# a.sum() ->returns the sum of all values in the array
# a.min() ->returns the lowest value of the array
# a.max() ->returns the highest value of the array
# a.mean() ->returns the arithmetic mean of all the values in the array
# np.median(a) ->returns the median value of the array
# np.std(a) ->returns the standard deviation of values in the array

# MANIPULATING ARRAYS
# numpy offers us numerical ways which we can manipulate data of our arrays
ma = np.array([
    [4,2,9],
    [8,3,8]])
ma[1][2] = 7
print(ma)

# SHAPE MANIPULATION FUNCTIONS
# These functions allows us to restructure our arrays without changing their values
# a.reshape(x,y) ->returns an array with the same values structures in a different shape
# a.flatten() ->returns a flattened one-dimensional copy of the array
# a.ravel() ->dooes the same as flatten but works with the actual array instead of copy
# a.transpose() ->returns an array with the same values but swapped dimensions
# a.swapaxes() ->returns an array with same values but two swapped axes
# a.flat -> not a function but an interior of the flattened version of the array

#   JOINING FUNCTIONS
#  np.concatenate(a,b) ->joins multiple arrays along an existing axis
#  np.stack(a,b) ->joins multiple arrays along a new axis
#  np.hstack(a,b) ->stacks the arrays horizontally(column-wise)
# np.vstack(a,b) ->stacks the arrays vertically (row-wise)
# example
ca = np.array([10,20,30])
cb = np.array([20,20,10])
print('an example of a concatenated array:',np.concatenate((ca,cb)))
print('an example of a stacked array is:',np.stack((ca,cb)))

#concatenate joins the array together by just appending one into another.Stack creates additional axis that separates the two initial arrays

#  SPLITTING FUNCTIONS
# np.split(a,x) ->splits one array into multiple arrays
# np.hsplit(a,x) ->splits one array into multiple arrays horizontally(column-wise)
# np.vsplit(a,x) -<splits one array into multiple arrays vertically(row-wise)

sa = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
    [100,110,120]])

print('array above before splitting:\n',sa);
print('splitting the above array by two:\n',np.split(sa,2))
print('splitting the above array by four:\n',np.split(sa,4))

#   ADDING AND REMOVING ITEMS
#  np.resize(a,(x,y)) ->Returns a sized version of the array and fills empty spaces by repeating copies of a
#  np.append(a,[...]) ->Append values at the end of the array
#  np.insert(a,x,...) ->Insert a value at the index x of the array
#  np.delete(a,x,y) ->deletes axes of the array

#  LOADING AND SAVING ARRAYS
# talk about loading and saving Numpy arrays by intergrating Numpy format or CSV files

# using above array
print('an example of an array:',sa)
np.save('myarray.npy',sa) #saving the array
sa_load = np.load('myarray.npy')
print("loading the saved array:",sa_load)

#saving the array in csv format
np.savetxt('myarray.csv',sa)#this format is useful because it can be read by other applications and scripts
sa_load_csv = np.loadtxt('myarray.csv')
print('loading the saved csv array:\n',sa_load_csv)

#if we want to read in the CSV-fie that uses another separator than the default one,we can specify a certain delimiter
#sa_del = np.loadtxt('myarray.csv',delimiter =';')
#print('after using delimiter:\n',sa_del)



