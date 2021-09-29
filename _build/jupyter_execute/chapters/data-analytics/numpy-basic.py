#!/usr/bin/env python
# coding: utf-8

# # NumPy tutorial
# [`NumPy`](http://www.numpy.org/) is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.

# In this tutorial, we will cover:
# 
# * `Numpy`: Array, Array indexing, Array math & Boardcasting.
# 
# To use NumPy, we need to import the `numpy` package at first:

# In[1]:


import numpy as np
print(np.__version__)


# ## Array
# A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension.

# We can initialize `numpy` arrays from nested Python lists using the `array` function, and we can access elements using square brackets with interger indexing. Each `numpy` array has several attributes that allow us to know some basic information about it, such as `ndim` for the number of dimnsions of the array and `shape` for the sizes of all dimensions.

# In[2]:


a = [1, 2, 3]
a = np.array(a)  # Create a rank 1 array from a list
print(a, a.ndim, a.shape)
print(a[0], a[-1])  # Access 1st and last elements


# In[3]:


b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # Create a rank 2 array
print(b, b.shape, b[1, 2])
c = np.array([[[111, 112, 113, 114], [121, 122, 123, 124]],
              [[211, 212, 213, 214], [221, 222, 233, 234]],
              [[311, 312, 313, 314], [321, 322, 323, 324]]])
                                            # Create a rank 3 array
print(c, c.shape, c[0, 1, 1])


# Numpy also provides many functions to create arrays for specific purposes.

# In[4]:


d = np.zeros((2,2))   # Create an array of all zeros
d = np.ones((1,2))    # Create an array of all ones
d = np.full((2,2), 7) # Create a constant array
d = np.eye(2)         # Create a identity square matrix
d = np.random.random((2,2)) # Create an array filled with random values


# ## Array indexing
# 
# `NumPy` offers several ways to pull out a section of arrays. The most common ways include **slicing**, **integer array indexing** and **Boolean array indexing**. We may choose the appropriate indexing methods for different purposes.

# + ***Slicing***
# 
# Similar to Python lists, numpy arrays can be sliced into a subarray. Since arrays may be multidimensional, you must specify a slice for each dimension of the array.

# In[5]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[:2, 1:3])  # Slice 1st to 2nd rows and 2nd to 3rd columns
print(a[:, ::2])   # Slice all odd columns


# Note that a slice of an array is a view into the same data, so modifying it will modify the original array.

# In[6]:


b = a[:2, 1:3]
print(a[0, 1])
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])


# + ***Integer array indexing***
# 
# When you index into numpy arrays using slicing, the resulting array will always be a subarray of the original array. In contrast, integer indexing allows you to index arbitrary elements in the array by separately assign the indexing for each dimension. Note that as the resulting array in this way is not subarray, modifying it will **not** modify the original.

# In[7]:


a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(a)
print(a[[0, 1, 2], [0, 1, 0]]) # Integer indexing

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))


# This method is useful when we want to conduct an operation on a series of specific elements in the array.

# In[8]:


# Create arrays for indices of rows and columns separately
row = np.arange(4)           # [0, 1, 2, 3]
col = np.array([0, 2, 0, 1])

# Select one element from each row using the indices in col
print(a[row, col])      # Integer indexing
a[row, col] += 10       # Only operate on specific elements
print(a)


# You can also mix integer indexing with slice indexing to obtain a subarray. However, note that mixing yields an array of lower rank, while using only slices yields an array of the same rank as the original array.

# In[9]:


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_r1 = a[1, :]    # Mix integer indexing with slice indexing
row_r2 = a[1:2, :]  # Slice indexing
row_r3 = a[[1], :]  # Slice indexing
print(row_r1, row_r1.shape)  # Lower rank
print(row_r2, row_r2.shape)
print(row_r3, row_r3.shape)


# + ***Boolean array indexing***
# 
# Boolean array indexing lets you pick out arbitrary elements of an array. Frequently this type of indexing is used to select the elements of an array that satisfy some conditions.

# In[10]:


a = np.array([[1, 2], [3, 4], [5, 6]])

bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                    # this returns a numpy array of Booleans of the same
                    # shape as a, where each slot of bool_idx tells
                    # whether that element of a is > 2.

print(bool_idx)
print(a[bool_idx])  # Boolean array indexing to construct a rank 1 array for True values 


# We can do all of the above in a single concise statement.

# In[11]:


print(a[a > 2])


# For brevity we have left out a lot of details about numpy array indexing; if you want to know more you should read the [documentation](https://numpy.org/doc/stable/reference/arrays.indexing.html).

# ## Datatypes
# 
# Every numpy array is a grid of elements of the same type. `NumPy` provides a large set of numeric datatypes that you can use to construct arrays. `NumPy` tries to guess a datatype when you create an array, but functions that construct arrays usually also include an optional argument to explicitly specify the datatype.

# In[12]:


a = np.array([1, 2])      # Let numpy choose the datatype
b = np.array([1, 2.0])    # Let numpy choose the datatype
c = np.array([1, 2], dtype=np.int64)  # Force a particular datatype

print(a.dtype, b.dtype, c.dtype)


# You can read all about `numpy` datatypes in the [documentation](http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html).

# ## Array math

# Basic mathematical functions operate elementwise on arrays, and are available both as operator overloads and as functions in the numpy module:

