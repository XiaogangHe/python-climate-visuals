#!/usr/bin/env python
# coding: utf-8

# # Python tutorial

# Python is a high-level, dynamically typed multiparadigm programming language. Python code is often said to be almost like pseudocode, since it allows you to express very powerful ideas in very few lines of code while being very readable. As an example, here is an implementation of the classic quicksort algorithm in Python:

# In[1]:


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))


# If you are already familar with Python, you may choose to skip this tutorial; however, if not, this tutorial will serve as a quick crash course on the Python programming language as the basis for subsequent tutorials on scientific computing and visualization.
# 
# In this tutorial, we will cover:
# 
# * Basic Python: Basic data types, Containers, Control Flow (Conditions and Loops), Functions and Classes

# ## Jupyter Notebooks
# 
# Before we dive into Python, we'd like to briefly talk about *notebooks*.
# A Jupyter notebook lets you write and execute Python code *locally* in your web browser. Jupyter notebooks make it very easy to tinker with code and execute it in bits and pieces; for this reason they are widely used in scientific computing.
# 
# The Binder service powered by BinderHub allows us to run entirely in the *cloud*. Binder is basically Jupyter notebook on steroids: it's free, requires no setup, comes preinstalled with many packages, is easy to share with the world, and benefits from free access to hardware resources.
# 
# + **Run Tutorial in Binder (recommended)**.
# If you wish to run this tutorial entirely in Binder, click the rocket logo and binder at the very top of pages.
# 
# + **Run Tutorial in Jupyter Notebook**.
# If you wish to run the notebook locally with Jupyter, make sure your virtual environment is installed correctly, activate it, then run `pip install notebook` to install Jupyter notebook. Next, open the notebook and download it to a directory of your choice by right-clicking on the page and selecting `Save Page As`. Then run `jupyter notebook`. This should automatically launch a notebook server at `http://localhost:8888`. Find the `.ipynb` jupyter notebook you just downloaded and open it. Now, you will get the same page as Binder.

# As of Janurary 1, 2020, Python has [officially dropped support](https://www.python.org/doc/sunset-python-2/) for `python2`. We'll be using Python 3.7 for this iteration of the course. In Jupyter notebook, we can check the Python version by clicking `Help -> About`.

# ## Basic data types

# ### Numbers

# Integers and floats work as you would expect from other languages. When initialzing variables, Python would assign proper data types. Python has a built-in function `type()` to look at the type

# In[2]:


x = 3
y = 1.0
print(x, type(x))  #print() is a Python built-in function for printing 
print(y, type(y))


# Python also supports common operators.

# In[3]:


