#!/usr/bin/env python
# coding: utf-8

# # Python Exercise

# ## Task 1 (Containers)
# For a list which contains three sublists `precipitation = [[0, 0, 3.0], [1.1, 4.8, 0], [0, 0, 0]]`, write a program to find the maximum for each sublist and print it as a dictionary whose key is `sublist_n` (where `n` is the index of sublist) and value is the corresponding maximum. 
# 
# Hint: use `max()` to obtain the maximum of a list. You could also try to use dictionary comprehension to accomplish this within one line of code.

# In[16]:


# Your solution goes here.
precipitation = [[0, 0, 3.0], [1.1, 4.8, 0], [0, 0, 0]]


# ## Task 2 (Control flows)
# Write a program to print all prime numbers within the range `range(25, 50)`.
# 
# Hint: A prime number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. You may wish to use the following statements:
# + use `for num in range(25, 50)` to iterate over all numbers;
# + for a specific number, use `for i in range(2, num)` to iterate over potential factors except 1;
# + use `(num % i) == 0` to determine whether `i` is truly a factor of `num` (if it is true, `num` is not a prime number); and
# + use `break` to stop one iter loop.

# In[2]:


# Your solution goes here.


# ## Task 3 (Functions)
# Following Task 2, define a function that returns the list of prime numbers for a specified range. Then, use this function to print the prime numbers within the ranges `range(25, 50)` and `range(50, 100)` respectively.
# 
# Hint: in the function, you may define an empty list `prime_num = []` at first and use the `append` method to add prime numbers. The list 

# In[8]:


# Your solution goes here.

