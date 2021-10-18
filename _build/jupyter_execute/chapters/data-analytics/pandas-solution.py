#!/usr/bin/env python
# coding: utf-8

# # Pandas Solution

# Create a DataFrame by reading file *../../assets/data/Changi_daily_rainfall.csv*. Perform the following two tasks with this DataFrame:

# ## Task 1
# 1. Determine whether the dataframe contains `NaN` values, and if so, populates the `NaN` values with 0.
# 2. View the first 2 rows and the tail 2 rows, and check total length of data.
# 3. Display a summary of the characteristics of the dataframe
# 4. Calculate the number of days with daily rainfall exceeding 50mm.
# 
# Hint: If you complete this task in your local computer (not recommend), please modify the file path accordingly.

# In[1]:


# 1
import pandas as pd
df = pd.read_csv('../../assets/data/Changi_daily_rainfall.csv', index_col=0, parse_dates=True)
df.isnull().sum().values[0] # no NaN value


# In[2]:


# 2
print('the first 2 rows:\n', df.head(2))
print('the tail 2 rows:\n', df.tail(2))
print('total length of data:\n', df.shape[0])


# In[3]:


# 3
df.describe()


# In[4]:


# 4
df[df['Daily Rainfall Total (mm)']>50].shape[0]


# ## Task 2
# 1. Upsample the DataFrame into 1-year bins and sum the values of the timestamps falling into a bin.
# 2. Calculate the average value of yearly rainfall in 1981-2000 and 2001-2020 and compare them.
# 3. Calculate the year with the largest annual rainfall and corresponding value, and the year with the smallest annual rainfall and corresponding value.
# 4. Make a line plot of data generated in step 1 (Optional)

# In[5]:


# 1
df_year = df.resample('y').sum()
df_year.head(5)


# In[6]:


# 2 
print('the average value of yearly rainfall in 1981-2000:\n', df_year['1981':'2000'].mean().values[0])
print('the average value of yearly rainfall in 2001-2020:\n', df_year['2001':'2020'].mean().values[0])
# the average value of yearly rainfall in 2001-2020 is greater than 1981-2000


# In[7]:


# 3
print('the largest annual rainfall and corresponding value:\n', df_year[df_year['Daily Rainfall Total (mm)']==df_year.max().values[0]])
print('the smallest annual rainfall and corresponding value:\n', df_year[df_year['Daily Rainfall Total (mm)']==df_year.min().values[0]])


# In[8]:


df_year.plot()