print(x + 1)   # Addition
print(x - 1)   # Subtraction
print(x * 2)   # Multiplication
print(x ** 2)  # Exponentiation
print(x // 2)  # Floor division


# In[4]:


x += 1
print(x)
x *= 2
print(x)


# ### Booleans

# In Python, the two Boolean constants are written as `True` and `False`.

# In[5]:


t, f = True, False
print(type(t), type(f))


# Now let's look at the operations of Booleans: `and`, `or` and `not`.

# In[6]:


print(t and f) # Logical AND;
print(t or f)  # Logical OR;
print(not t)   # Logical NOT;
print(t != f)  # Logical XOR;


# ### Strings

# In[7]:


hello = 'hello'   # String literals can use single quotes
world = "world"   # or double quotes
print(hello, len(hello))


# In[8]:


hw = hello + ' ' + world  # String concatenation
print(hw)


# In[9]:


hw12 = '{} {} {}'.format(hello, world, 12)  # string formatting
print(hw12)


# String objects have a bunch of useful methods; for example:

# In[10]:


s = "hello"
print(s.capitalize())  # Capitalize a string
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another
print('  world '.strip())  # Strip leading and trailing whitespace


# You can find more information about Python basic data types in the official [documantion](https://docs.python.org/3.7/library/stdtypes.html), such as a list of [all string methods](https://docs.python.org/3.7/library/stdtypes.html#string-methods).

# ## Containers

# Python includes several built-in container types. **lists**, **dictionaries**, **sets**, and **tuples**.

# ### Lists

# Lists are the most commonly used data structure. Think of it as a sequence of data that is enclosed in square brackets `[]` and data are separated by a comma `,`. Note that elements in Python lists could have different data types.

# In[11]:


x = [3, 1, 2]     # Create a list
print(x)
s = [3, 1, 'foo'] # Lists can contain elements of different types
print(s, len(s))  # Built-in function len() return the number of elements


# There are some useful built-in methods of lists, such as `append` (to add elements at the end of lists) and `pop` (to remove a specific element from lists).

# In[12]:


xs = [3, 1, 'foo']
xs.append('bar') # Add a new element to the end of the list
print(xs)
x = xs.pop()     # Remove and return the last element of the list
print(x, xs)


# + **Indexing**
# 
# Each of element in lists can be accessed by calling its index value. Note that in python, **indexing starts from 0**. Indexing can also be **in reverse order using negative values** (that is the last element can be accessed first with indexing -1).

# In[13]:


print(xs[2])     # Indexing 3rd element; list indexing starts from 0
print(xs[-1])    # Negative indices count from the end of the list


# + **Slicing**
# 
# Indexing was only limited to accessing a single element, but slicing on the other hand accesses a sequence of data inside the list. Slicing is done by defining the index values of the first element (a) and the last element (b) in the form as parentlist `[a:b]`. **Note that b is not included in the resulting slicing**. If a (or b) is not defined then the slicing will start from the first (or end to the last).

# In[14]:


nums = list(range(6))  # range() is a built-in function that creates a list of integers
print(nums)
print(nums[2:4])       # Get a slice from index 2 to 4 (exclusive)
print(nums[2:])        # Get a slice from index 2 to the end
print(nums[:])         # Get a slice of the whole list
print(nums[:-1])       # Slice indices can be negative
nums[2:4] = [8, 9]     # Assign a new sublist to a slice
print(nums)


# You can also slice a parent list with a fixed step length (c): `[a:b:c]`.

# In[15]:


print(nums[:-1:2])  # Get a slice from index 0 to -1 (exclusive) in a step length of 2
print(nums[::-1])   # Get a slice of whole list in reverse order


# We will meet slicing again in `numpy` [tutorial]().

# ### Dictionaries

# A dictionary stores pairs of key and value in the form of braces `{key: value}`. Dictionaries are more used like a database because here you can index a particular sequence with your user defined string.

# In[16]:


d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print(d['cat'])       # Get an value from a dictionary
print('cat' in d)     # Check if a dictionary has a given key


# In[17]:


d['fish'] = 'wet'   # Set a new entry in a dictionary
print('fish' in d)


# One useful built-in method of dictionaries is `get` where you can get the value with a default for the cases when the key does not exists.

# In[18]:


print(d.get('monkey', 'N/A'))  # Get a value with a default
print(d.get('fish', 'N/A'))    # Get a value with a default


# In[19]:


del d['fish']               # Remove an element from a dictionary
print(d.get('fish', 'N/A')) # "fish" is no longer a key


# ### Tuples

# A tuple is an (immutable) ordered list of values in the form of parentheses `()`. A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot.

# In[20]:


t1 = (5, 6)       # Create a tuple
t2 = (7, 8)
d = {t1:'Group A', t2:'Group B'}
print(d)
print(type(t1))
print(d[t1], d[(7, 8)])       


# In[21]:


# t[0] = 1  # Tuple is immutable after its initialization; 


# ## Control Flow

# ### Conditions: if-elif-else
# Control flow of conditions is used to execuate different algorithms under different conditions. Next is an example. **Note that there should be incidents of four blanks for each section of algorithms.**

# In[22]:


x = 10
y = 12
if x > y:
    print("x>y")  # Four blanks before the algorithm
elif x < y:
    print("x<y")  # Four blanks before the algorithm
else:
    print("x=y")  # Four blanks before the algorithm


# ### Loops:
# Control flow of loops is used to iterate algorithms for each element in containers or under a specific condition.

# + **`for` Loops**
# 
# Here is an example that iterates over elements in lists.

# In[23]:


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list1 in list_of_lists:  # Iterate over elements in list_of_lists
        print(list1)         # Four blanks before the algorithm


# For dictionaries, we could also iterate over pairs of key and value.

# In[24]:


d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A {} has {} legs'.format(animal, legs))


# + **`while` Loops**
# 
# Here is an example that iterates under a specific condition.

# In[25]:


i = 1
while i < 3:    # Iterate when i smaller than 3
    print(i**2) # Four blanks before each line of algorithm
    i += 1      # Four blanks before
print('Bye')    # This is not a part of iterations


# ### List Comprehensions
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. We can employ control flows of other lists in the initialization of a new list.

# In[26]:


nums = [0, 1, 3, 4, 6]
squares = [x ** 2 for x in nums]
print(squares)

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)


# Similarly, for dictionaries, we could use dictionary comprehension to create a new dictionary based on an existing list.

# In[27]:


nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)


# ## Functions

# Python functions are defined using the `def` keyword. For example:

# In[28]:


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

# In[29]:


def hello(name, loud=False):
    if loud:
        print('HELLO, {}'.format(name.upper()))
    else:
        print('Hello, {}!'.format(name))

hello('Bob')
hello('Fred', loud=True)


# ## Classes

# The syntax for defining classes in Python is straightforward. `__init__` is defined as the initialization method of classes.

# In[30]:


class Greeter:

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable (attribute)

    # Instance method
    def greet(self, loud=False):
        if loud:
          print('HELLO, {}'.format(self.name.upper()))
        else:
          print('Hello, {}!'.format(self.name))

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method
g.greet(loud=True)   # Call an instance method


# ## References
# + This tutorial was edited based on the [Python Numpy Tutorial](https://cs231n.github.io/python-numpy-tutorial) and [Rajath Kumar's Python Lectures](https://github.com/rajathkmp/Python-Lectures).
# + This tutorial only touched basic things about Python that you need to know. You may refer to official documentation of [Python Standard Library](https://docs.python.org/3.7/library/index.html) for detailed information when necessary.