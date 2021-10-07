#!/usr/bin/env python
# coding: utf-8

# # Python Answer

# :::{note} <u>*The answer to each task is not exclusive*</u>. Depending on the purpose of our programming, we may wish our scripts to be intuitive or concise or fast or flexible. There should be a lot of ways to accomplish the following programming tasks, yet we may alter how we script to be in alignment with our purposes.:::

# ## Task 1 (Containers)
# For a list which contains three sublists `precipitation = [[0, 0, 3.0], [1.1, 4.8, 0], [0, 0, 0]]`, write a program to find the maximum for each sublist and print it as a dictionary whose key is `sublist_n` (where `n` is the index of sublist) and value is the corresponding maximum. 
# 
# Hint: use `max()` to obtain the maximum of a list. You could also try to use dictionary comprehension to accomplish this task within one line of code.

# In[1]:


# Your solution goes here.
precipitation = [[0, 0, 3.0], [1.1, 4.8, 0], [0, 0, 0]]
print({"sublist_{}".format(x): max(precipitation[x]) for x in range(0, len(precipitation))})


# :::{note} `len()` is a Python built-in function that returns the number of elements in a list. We may use `help(len)` to see the description and usage of this function.:::

# ## Task 2 (Control flows)
# Write a program to print all prime numbers within the range `range(25, 50)`.
# 
# Hint: a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. You may wish to use the following statements:
# + use `for num in range(25, 50)` to iterate over all numbers;
# + for a specific number, use `for i in range(2, num)` to iterate over potential factors except 1;
# + use `(num % i) == 0` to determine whether `i` is truly a factor of `num` (if it is true, `num` is not a prime number); and
# + use `break` to stop one loop.

# In[2]:


# Your solution goes here.
for num in range(25, 50):
    if num > 1:  # all prime numbers are greater than 1
        for i in range(2, num):  # check for factors
            if (num % i) == 0:  # not a prime number, so break inner loop
                break
        else:
            print(num)


# :::{note} It is not common to use `for-else` loops. `else` here means that the following algorithms will be run when the `for` loop ends. Normally, if we want to run specific algorithms after loops, we just need to script them after loops. However, if `break` exists in the loop, the algorithms in `else` will not execute when `break` happens, because the loop do not reach its end. Thus, `for-else` loops is useful only when there exists `break` statements within loops.
# 
# In addition, please mind the indents before each line. Python relies on indents to identify code blocks, so a wrong slip in indents may cause errors or even unanticipated results. You may try adding an indent before `else:` and `print(num)` to see what will happen.:::

# ## Task 3 (Functions)
# Following Task 2, define a function that returns the list of prime numbers for a specified range. Then, use this function to print the prime numbers within the ranges `range(25, 50)` and `range(50, 100)` respectively.
# 
# Hint: in the function, you may define an empty list `prime_num = []` at first and use the `append` method to add prime numbers.

# In[3]:


# Your solution goes here.
def findprime(rangelist):
    prime_num = []
    for num in rangelist:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_num.append(num)
    return prime_num


print(findprime(range(25, 50)))
print(findprime(range(50, 100)))


# ## Bonus Task
# Still remember the example `quicksort()` programming at the beginning of Python Tutorial? Try to comprehend how this function sorts a list. This function was run in a recursive manner (i.e. the function was used within its own codes). This brings effects quite alike as loops; you could try adding a printing function `print(left, middle, right)` to see what happened in each step.