# In[13]:


x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Elementwise sum; both produce the array
print(x + y)
print(np.add(x, y))


# In[14]:


# Elementwise square root; produces the array
print(np.sqrt(x))
# Elementwise natural logarithm; produces the array
print(np.log(x))


# `NumPy` also supports matrix multiplication. We use the `dot` function to compute inner products of vectors, to multiply a vector by a matrix, and to multiply matrices. `dot` is available both as a function in the numpy module and as an instance method of array objects:

# In[15]:


v = np.array([9, 10])
w = np.array([11, 12])

# Inner product of vectors
print(v.dot(w))
print(np.dot(v, w))


# In[16]:


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# Matrix / matrix product
print(x.dot(y))
print(np.dot(x, y))


# You can also use the `@` operator which is equivalent to `dot` operator.

# In[17]:


print(v @ w)
print(x @ y)


# Apart from computing mathematical functions using arrays, we frequently need to manipulate the shape of arrays, such transposing a matrix or converting to one dimension. To transpose a matrix, simply use the `T` attribute of an array object. To manipulate the shape of arrays, simply use the `reshape` funcion.

# In[18]:


print(x)
print("transpose\n", x.T)
print("reshape\n", x.reshape(4))


# In[19]:


v = np.array([[1, 2, 3, 4]])  # Note that dimensions matter when transpose
print(v)
print("transpose\n", v.T)


# `Numpy` provides many useful functions for performing computations on arrays; one of the most useful is `sum`:

# In[20]:


x = np.array([[1, 2], [3, 4]])

print(np.sum(x))          # Compute sum of all elements
print(np.sum(x, axis=0))  # Compute sum of each column
print(np.sum(x, axis=1))  # Compute sum of each row


# You can find the full list of mathematical functions provided by `numpy` in the [documentation](http://docs.scipy.org/doc/numpy/reference/routines.math.html).

# ## Broadcasting

# Broadcasting is a powerful mechanism that allows `numpy` to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operations on the larger array.
# 
# For example, suppose that we want to add a constant vector to each row of a matrix. At the very begining, we may use a loop to do operations for each element as follows.

# In[21]:


# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, -1])

# Add the vector v to each row of the matrix x with an explicit loop
y = np.empty_like(x)  # Create an empty matrix with the same shape as x
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)


# This works; however computing an explicit loop in Python could be slow, especially when `x` is very large. In `numpy`, we could use its elementwise math operations: forming a matrix `vv` by stacking multiple copies of `v` vertically, then performing elementwise addition of `x` and `vv`.

# In[22]:


vv = np.tile(v, (4, 1))  # Stack 4 copies of v on top of each other
print(vv)
y = x + vv  # Add x and vv elementwise
print(y)


# Even more conveniently, `Numpy` **broadcasting** allows us to perform this computation within one step.

# In[23]:


y = x + v  # Add v to each row of x using broadcasting
print(y)


# The line `y = x + v` works even though `x` has shape `(4, 3)` and `v` has shape `(3,)` due to broadcasting; this line works as if v actually had shape `(4, 3)`, where each row was a copy of `v`, and the sum was performed elementwise.
# 
# Broadcasting two arrays together follows these rules:
# 
# 1. If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.
# 2. The two arrays are said to be compatible in one dimension if they have the same size in this dimension, or if one of the arrays has size 1 in that dimension.
# 3. The arrays can be broadcast together if they are compatible in all dimensions.
# 4. After broadcasting, each array behaves as if it had a shape equal to the elementwise maximum of shapes of the two input arrays.
# 5. In any dimension where one array had size 1 and the other array had size greater than 1, the first array behaves as if it were copied along that dimension
# 
# If this explanation does not make sense, try reading the explanation from the [documentation](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) or this [explanation](http://wiki.scipy.org/EricsBroadcastingDoc).
# 
# Functions that support broadcasting are known as universal functions. You can find the list of all universal functions in the [documentation](http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs). Here are some other applications of broadcasting:

# In[24]:


# Compute outer product of vectors
v = np.array([1, 2, 3])  # v has shape (3,)
w = np.array([4, 5])     # w has shape (2,)

# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:
print(np.reshape(v, (3, 1)) * w)


# In[25]:


# Add a vector to each column of a matrix
x = np.array([[1, 2, 3], [4, 5, 6]])
w = np.array([4, 5])  # w has shape (2,)

# x has shape (2, 3) and w has shape (2,). Thus, we could transpose x
# and add w to it by rows at first; then, transpose x back.
print((x.T + w).T)

# Another solution is to reshape w to be a row vector of shape (2, 1);
# we can then broadcast it directly against x
print(x + np.reshape(w, (2, 1)))


# Broadcasting typically makes your code more concise and faster, so you should strive to use it where possible.

# ## References
# + This tutorial was edited based on the [Python Numpy Tutorial](https://cs231n.github.io/python-numpy-tutorial).
# + This tutorial has touched on many of the important things that you need to know about `numpy`, but is far from complete. Check out the [numpy reference](http://docs.scipy.org/doc/numpy/reference/) to find out more.
# + If you are already familiar with MATLAB, you might find this [tutorial](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) useful to get started with `numpy`.
# + If you are already familiar with R, you might refer to this [tutorial](http://www.data-analysis-in-python.org/python_for_r.html) to get started with `numpy`.
