#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datascience import *
path_data = '../../../assets/data/'
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

cones = Table.read_table(path_data + 'cones.csv')
nba = Table.read_table(path_data + 'nba_salaries.csv').relabeled(3, 'SALARY')
movies = Table.read_table(path_data + 'movies_by_year.csv')


# # Introduction to Tables
# 
# We can now apply Python to analyze data. We will work with data stored in Table structures.
# 
# Tables are a fundamental way of representing data sets. A table can be viewed in two ways:
# * a sequence of named columns that each describe a single attribute of all entries in a data set, or
# * a sequence of rows that each contain all information about a single individual in a data set.
# 
# We will study tables in great detail in the next several chapters. For now, we will just introduce a few methods without going into technical details. 
# 
# The table `cones` has been imported for us; later we will see how, but here we will just work with it. First, let's take a look at it.

# In[2]:


cones


# The table has six rows. Each row corresponds to one ice cream cone. The ice cream cones are the *individuals*.
# 
# Each cone has three attributes: flavor, color, and price. Each column contains the data on one of these attributes, and so all the entries of any single column are of the same kind. Each column has a label. We will refer to columns by their labels.
# 
# A table method is just like a function, but it must operate on a table. So the call looks like
# 
# `name_of_table.method(arguments)`
# 
# For example, if you want to see just the first two rows of a table, you can use the table method `show`.

# In[3]:


cones.show(2)


# You can replace 2 by any number of rows. If you ask for more than six, you will only get six, because `cones` only has six rows.

# ## Choosing Sets of Columns
# The method `select` creates a new table consisting of only the specified columns.

# In[4]:


cones.select('Flavor')


# This leaves the original table unchanged.

# In[5]:


cones


# You can select more than one column, by separating the column labels by commas.

# In[6]:


cones.select('Flavor', 'Price')


# You can also *drop* columns you don't want. The table above can be created by dropping the `Color` column.

# In[7]:


cones.drop('Color')


# You can name this new table and look at it again by just typing its name.

# In[8]:


no_colors = cones.drop('Color')

no_colors


# Like `select`, the `drop` method creates a smaller table and leaves the original table unchanged. In order to explore your data, you can create any number of smaller tables by using choosing or dropping columns. It will do no harm to your original data table.

# ## Sorting Rows

# The `sort` method creates a new table by arranging the rows of the original table in ascending order of the values in the specified column. Here the `cones` table has been sorted in ascending order of the price of the cones.

# In[9]:


cones.sort('Price')


# To sort in descending order, you can use an *optional* argument to `sort`. As the name implies, optional arguments don't have to be used, but they can be used if you want to change the default behavior of a method. 
# 
# By default, `sort` sorts in increasing order of the values in the specified column. To sort in decreasing order, use the optional argument `descending=True`.

# In[10]:


cones.sort('Price', descending=True)


# Like `select` and `drop`, the `sort` method leaves the original table unchanged.

# ## Selecting Rows that Satisfy a Condition
# The `where` method creates a new table consisting only of the rows that satisfy a given condition. In this section we will work with a very simple condition, which is that the value in a specified column must be equal to a value that we also specify. Thus the `where` method has two arguments.
# 
# The code in the cell below creates a table consisting only of the rows corresponding to chocolate cones.

# In[11]:


cones.where('Flavor', 'chocolate')


# The arguments, separated by a comma, are the label of the column and the value we are looking for in that column. The `where` method can also be used when the condition that the rows must satisfy is more complicated. In those situations the call will be a little more complicated as well.
# 
# It is important to provide the value exactly. For example, if we specify `Chocolate` instead of `chocolate`, then `where` correctly finds no rows where the flavor is `Chocolate`.

# In[12]:


cones.where('Flavor', 'Chocolate')


# Like all the other table methods in this section, `where` leaves the original table unchanged.

# ## Example: Salaries in the NBA

# "The NBA is the highest paying professional sports league in the world," [reported CNN](http://edition.cnn.com/2015/12/04/sport/gallery/highest-paid-nba-players/) in March 2016. The table `nba` contains the [salaries of all National Basketball Association players](https://www.statcrunch.com/app/index.php?dataid=1843341) in 2015-2016.
# 
# Each row represents one player. The columns are:
# 
# | **Column Label**   | Description                                         |
# |--------------------|-----------------------------------------------------|
# | `PLAYER`           | Player's name                                       |
# | `POSITION`         | Player's position on team                           |
# | `TEAM`             | Team name                                           |
# |`SALARY`    | Player's salary in 2015-2016, in millions of dollars|
#  
# The code for the positions is PG (Point Guard), SG (Shooting Guard), PF (Power Forward), SF (Small Forward), and C (Center). But what follows doesn't involve details about how basketball is played.
# 
# The first row shows that Paul Millsap, Power Forward for the Atlanta Hawks, had a salary of almost $\$18.7$ million in 2015-2016.

# In[13]:


nba


# Fans of Stephen Curry can find his row by using `where`.

# In[14]:


nba.where('PLAYER', 'Stephen Curry')


# We can also create a new table called `warriors` consisting of just the data for the Golden State Warriors.

# In[15]:


warriors = nba.where('TEAM', 'Golden State Warriors')
warriors


# By default, the first 10 lines of a table are displayed. You can use `show` to display more or fewer. To display the entire table, use `show` with no argument in the parentheses.

# In[16]:


warriors.show()


# The `nba` table is sorted in alphabetical order of the team names. To see how the players were paid in 2015-2016, it is useful to sort the data by salary. Remember that by default, the sorting is in increasing order.

# In[17]:


nba.sort('SALARY')


# These figures are somewhat difficult to compare as some of these players changed teams during the season and received salaries from more than one team; only the salary from the last team appears in the table.  
# 
# The CNN report is about the other end of the salary scale – the players who were among the highest paid in the world. To identify these players we can sort in descending order of salary and look at the top few rows.

# In[18]:


nba.sort('SALARY', descending=True)


# The late Kobe Bryant was the highest earning NBA player in 2015-2016.

# In[ ]:




