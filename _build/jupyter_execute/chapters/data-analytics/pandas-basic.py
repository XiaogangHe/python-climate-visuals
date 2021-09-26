#!/usr/bin/env python
# coding: utf-8

# # Pandas (Basic)

# `Pandas` is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool, built on top of the `Python` programming language, used for data preparation and data analysis. The tutorial mainly includes two parts, **Basic** and **Advanced**. The former is mandatory for this course and the latter is optional. The following content is the **Basic**  part.

# ## Install Pandas
# If you run code on your own computer, you need to install pandas. Open the console and enter ```pip install pandas```

# In[1]:


# Import panas and view pandas version. The 'as' keyword is to replace pandas with an abbreviation 'pd'.
import pandas as pd
print(pd.__version__)


# ## Introduction to pandas Data Structures
# The two primary data structures of pandas is
# + Series
# + DataFrame
# 
# The `series` is designed to accommodate a sequence of one-dimensional data, and the `dataframe` is designed to contain cases with several dimensions.

# ## Series
# As shown below, the internal structure of the series object is simple, which is composed of two arrays associated with each other. The main array holds the data (data of any `NumPy` type) to which each element is associated
# with a label, contained within the other array, called the ```index```.
# 
# |index|Value|
# |:---|--:|
# |0|-1|
# |1|3|
# |2|8|

# ### Defining a Series

# To create the series specified in above, you simply call the `Series()` function and pass as an argument an array containing the values to be included in it.

# In[2]:


s = pd.Series([-1,3,8]) # list
print(s)
s1 = pd.Series(s) # from Other Series
print(s1)


# As you can see from the output of the series, on the left there are the values in the index, which is a series of labels, and on the right are the corresponding values.
# 

# ```{margin}
# If you do not specify any index during the definition of the series, by default, pandas will assign numerical values increasing from 0 as labels. In this case, the labels correspond to the indexes (position in the array) of the elements in the series object.
# ```

# In general, it is best to create a series with meaningful labels to distinguish and identify each item. During the constructor call, the labels are added by specifying the value of the `index` option or using `dict` object.

# In[3]:


# when declaring a Series, you can specify the index
s2 = pd.Series({"a":-1,"b":3,"c":8}) # dictionary
print(s2)
s3 = pd.Series([-1,3,8], index=['x','y','z']) # specify the index by 'index' option
print(s3)


# In[4]:


import numpy as np
arr = np.array([100,20,-3]) # from NumPy Arrays
s4 = pd.Series(arr, index=['x','y','z'] )
print(s4)


# ```{margin}
# Always keep in mind that the values contained in the `NumPy` array or in the
# original series are not copied, but are passed by reference. That is, the object is inserted
# dynamically within the new series object. If it changes, for example its internal element
# varies in value, then those changes will also be present in the new series object.
# ```

# In[5]:


arr[2] = -40
arr
s4


# As you can see in this example, by changing the third element of the `arr` array, we
# also modified the corresponding element in the `s4` series.

# If you want to individually see the two arrays that make up this data structure, you
# can call the two attributes of the series as follows: index and values.

# In[6]:


print(s.values)
print(s.index)


# ### Selecting the Internal Elements

# You can select individual elements as ordinary numpy arrays, specifying the key.

# In[7]:


s2 = pd.Series({"a":-1,"b":3,"c":8})
s2[1]


# Or you can specify the label corresponding to the position of the index.

# In[8]:


s2['a']


# In the same way you select multiple items in a numpy array, you can specify the
# following:

# In[9]:


s2[0:2]


# In[10]:


s2['a':'c']


# In[11]:


s2[['a','c']]


# ### Assigning Values to the Elements

# In[12]:


s1['a'] = 100
s1


# ### Filtering Values

# If you need to know which elements in the series are greater than 4, you
# write the following

# In[13]:


s = pd.Series([1,3,5,2,10])
s[s>4] # greater than 4


# In[14]:


# According to Boolean value to filter
s = pd.Series([1,3,5,2,10])
print(s.isin([2,5]))
print(s[s.isin([2,5])])


# ### Operations and Mathematical Functions

# In[15]:


s*2.5


# In[16]:


np.exp(s)


# ### Nan Value

# The `NaN` refers to `Not a Number`, which generally is caused by the missing value. Before data analysis, the `NaN` value need to be adressed.

# In[17]:


import numpy as np 
# Declaring a Series with NaN value
s = pd.Series([1,np.NaN,10,9,-2,np.NaN])
s


# Call `isnull()` or `notnull()` functions to generate boolean value and further identify the indexes with NaN value. 

# In[18]:


print(s.isnull())
print(s.notnull())


# Based on the generated boolean value, the series with full NaN value and without NaN can be generated.

# In[19]:


print(s[s.isnull()])
print(s[s.notnull()])


# ### Operation of multiple Series

# In[20]:


s = pd.Series({"Singapore":30,"Malaysia":23,"Vietnam":36,"Cambodia":41})
s1 = pd.Series({"China":51,"Japan":73,"Vietnam":36,"Laos":31})
s*s1


# As you can see, only indexes which all series have can opearte. 

# ## DataFrame

# Compared with the `Series`, the `DataFrame` can contain multiple dimentional data. Its fist column and first row are `index` and `columns`, respectively. (Only for DataFrame without multiple index, `DataFrame` with multiple indexes which will be introduced later). Each column must be same data type (numeric, string, boolean et al.) but different columns can have different data types. 
# 
# |index|numeric|string|boolean|
# |:--|:--:|:--:|--:|
# |0|-1|Singapore|True|
# |1|3|China|True|
# |2|8|Japan|False|
# 

# ### Defining a DataFrame

# Call `DataFrame()` function to create a `DataFrame`. The `Array`, `List`, `dict` all can taken as the input of `DataFrame()` function.

# In[21]:


# array
df = pd.DataFrame(np.array([[14, 35, 35, 35],
                            [19, 34, 57, 34],
                            [42, 74, 49, 59]]))
print(df)
# list,  use 'columns' and 'index' parameters to specify the column and index of generated dataframe.
df = pd.DataFrame([["Malaysia","Kuala Lumpur",32365999,False],
              ["Singapore","Singapore",5850342,True],
              ["Vietnam","Hanoi",97338579,True]],
              columns = ["Country", "Capital", "Population", "Isdeveloped"],
              index=["a","b","c"])
print(df)
# dict
df = pd.DataFrame({"Country":["Malaysia","Singapore","Vietnam"],
                   "Capital":["Kuala Lumpur","Singapore","Hanoi"],
              "Population":[32365999,5850342,97338579],
              "Isdeveloped":[False,True,True]})
df


# ### Selecting the Internal Elements

# Similar with `Series`, two ways can be used to select the elements from `DataFrame`. Call `iloc[]` and `loc[]` to select the elements by position and label, respectively .

# In[22]:


df = pd.DataFrame([["Malaysia","Kuala Lumpur",32365999,False],
              ["Singapore","Singapore",5850342,True],
              ["Vietnam","Hanoi",97338579,True]],
              columns = ["Country", "Capital", "Population", "Isdeveloped"],
              index=["a","b","c"])
df


# In[23]:


# use ':' to represent select all
df.iloc[:,0:2]


# In[24]:


df.loc[:,"Country":"Population"]


# In[25]:


df.loc["a",["Country","Population"]]


# In[26]:


df.iloc[[0,1]] # If you omit number of columns, all columns will be selected 


# Use ```columns```,```index``` and ```values``` atrributes to obtain corresponding object value.

# In[27]:


df.index


# In[28]:


df.columns


# In[29]:


df.values


# Select corresponding column according the label or number of columns.

# In[30]:


df["Country"]


# In[31]:


df[["Country","Population"]] # Use list to select multiple columns  


# In[32]:


df.Country # Also support as atrribute to select


# In[33]:


df["a":"b"] # When select multiple rows, do not use list   


# In[34]:


df[0:2] # When select multiple rows, do not use list


# ### Assigning value

# In[35]:


df.loc["c","Country"] = "Japan"
df.loc["c","Capital"] = "Tokyo"
df.loc["c","Population"] = 126476461
df.loc["c","Isdeveloped"] = True
df


# In[36]:


df.loc["c"] = ["Japan", "Tokyo", 126476461, True]
df


# ### Assigning index, columns, and name of index and columns

# In[37]:


df.index = ["e", "f", "g"]
df.index.name = "label"
df.columns.name = "atributes"
df.columns = ["Coun", "Cap", "Pop", "ID"]
df


# ### Delete columns from dataframe

# In[38]:


del df["ID"]
df


# ### Filtering
# Same as ```Series()``` mentioned above.

# In[39]:


df = pd.DataFrame(np.array([[14, 35, 35, 35],
                            [19, 34, 57, 34],
                            [42, 74, 49, 59]]))
# filtering lesser than 30
df[df<30]


# In[40]:


df = pd.DataFrame([["Malaysia","Kuala Lumpur",32365999,False],
              ["Singapore","Singapore",5850342,True],
              ["Vietnam","Hanoi",97338579,True]],
              columns = ["Country", "Capital", "Population", "Isdeveloped"],
              index=["a","b","c"])
# Filtering accroding to conditions of one column
df[df["Population"]<50000000]


# In[41]:


# Filtering accroding to conditions of multiple columns
df[(df["Population"]<50000000) & (df["Isdeveloped"]==True)]


# ### Transposition  of a Dataframe
# Same as `Array` from `Numpy` dataframe can transpose. `Columns` change to `Index` and `Index` change to `Columns`.

# In[42]:


df = pd.DataFrame([["Malaysia","Kuala Lumpur",32365999,False],
              ["Singapore","Singapore",5850342,True],
              ["Vietnam","Hanoi",97338579,True]],
              columns = ["Country", "Capital", "Population", "Isdeveloped"],
              index=["a","b","c"])
df1 = df.T
df1


# In[43]:


df1.index


# In[44]:


df1.columns


# ### Merge of dataframe
# `Concat()`, `Join()`

# In[45]:


df1 = pd.DataFrame(np.random.rand(3,4))
df2 = pd.DataFrame(np.random.rand(3,4))
df3 = pd.DataFrame(np.random.rand(6,4))
df4 = pd.DataFrame(np.random.rand(3,6))


# In[46]:


df1


# In[47]:


df2


# In[48]:


df3


# In[49]:


df4


# In[50]:


pd.concat([df1,df2])


# In[51]:


result = df1.append(df2)
result


# ### `join`, `inner` and `merge`

# ### View data

# In[52]:


df = pd.DataFrame(np.random.rand(100,4))
df.head()


# In[53]:


df.tail()


# ### Computational tools

# ### Covariance

# In[54]:


df = pd.DataFrame(np.random.rand(5,5))
df.cov()


# ### Correlation

# In[55]:


df.corr() # pearson (default), kendall, spearman


# ### `mean()`, `sum()`, `describe()`

# In[56]:


df.mean()


# In[57]:


df.sum()


# In[58]:


df.describe()


# ### Data ranking

# In[59]:


df = pd.DataFrame([["Malaysia","Kuala Lumpur",32365999,False],
              ["Singapore","Singapore",5850342,True],
              ["Vietnam","Hanoi",97338579,True],
                  ["Japan","Tokyo",None,True]],
              columns = ["Country", "Capital", "Population", "Isdeveloped"],
              index=["a","b","c",'d'])
df.sort_values(by=['Population','Country'], ascending=False, na_position='first')


# ## Missing data (NaN value)

# In[60]:


df = pd.DataFrame(np.random.rand(5,5))
df.iloc[0,1] = np.nan
df.iloc[2,2] = np.nan
df.iloc[3,1] = np.nan
df.iloc[3,3] = np.nan
df


# In[61]:


# detecting nan value
df.isnull()


# In[62]:


# detecting nan value
df.notnull()


# In[63]:


df.isna()


# In[64]:


# fill nan using a specify value
df.fillna(value=0)


# In[65]:


# fill nan using a method
# set inplace to True, the changes will act on dataframe
df.fillna(method="ffill") # other method: ‘backfill’, ‘bfill’, ‘pad’
df


# In[66]:


df.fillna(method="pad")


# In[67]:


# delete NaN value
# ‘any’ : If any NA values are present, drop that row or column.
# ‘all’ : If all values are NA, drop that row or column.

# 0, or ‘index’ : Drop rows which contain missing values.
# 1, or ‘columns’ : Drop columns which contain missing value.
df.dropna(axis="index",how="any")


# ## Date index

# In[68]:


dti = pd.date_range("2018-01-01", periods=3, freq="H")
print(dti)
dti = pd.date_range(start = "2021-09-28",end="2021-09-30", freq="10H")
print(dti)


# Manipulating and converting date times with timezone information

# In[69]:


dti = pd.date_range(start = "2021-09-28",end="2021-09-30", freq="10H")
dti = dti.tz_localize("UTC")
dti


# In[70]:


dti = pd.date_range(start = "2021-09-28",end="2021-09-30", freq="10H")
dti = dti.tz_localize("Asia/Singapore")
dti


# Using the `origin` option, one can specify an alternative starting point for creation of a `DatetimeIndex`. For example, to use 1900-01-01 00:00:00 as the starting time and hour as the unit period length:

# In[71]:


pd.to_datetime([100, 101, 102], unit="h", origin=pd.Timestamp("1900-01-01 00:00:00"))


# Supported units are: `D`:day, `h`:hour, `m`: minute, and `s`:second.

# ```{tip}
# The time labels of climate products is usually given a start time point and discrete time interval, and then represented by a column of integers. In this case, we can use above way to construct time labels.
# ```

# ## Upsampling and Downsampling

# * Upsampling: Increase the frequency of the samples by interpolation, such as from minutes to seconds. 
# * Downsampling: Ddecrease the frequency of the samples by aggregation, such as from months to years.
# 

# In[72]:


# prepare data, this section will be introduced in the next tutorial
# Data Source: http://www.weather.gov.sg/climate-historical-daily/
data = pd.read_csv('../../../assets/data/Changi_daily_rainfall.csv', index_col=0,header=0,parse_dates=True)
data.head()


# In[73]:


# Downsampling: Convert monthly data to yearly data by sum and max
df = data
dfsum = df.resample("Y").sum()
dfsum.head()


# In[74]:


dfmax = df.resample("Y").max()
dfmax.head()


# In[75]:


# Upsampling: Convert monthly data to yearly data by sum and max
dfmax.resample('10D').asfreq()[0:5]


# In[76]:


dfmax.resample('10D').pad()[0:5]


# In[77]:


dfmax.resample('D').ffill(limit=2)[0:5]


# In[ ]:




