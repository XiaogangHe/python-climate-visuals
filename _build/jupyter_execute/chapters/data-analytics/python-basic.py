#!/usr/bin/env python
# coding: utf-8

# # Python tutorial
# 
# This tutorial will serve as a quick crash course both on the Python programming language and on the use of Python for scientific computing and visualization.

# In this tutorial, we will cover:
# 
# * Basic Python: Basic data types, Containers, Loops, Functions and Classes

# ## Jupyter Notebooks
# 
# Before we dive into Python, we'd like to briefly talk about *notebooks*.
# A Jupyter notebook lets you write and execute Python code *locally* in your web browser. Jupyter notebooks make it very easy to tinker with code and execute it in bits and pieces; for this reason they are widely used in scientific computing.
# 
# The Binder service powered by BinderHub allows us to run entirely in the *cloud*. Binder is basically Jupyter notebook on steroids: it's free, requires no setup, comes preinstalled with many packages, is easy to share with the world, and benefits from free access to hardware resources.
# 
# **Run Tutorial in Binder (recommended)**. If you wish to run this tutorial entirely in Binder, click the rocket logo and binder at the very top of pages.
# 
# **Run Tutorial in Jupyter Notebook**. If you wish to run the notebook locally with Jupyter, make sure your virtual environment is installed correctly, activate it, then run `pip install notebook` to install Jupyter notebook. Next, open the notebook and download it to a directory of your choice by right-clicking on the page and selecting `Save Page As`. Then run `jupyter notebook`. This should automatically launch a notebook server at `http://localhost:8888`. Find the `.ipynb` jupyter notebook you just downloaded and open it. Now, you will get the same page as Binder.

# ## Python versions
# 
# As of Janurary 1, 2020, Python has [officially dropped support](https://www.python.org/doc/sunset-python-2/) for `python2`. We'll be using Python 3.7 for this iteration of the course. In Jupyter notebook, we can check the Python version by clicking `Help -> About`.

# ## Basics of Python

# ### Basic data types

# #### Numbers

# Integers and floats work as you would expect from other languages. When initialzing variables, Python would assign proper data types.

# In[1]:


x = 3
y = 1.0
print(x, type(x))
print(y, type(y))


# In[2]:


Python also supports common operators.


# In[ ]:


print(x + 1)   # Addition
print(x - 1)   # Subtraction
print(x * 2)   # Multiplication
print(x ** 2)  # Exponentiation


# In[ ]:


x += 1
print(x)
x *= 2
print(x)


# #### Booleans

# Python implements all of the usual operators for Boolean logic by using `True` and `False`.

# In[ ]:


t, f = True, False
print(type(t), type(f))


# Now we let's look at the operations of Booleans: `and`, `or` and `not`.

# In[ ]:


print(t and f) # Logical AND;
print(t or f)  # Logical OR;
print(not t)   # Logical NOT;
print(t != f)  # Logical XOR;


# #### Strings

# In[ ]:


hello = 'hello'   # String literals can use single quotes
world = "world"   # or double quotes
print(hello, len(hello))


# In[ ]:


hw = hello + ' ' + world  # String concatenation
print(hw)


# In[ ]:


hw12 = '{} {} {}'.format(hello, world, 12)  # string formatting
print(hw12)


# String objects have a bunch of useful methods; for example:

# In[ ]:


s = "hello"
print(s.capitalize())  # Capitalize a string
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces
print(s.center(7))     # Center a string, padding with spaces
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another
print('  world '.strip())  # Strip leading and trailing whitespace


# You can find a list of all string methods in the [documentation](https://docs.python.org/3.7/library/stdtypes.html#string-methods).

# ### Containers

# Python includes several built-in container types: **lists**, **sets**, and **tuples**.

# #### Lists

# Lists are the most commonly used data structure. Think of it as a sequence of data that is enclosed in square brackets and data are separated by a comma. Note that elements in Python lists could have different data types.

# In[3]:


x = [3, 1, 2]     # Create a list
print(x)
s = [3, 1, 'foo'] # Lists can contain elements of different types
print(s, len(s))  # Built-in function len() return the number of elements


# There are some useful built-in methods for lists, such as `append` (to add elements at the end of lists) and `pop` (to remove a specific element from lists).

# In[4]:


xs = [3, 1, 'foo']
xs.append('bar') # Add a new element to the end of the list
print(xs)
x = xs.pop()     # Remove and return the last element of the list
print(x, xs)


# + **Indexing**
# 
# Each of element in lists can be accessed by calling its index value. In python, Indexing starts from 0. Indexing can also be done in reverse order by using negative values. That is the last element can be accessed first. Here, indexing starts from -1.

# In[5]:


print(xs[2])     # Indexing 3rd element; list indexing starts from 0
print(xs[-1])    # Negative indices count from the end of the list


# + **Slicing**
# 
# Indexing was only limited to accessing a single element, Slicing on the other hand is accessing a sequence of data inside the list. Slicing is done by defining the index values of the first element and the last element from the parent list that is required in the sliced list. It is written as parentlist `[a:b]` where a,b are the index values from the parent list. If a or b is not defined then the index value is considered to be the first value for a if a is not defined and the last value for b when b is not defined.

# In[6]:


nums = list(range(5))  # range is a built-in function that creates a list of integers
print(nums)            
print(nums[2:4])       # Get a slice from index 2 to 4 (exclusive)
print(nums[2:])        # Get a slice from index 2 to the end
print(nums[:2])        # Get a slice from the start to index 2 (exclusive)
print(nums[:])         # Get a slice of the whole list
print(nums[:-1])       # Slice indices can be negative
nums[2:4] = [8, 9]     # Assign a new sublist to a slice
print(nums)            


# #### Sets

# A set is an unordered collection of distinct elements. Sets are mainly used to eliminate repeated numbers in a sequence/list. It is also used to perform some standard set operations.

# In[7]:


animals = {'cat', 'dog'}
print(animals)
animals = {'cat', 'dog', 'cat'}  # Sets do not have deplicate elements
print(animals)  


# Some useful methods of sets include `add` (to add a new element in sets) and `remove` (to remove an element from sets).

# In[8]:


animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Check if an element is in a set
print(len(animals))       # Number of elements in a set
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Number of elements in a set


# #### Tuples

# A tuple is an (immutable) ordered list of values. A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot.

# In[9]:


d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)       # Create a tuple
print(type(t))
print(d[t])       
print(d[(1, 2)])


# In[10]:


t[0] = 1  # Tuple is immutable after its initialization


# ### Functions

# Python functions are defined using the `def` keyword. For example:

# In[ ]:


def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))


# We will often define functions to take optional keyword arguments, like this:

# In[ ]:


def hello(name, loud=False):
    if loud:
        print('HELLO, {}'.format(name.upper()))
    else:
        print('Hello, {}!'.format(name))

hello('Bob')
hello('Fred', loud=True)


# ### Classes

# The syntax for defining classes in Python is straightforward.

# In[ ]:


class Greeter:

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
          print('HELLO, {}'.format(self.name.upper()))
        else:
          print('Hello, {}!'.format(self.name))

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method
g.greet(loud=True)   # Call an instance method

