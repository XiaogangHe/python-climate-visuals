#!/usr/bin/env python
# coding: utf-8

# # Pandas (basic)

# `Pandas` is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool, built on top of the Python programming language, used for data preparation and data analysis.

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
import numpy as np
arr = np.array([100,20,-3]) # from NumPy Arrays
s1 = pd.Series(arr)
print(s1)
s2 = pd.Series(s) # from Other Series
s2

# when declaring a Series, you can specify the index
s2 = pd.Series({"a":-1,"b":3,"c":8}) # dictionary
print(s2)
s3 = pd.Series([-1,3,8], index=['x','y','z']) # specify the index by 'index' option
print(s3)


# As you can see from the output of the series, on the left there are the values in the index, which is a series of labels, and on the right are the corresponding values.
# 
# If you do not specify any index during the definition of the series, by default,
# pandas will assign numerical values increasing from 0 as labels. In this case, the labels correspond to the indexes (position in the array) of the elements in the series object.
# 
# Often, however, it is preferable to create a series using meaningful labels in order to distinguish and identify each item regardless of the order in which they were inserted into the series.
# 
# In this case it will be necessary, during the constructor call, to include the `index` option and assign an array of strings containing the labels.

# ```{margin}
# Always keep in mind that the values contained in the NumPy array or in the
# original series are not copied, but are passed by reference. That is, the object is inserted
# dynamically within the new series object. If it changes, for example its internal element
# varies in value, then those changes will also be present in the new series object.
# ```

# In[3]:


arr[2] = -40
arr
s1


# As you can see in this example, by changing the third element of the `arr` array, we
# also modified the corresponding element in the `s1` series.

# If you want to individually see the two arrays that make up this data structure, you
# can call the two attributes of the series as follows: index and values.

# In[4]:


print(s.values)
print(s.index)


# ### Selecting the Internal Elements

# You can select individual elements as ordinary numpy arrays, specifying the key.

# In[5]:


s2 = pd.Series({"a":-1,"b":3,"c":8})
s2[1]


# Or you can specify the label corresponding to the position of the index.

# In[6]:


s2['a']


# In the same way you select multiple items in a numpy array, you can specify the
# following:

# In[7]:


s2[0:2]


# In[8]:


s2['a':'c']


# In[9]:


s2[['a','c']]


# ### Assigning Values to the Elements

# In[10]:


s1['a'] = 100
s1


# ### Filtering Values

# If you need to know which elements in the series are greater than 4, you
# write the following

# In[11]:


s = pd.Series([1,3,5,2,10])
s[s>4] # greater than 4


# In[12]:


# According to Boolean value to filter
s = pd.Series([1,3,5,2,10])
print(s.isin([2,5]))
print(s[s.isin([2,5])])


# ### Operations and Mathematical Functions

# In[13]:


s*2.5


# In[14]:


np.exp(s)


# ### Nan Value

# The `NaN` refers to `Not a Number`, which generally is caused by the missing value. Before data analysis, the `NaN` value need to be adressed.

# In[15]:


import numpy as np 
# Declaring a Series with NaN value
s = pd.Series([1,np.NaN,10,9,-2,np.NaN])
s


# Call `isnull()` or `notnull()` functions to generate boolean value and further identify the indexes with NaN value. 

# In[16]:


print(s.isnull())
print(s.notnull())


# Based on the generated boolean value, the series with full NaN value and without NaN can be generated.

# In[17]:


print(s[s.isnull()])
print(s[s.notnull()])


# ### Operation of multiple Series

# In[18]:


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

# In[19]:


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

# In[20]:


df = pd.DataFrame([["Malaysia","Kuala Lumpur",32365999,False],
              ["Singapore","Singapore",5850342,True],
              ["Vietnam","Hanoi",97338579,True]],
              columns = ["Country", "Capital", "Population", "Isdeveloped"],
              index=["a","b","c"])
df


# In[21]:


# use ':' to represent select all
df.iloc[:,0:2]


# In[22]:


df.loc[:,"Country":"Population"]


# In[23]:


df.loc["a",["Country","Population"]]


# In[24]:


df.iloc[[0,1]] # If you omit number of columns, all columns will be selected 


# Use ```columns```,```index``` and ```values``` atrributes to obtain corresponding object value.

# In[25]:


df.index


# In[26]:


df.columns


# In[27]:


df.values


# Select corresponding column according the label or number of columns.

# In[28]:


df["Country"]


# In[29]:


df[["Country","Population"]] # Use list to select multiple columns  


# In[30]:


df.Country # Also support as atrribute to select


# In[31]:


df["a":"b"] # When select multiple rows, do not use list   


# In[32]:


df[0:2] # When select multiple rows, do not use list


# ### Assigning value

# In[33]:


df.loc["c","Country"] = "Japan"
df.loc["c","Capital"] = "Tokyo"
df.loc["c","Population"] = 126476461
df.loc["c","Isdeveloped"] = True
df


# In[34]:


df.loc["c"] = ["Japan", "Tokyo", 126476461, True]
df


# ### Assigning index, columns, and name of index and columns

# In[35]:


df.index = ["e", "f", "g"]
df.index.name = "label"
df.columns.name = "atributes"
df.columns = ["Coun", "Cap", "Pop", "ID"]
df


# ### Delete columns from dataframe

# In[36]:


del df["ID"]
df


# ### Filtering
# Same as ```Series()``` mentioned above.

# In[37]:


df = pd.DataFrame(np.array([[14, 35, 35, 35],
                            [19, 34, 57, 34],
                            [42, 74, 49, 59]]))
# filtering lesser than 30
df[df<30]


# In[38]:


df = pd.DataFrame([["Malaysia","Kuala Lumpur",32365999,False],
              ["Singapore","Singapore",5850342,True],
              ["Vietnam","Hanoi",97338579,True]],
              columns = ["Country", "Capital", "Population", "Isdeveloped"],
              index=["a","b","c"])
# Filtering accroding to conditions of one column
df[df["Population"]<50000000]


# In[39]:


# Filtering accroding to conditions of multiple columns
df[(df["Population"]<50000000) & (df["Isdeveloped"]==True)]


# ### Transposition  of a Dataframe
# Same as `Array` from `Numpy` dataframe can transpose. `Columns` change to `Index` and `Index` change to `Columns`.

# In[40]:


df = pd.DataFrame([["Malaysia","Kuala Lumpur",32365999,False],
              ["Singapore","Singapore",5850342,True],
              ["Vietnam","Hanoi",97338579,True]],
              columns = ["Country", "Capital", "Population", "Isdeveloped"],
              index=["a","b","c"])
df1 = df.T
df1


# In[41]:


df1.index


# In[42]:


df1.columns


# ### Merge of dataframe
# `Concat()`, `Join()`

# In[43]:


df1 = pd.DataFrame(np.random.rand(3,4))
df2 = pd.DataFrame(np.random.rand(3,4))
df3 = pd.DataFrame(np.random.rand(6,4))
df4 = pd.DataFrame(np.random.rand(3,6))


# In[44]:


df1


# In[45]:


df2


# In[46]:


df3


# In[47]:


df4


# In[48]:


pd.concat([df1,df2])


# In[49]:


result = df1.append(df2)
result


# ### `join`, `inner` and `merge`

# ### View data

# In[50]:


df = pd.DataFrame(np.random.rand(100,4))
df.head()


# In[51]:


df.tail()


# ### Computational tools

# ### Covariance

# In[52]:


df = pd.DataFrame(np.random.rand(5,5))
df.cov()


# ### Correlation

# In[53]:


df.corr() # pearson (default), kendall, spearman


# ### `mean()`, `sum()`, `describe()`

# In[54]:


df.mean()


# In[55]:


df.sum()


# In[56]:


df.describe()


# ### Data ranking

# ## Missing data (NaN value)

# In[57]:


df = pd.DataFrame(np.random.rand(5,5))
df.iloc[0,1] = np.nan
df.iloc[2,2] = np.nan
df.iloc[3,1] = np.nan
df.iloc[3,3] = np.nan
df


# In[58]:


# detecting nan value
df.isnull()


# In[59]:


# detecting nan value
df.notnull()


# In[60]:


df.isna()


# In[61]:


# fill nan using a specify value
df.fillna(value=0)


# In[62]:


# fill nan using a method
# set inplace to True, the changes will act on dataframe
df.fillna(method="ffill") # other method: ‘backfill’, ‘bfill’, ‘pad’
df


# In[63]:


df.fillna(method="pad")


# In[64]:


# delete NaN value
# ‘any’ : If any NA values are present, drop that row or column.
# ‘all’ : If all values are NA, drop that row or column.

# 0, or ‘index’ : Drop rows which contain missing values.
# 1, or ‘columns’ : Drop columns which contain missing value.
df.dropna(axis="index",how="any")


# ## Date index

# In[65]:


# pd.read_csv("")


# ## Upsampling and Downsampling

# * Upsampling: Increase the frequency of the samples by interpolation, such as from minutes to seconds. 
# * Downsampling: Ddecrease the frequency of the samples by aggregation, such as from months to years.
# 

# In[66]:


# prepare data, this section will be introduced in the next tutorial
# Source: https://data.gov.sg/dataset/rainfall-monthly-total
data = [{"_id": 1, "total_rainfall": "107.1", "month": "1982-01"}, {"_id": 2, "total_rainfall": "27.8", "month": "1982-02"}, {"_id": 3, "total_rainfall": "160.8", "month": "1982-03"}, {"_id": 4, "total_rainfall": "157", "month": "1982-04"}, {"_id": 5, "total_rainfall": "102.2", "month": "1982-05"}, {"_id": 6, "total_rainfall": "59.5", "month": "1982-06"}, {"_id": 7, "total_rainfall": "76.3", "month": "1982-07"}, {"_id": 8, "total_rainfall": "169.5", "month": "1982-08"}, {"_id": 9, "total_rainfall": "54.1", "month": "1982-09"}, {"_id": 10, "total_rainfall": "39.3", "month": "1982-10"}, {"_id": 11, "total_rainfall": "134", "month": "1982-11"}, {"_id": 12, "total_rainfall": "494.1", "month": "1982-12"}, {"_id": 13, "total_rainfall": "246", "month": "1983-01"}, {"_id": 14, "total_rainfall": "5.6", "month": "1983-02"}, {"_id": 15, "total_rainfall": "18.6", "month": "1983-03"}, {"_id": 16, "total_rainfall": "33.6", "month": "1983-04"}, {"_id": 17, "total_rainfall": "160.8", "month": "1983-05"}, {"_id": 18, "total_rainfall": "94", "month": "1983-06"}, {"_id": 19, "total_rainfall": "190", "month": "1983-07"}, {"_id": 20, "total_rainfall": "262.2", "month": "1983-08"}, {"_id": 21, "total_rainfall": "170.8", "month": "1983-09"}, {"_id": 22, "total_rainfall": "212.7", "month": "1983-10"}, {"_id": 23, "total_rainfall": "228.8", "month": "1983-11"}, {"_id": 24, "total_rainfall": "370.6", "month": "1983-12"}, {"_id": 25, "total_rainfall": "251.2", "month": "1984-01"}, {"_id": 26, "total_rainfall": "470.4", "month": "1984-02"}, {"_id": 27, "total_rainfall": "361.3", "month": "1984-03"}, {"_id": 28, "total_rainfall": "153.1", "month": "1984-04"}, {"_id": 29, "total_rainfall": "186.5", "month": "1984-05"}, {"_id": 30, "total_rainfall": "255", "month": "1984-06"}, {"_id": 31, "total_rainfall": "127.2", "month": "1984-07"}, {"_id": 32, "total_rainfall": "102.7", "month": "1984-08"}, {"_id": 33, "total_rainfall": "186.7", "month": "1984-09"}, {"_id": 34, "total_rainfall": "187.5", "month": "1984-10"}, {"_id": 35, "total_rainfall": "127.7", "month": "1984-11"}, {"_id": 36, "total_rainfall": "277.4", "month": "1984-12"}, {"_id": 37, "total_rainfall": "111.1", "month": "1985-01"}, {"_id": 38, "total_rainfall": "79.3", "month": "1985-02"}, {"_id": 39, "total_rainfall": "88", "month": "1985-03"}, {"_id": 40, "total_rainfall": "110.5", "month": "1985-04"}, {"_id": 41, "total_rainfall": "70.1", "month": "1985-05"}, {"_id": 42, "total_rainfall": "37", "month": "1985-06"}, {"_id": 43, "total_rainfall": "131.8", "month": "1985-07"}, {"_id": 44, "total_rainfall": "56.9", "month": "1985-08"}, {"_id": 45, "total_rainfall": "110.7", "month": "1985-09"}, {"_id": 46, "total_rainfall": "169", "month": "1985-10"}, {"_id": 47, "total_rainfall": "179.4", "month": "1985-11"}, {"_id": 48, "total_rainfall": "340.1", "month": "1985-12"}, {"_id": 49, "total_rainfall": "308.2", "month": "1986-01"}, {"_id": 50, "total_rainfall": "26.7", "month": "1986-02"}, {"_id": 51, "total_rainfall": "353.4", "month": "1986-03"}, {"_id": 52, "total_rainfall": "150", "month": "1986-04"}, {"_id": 53, "total_rainfall": "145.1", "month": "1986-05"}, {"_id": 54, "total_rainfall": "122.9", "month": "1986-06"}, {"_id": 55, "total_rainfall": "109.7", "month": "1986-07"}, {"_id": 56, "total_rainfall": "72.9", "month": "1986-08"}, {"_id": 57, "total_rainfall": "396", "month": "1986-09"}, {"_id": 58, "total_rainfall": "227.3", "month": "1986-10"}, {"_id": 59, "total_rainfall": "256.7", "month": "1986-11"}, {"_id": 60, "total_rainfall": "367.2", "month": "1986-12"}, {"_id": 61, "total_rainfall": "568.6", "month": "1987-01"}, {"_id": 62, "total_rainfall": "86.9", "month": "1987-02"}, {"_id": 63, "total_rainfall": "132.5", "month": "1987-03"}, {"_id": 64, "total_rainfall": "72.5", "month": "1987-04"}, {"_id": 65, "total_rainfall": "270", "month": "1987-05"}, {"_id": 66, "total_rainfall": "126.6", "month": "1987-06"}, {"_id": 67, "total_rainfall": "80.9", "month": "1987-07"}, {"_id": 68, "total_rainfall": "191.9", "month": "1987-08"}, {"_id": 69, "total_rainfall": "129.9", "month": "1987-09"}, {"_id": 70, "total_rainfall": "22.6", "month": "1987-10"}, {"_id": 71, "total_rainfall": "347.6", "month": "1987-11"}, {"_id": 72, "total_rainfall": "72.8", "month": "1987-12"}, {"_id": 73, "total_rainfall": "237.5", "month": "1988-01"}, {"_id": 74, "total_rainfall": "158.1", "month": "1988-02"}, {"_id": 75, "total_rainfall": "186.8", "month": "1988-03"}, {"_id": 76, "total_rainfall": "109.6", "month": "1988-04"}, {"_id": 77, "total_rainfall": "229.6", "month": "1988-05"}, {"_id": 78, "total_rainfall": "252.2", "month": "1988-06"}, {"_id": 79, "total_rainfall": "305.4", "month": "1988-07"}, {"_id": 80, "total_rainfall": "80.1", "month": "1988-08"}, {"_id": 81, "total_rainfall": "440.4", "month": "1988-09"}, {"_id": 82, "total_rainfall": "134.6", "month": "1988-10"}, {"_id": 83, "total_rainfall": "401.4", "month": "1988-11"}, {"_id": 84, "total_rainfall": "62.9", "month": "1988-12"}, {"_id": 85, "total_rainfall": "189.7", "month": "1989-01"}, {"_id": 86, "total_rainfall": "52.4", "month": "1989-02"}, {"_id": 87, "total_rainfall": "305.9", "month": "1989-03"}, {"_id": 88, "total_rainfall": "198.6", "month": "1989-04"}, {"_id": 89, "total_rainfall": "194", "month": "1989-05"}, {"_id": 90, "total_rainfall": "117.6", "month": "1989-06"}, {"_id": 91, "total_rainfall": "157.6", "month": "1989-07"}, {"_id": 92, "total_rainfall": "201", "month": "1989-08"}, {"_id": 93, "total_rainfall": "247.3", "month": "1989-09"}, {"_id": 94, "total_rainfall": "111", "month": "1989-10"}, {"_id": 95, "total_rainfall": "508.4", "month": "1989-11"}, {"_id": 96, "total_rainfall": "179.7", "month": "1989-12"}, {"_id": 97, "total_rainfall": "147.4", "month": "1990-01"}, {"_id": 98, "total_rainfall": "24.1", "month": "1990-02"}, {"_id": 99, "total_rainfall": "94.2", "month": "1990-03"}, {"_id": 100, "total_rainfall": "52.4", "month": "1990-04"}, {"_id": 101, "total_rainfall": "180.1", "month": "1990-05"}, {"_id": 102, "total_rainfall": "112.6", "month": "1990-06"}, {"_id": 103, "total_rainfall": "124", "month": "1990-07"}, {"_id": 104, "total_rainfall": "146.6", "month": "1990-08"}, {"_id": 105, "total_rainfall": "204.5", "month": "1990-09"}, {"_id": 106, "total_rainfall": "56.4", "month": "1990-10"}, {"_id": 107, "total_rainfall": "180.4", "month": "1990-11"}, {"_id": 108, "total_rainfall": "201.1", "month": "1990-12"}, {"_id": 109, "total_rainfall": "123.9", "month": "1991-01"}, {"_id": 110, "total_rainfall": "45.5", "month": "1991-02"}, {"_id": 111, "total_rainfall": "92.4", "month": "1991-03"}, {"_id": 112, "total_rainfall": "134.2", "month": "1991-04"}, {"_id": 113, "total_rainfall": "256.4", "month": "1991-05"}, {"_id": 114, "total_rainfall": "88.7", "month": "1991-06"}, {"_id": 115, "total_rainfall": "37.3", "month": "1991-07"}, {"_id": 116, "total_rainfall": "226.2", "month": "1991-08"}, {"_id": 117, "total_rainfall": "123.1", "month": "1991-09"}, {"_id": 118, "total_rainfall": "52", "month": "1991-10"}, {"_id": 119, "total_rainfall": "205", "month": "1991-11"}, {"_id": 120, "total_rainfall": "492.3", "month": "1991-12"}, {"_id": 121, "total_rainfall": "83.9", "month": "1992-01"}, {"_id": 122, "total_rainfall": "62.4", "month": "1992-02"}, {"_id": 123, "total_rainfall": "67.6", "month": "1992-03"}, {"_id": 124, "total_rainfall": "160.3", "month": "1992-04"}, {"_id": 125, "total_rainfall": "63.1", "month": "1992-05"}, {"_id": 126, "total_rainfall": "162.8", "month": "1992-06"}, {"_id": 127, "total_rainfall": "290.8", "month": "1992-07"}, {"_id": 128, "total_rainfall": "76.1", "month": "1992-08"}, {"_id": 129, "total_rainfall": "83.6", "month": "1992-09"}, {"_id": 130, "total_rainfall": "233.2", "month": "1992-10"}, {"_id": 131, "total_rainfall": "474.3", "month": "1992-11"}, {"_id": 132, "total_rainfall": "502.7", "month": "1992-12"}, {"_id": 133, "total_rainfall": "176.4", "month": "1993-01"}, {"_id": 134, "total_rainfall": "69.2", "month": "1993-02"}, {"_id": 135, "total_rainfall": "250.5", "month": "1993-03"}, {"_id": 136, "total_rainfall": "283.9", "month": "1993-04"}, {"_id": 137, "total_rainfall": "129.9", "month": "1993-05"}, {"_id": 138, "total_rainfall": "115.5", "month": "1993-06"}, {"_id": 139, "total_rainfall": "240", "month": "1993-07"}, {"_id": 140, "total_rainfall": "106.8", "month": "1993-08"}, {"_id": 141, "total_rainfall": "61.7", "month": "1993-09"}, {"_id": 142, "total_rainfall": "175.5", "month": "1993-10"}, {"_id": 143, "total_rainfall": "250.8", "month": "1993-11"}, {"_id": 144, "total_rainfall": "308.5", "month": "1993-12"}, {"_id": 145, "total_rainfall": "56.9", "month": "1994-01"}, {"_id": 146, "total_rainfall": "133.5", "month": "1994-02"}, {"_id": 147, "total_rainfall": "288.2", "month": "1994-03"}, {"_id": 148, "total_rainfall": "154", "month": "1994-04"}, {"_id": 149, "total_rainfall": "169.6", "month": "1994-05"}, {"_id": 150, "total_rainfall": "184.7", "month": "1994-06"}, {"_id": 151, "total_rainfall": "53.8", "month": "1994-07"}, {"_id": 152, "total_rainfall": "45.1", "month": "1994-08"}, {"_id": 153, "total_rainfall": "23.7", "month": "1994-09"}, {"_id": 154, "total_rainfall": "84.7", "month": "1994-10"}, {"_id": 155, "total_rainfall": "322.2", "month": "1994-11"}, {"_id": 156, "total_rainfall": "425.4", "month": "1994-12"}, {"_id": 157, "total_rainfall": "349.4", "month": "1995-01"}, {"_id": 158, "total_rainfall": "334", "month": "1995-02"}, {"_id": 159, "total_rainfall": "67.7", "month": "1995-03"}, {"_id": 160, "total_rainfall": "242.3", "month": "1995-04"}, {"_id": 161, "total_rainfall": "84.4", "month": "1995-05"}, {"_id": 162, "total_rainfall": "63.7", "month": "1995-06"}, {"_id": 163, "total_rainfall": "173.6", "month": "1995-07"}, {"_id": 164, "total_rainfall": "211.6", "month": "1995-08"}, {"_id": 165, "total_rainfall": "29.5", "month": "1995-09"}, {"_id": 166, "total_rainfall": "101.1", "month": "1995-10"}, {"_id": 167, "total_rainfall": "372.8", "month": "1995-11"}, {"_id": 168, "total_rainfall": "302.5", "month": "1995-12"}, {"_id": 169, "total_rainfall": "173.2", "month": "1996-01"}, {"_id": 170, "total_rainfall": "180.2", "month": "1996-02"}, {"_id": 171, "total_rainfall": "129.7", "month": "1996-03"}, {"_id": 172, "total_rainfall": "178.2", "month": "1996-04"}, {"_id": 173, "total_rainfall": "107.5", "month": "1996-05"}, {"_id": 174, "total_rainfall": "265.8", "month": "1996-06"}, {"_id": 175, "total_rainfall": "162.3", "month": "1996-07"}, {"_id": 176, "total_rainfall": "258.4", "month": "1996-08"}, {"_id": 177, "total_rainfall": "297", "month": "1996-09"}, {"_id": 178, "total_rainfall": "300", "month": "1996-10"}, {"_id": 179, "total_rainfall": "180.2", "month": "1996-11"}, {"_id": 180, "total_rainfall": "185.5", "month": "1996-12"}, {"_id": 181, "total_rainfall": "15.4", "month": "1997-01"}, {"_id": 182, "total_rainfall": "105.4", "month": "1997-02"}, {"_id": 183, "total_rainfall": "34.3", "month": "1997-03"}, {"_id": 184, "total_rainfall": "118.4", "month": "1997-04"}, {"_id": 185, "total_rainfall": "41.6", "month": "1997-05"}, {"_id": 186, "total_rainfall": "78.9", "month": "1997-06"}, {"_id": 187, "total_rainfall": "18.6", "month": "1997-07"}, {"_id": 188, "total_rainfall": "86.6", "month": "1997-08"}, {"_id": 189, "total_rainfall": "31.1", "month": "1997-09"}, {"_id": 190, "total_rainfall": "78.4", "month": "1997-10"}, {"_id": 191, "total_rainfall": "158.3", "month": "1997-11"}, {"_id": 192, "total_rainfall": "351.9", "month": "1997-12"}, {"_id": 193, "total_rainfall": "268.8", "month": "1998-01"}, {"_id": 194, "total_rainfall": "32.5", "month": "1998-02"}, {"_id": 195, "total_rainfall": "58.8", "month": "1998-03"}, {"_id": 196, "total_rainfall": "187.7", "month": "1998-04"}, {"_id": 197, "total_rainfall": "370.8", "month": "1998-05"}, {"_id": 198, "total_rainfall": "198.8", "month": "1998-06"}, {"_id": 199, "total_rainfall": "259.2", "month": "1998-07"}, {"_id": 200, "total_rainfall": "195", "month": "1998-08"}, {"_id": 201, "total_rainfall": "258.2", "month": "1998-09"}, {"_id": 202, "total_rainfall": "222.7", "month": "1998-10"}, {"_id": 203, "total_rainfall": "107.2", "month": "1998-11"}, {"_id": 204, "total_rainfall": "463.4", "month": "1998-12"}, {"_id": 205, "total_rainfall": "193.9", "month": "1999-01"}, {"_id": 206, "total_rainfall": "67.4", "month": "1999-02"}, {"_id": 207, "total_rainfall": "181.4", "month": "1999-03"}, {"_id": 208, "total_rainfall": "88.5", "month": "1999-04"}, {"_id": 209, "total_rainfall": "157.1", "month": "1999-05"}, {"_id": 210, "total_rainfall": "103.4", "month": "1999-06"}, {"_id": 211, "total_rainfall": "225.4", "month": "1999-07"}, {"_id": 212, "total_rainfall": "204", "month": "1999-08"}, {"_id": 213, "total_rainfall": "125.9", "month": "1999-09"}, {"_id": 214, "total_rainfall": "205", "month": "1999-10"}, {"_id": 215, "total_rainfall": "241.5", "month": "1999-11"}, {"_id": 216, "total_rainfall": "340.5", "month": "1999-12"}, {"_id": 217, "total_rainfall": "275.2", "month": "2000-01"}, {"_id": 218, "total_rainfall": "237.8", "month": "2000-02"}, {"_id": 219, "total_rainfall": "238.3", "month": "2000-03"}, {"_id": 220, "total_rainfall": "311.6", "month": "2000-04"}, {"_id": 221, "total_rainfall": "96.8", "month": "2000-05"}, {"_id": 222, "total_rainfall": "157.5", "month": "2000-06"}, {"_id": 223, "total_rainfall": "116.1", "month": "2000-07"}, {"_id": 224, "total_rainfall": "113.5", "month": "2000-08"}, {"_id": 225, "total_rainfall": "81.1", "month": "2000-09"}, {"_id": 226, "total_rainfall": "120.9", "month": "2000-10"}, {"_id": 227, "total_rainfall": "385.7", "month": "2000-11"}, {"_id": 228, "total_rainfall": "236", "month": "2000-12"}, {"_id": 229, "total_rainfall": "425.8", "month": "2001-01"}, {"_id": 230, "total_rainfall": "86.6", "month": "2001-02"}, {"_id": 231, "total_rainfall": "297.3", "month": "2001-03"}, {"_id": 232, "total_rainfall": "203.3", "month": "2001-04"}, {"_id": 233, "total_rainfall": "164.9", "month": "2001-05"}, {"_id": 234, "total_rainfall": "137.1", "month": "2001-06"}, {"_id": 235, "total_rainfall": "111.3", "month": "2001-07"}, {"_id": 236, "total_rainfall": "158.3", "month": "2001-08"}, {"_id": 237, "total_rainfall": "162", "month": "2001-09"}, {"_id": 238, "total_rainfall": "252.2", "month": "2001-10"}, {"_id": 239, "total_rainfall": "175.3", "month": "2001-11"}, {"_id": 240, "total_rainfall": "609", "month": "2001-12"}, {"_id": 241, "total_rainfall": "221.2", "month": "2002-01"}, {"_id": 242, "total_rainfall": "50.8", "month": "2002-02"}, {"_id": 243, "total_rainfall": "55.6", "month": "2002-03"}, {"_id": 244, "total_rainfall": "116.5", "month": "2002-04"}, {"_id": 245, "total_rainfall": "236.6", "month": "2002-05"}, {"_id": 246, "total_rainfall": "83.1", "month": "2002-06"}, {"_id": 247, "total_rainfall": "233.7", "month": "2002-07"}, {"_id": 248, "total_rainfall": "54.2", "month": "2002-08"}, {"_id": 249, "total_rainfall": "124.2", "month": "2002-09"}, {"_id": 250, "total_rainfall": "10.8", "month": "2002-10"}, {"_id": 251, "total_rainfall": "307.2", "month": "2002-11"}, {"_id": 252, "total_rainfall": "255", "month": "2002-12"}, {"_id": 253, "total_rainfall": "444.2", "month": "2003-01"}, {"_id": 254, "total_rainfall": "172.9", "month": "2003-02"}, {"_id": 255, "total_rainfall": "154.6", "month": "2003-03"}, {"_id": 256, "total_rainfall": "159.9", "month": "2003-04"}, {"_id": 257, "total_rainfall": "81.8", "month": "2003-05"}, {"_id": 258, "total_rainfall": "50.3", "month": "2003-06"}, {"_id": 259, "total_rainfall": "170.4", "month": "2003-07"}, {"_id": 260, "total_rainfall": "193.6", "month": "2003-08"}, {"_id": 261, "total_rainfall": "205.3", "month": "2003-09"}, {"_id": 262, "total_rainfall": "351.4", "month": "2003-10"}, {"_id": 263, "total_rainfall": "133.8", "month": "2003-11"}, {"_id": 264, "total_rainfall": "273", "month": "2003-12"}, {"_id": 265, "total_rainfall": "600.9", "month": "2004-01"}, {"_id": 266, "total_rainfall": "31.9", "month": "2004-02"}, {"_id": 267, "total_rainfall": "269.4", "month": "2004-03"}, {"_id": 268, "total_rainfall": "57.1", "month": "2004-04"}, {"_id": 269, "total_rainfall": "137.6", "month": "2004-05"}, {"_id": 270, "total_rainfall": "127.2", "month": "2004-06"}, {"_id": 271, "total_rainfall": "166.6", "month": "2004-07"}, {"_id": 272, "total_rainfall": "185.2", "month": "2004-08"}, {"_id": 273, "total_rainfall": "128.9", "month": "2004-09"}, {"_id": 274, "total_rainfall": "125.6", "month": "2004-10"}, {"_id": 275, "total_rainfall": "166.2", "month": "2004-11"}, {"_id": 276, "total_rainfall": "139.8", "month": "2004-12"}, {"_id": 277, "total_rainfall": "163.2", "month": "2005-01"}, {"_id": 278, "total_rainfall": "8.4", "month": "2005-02"}, {"_id": 279, "total_rainfall": "82.4", "month": "2005-03"}, {"_id": 280, "total_rainfall": "81.7", "month": "2005-04"}, {"_id": 281, "total_rainfall": "331.1", "month": "2005-05"}, {"_id": 282, "total_rainfall": "82.3", "month": "2005-06"}, {"_id": 283, "total_rainfall": "104", "month": "2005-07"}, {"_id": 284, "total_rainfall": "58.5", "month": "2005-08"}, {"_id": 285, "total_rainfall": "175.7", "month": "2005-09"}, {"_id": 286, "total_rainfall": "314.5", "month": "2005-10"}, {"_id": 287, "total_rainfall": "362.9", "month": "2005-11"}, {"_id": 288, "total_rainfall": "166", "month": "2005-12"}, {"_id": 289, "total_rainfall": "454.4", "month": "2006-01"}, {"_id": 290, "total_rainfall": "115.5", "month": "2006-02"}, {"_id": 291, "total_rainfall": "83.1", "month": "2006-03"}, {"_id": 292, "total_rainfall": "239.8", "month": "2006-04"}, {"_id": 293, "total_rainfall": "205.7", "month": "2006-05"}, {"_id": 294, "total_rainfall": "236.8", "month": "2006-06"}, {"_id": 295, "total_rainfall": "153.8", "month": "2006-07"}, {"_id": 296, "total_rainfall": "127.3", "month": "2006-08"}, {"_id": 297, "total_rainfall": "83.3", "month": "2006-09"}, {"_id": 298, "total_rainfall": "102", "month": "2006-10"}, {"_id": 299, "total_rainfall": "185.6", "month": "2006-11"}, {"_id": 300, "total_rainfall": "765.9", "month": "2006-12"}, {"_id": 301, "total_rainfall": "450.1", "month": "2007-01"}, {"_id": 302, "total_rainfall": "105.5", "month": "2007-02"}, {"_id": 303, "total_rainfall": "269.1", "month": "2007-03"}, {"_id": 304, "total_rainfall": "240.2", "month": "2007-04"}, {"_id": 305, "total_rainfall": "127.2", "month": "2007-05"}, {"_id": 306, "total_rainfall": "139", "month": "2007-06"}, {"_id": 307, "total_rainfall": "141.7", "month": "2007-07"}, {"_id": 308, "total_rainfall": "190.7", "month": "2007-08"}, {"_id": 309, "total_rainfall": "149", "month": "2007-09"}, {"_id": 310, "total_rainfall": "237.2", "month": "2007-10"}, {"_id": 311, "total_rainfall": "367.9", "month": "2007-11"}, {"_id": 312, "total_rainfall": "468.6", "month": "2007-12"}, {"_id": 313, "total_rainfall": "262.6", "month": "2008-01"}, {"_id": 314, "total_rainfall": "129.2", "month": "2008-02"}, {"_id": 315, "total_rainfall": "294.1", "month": "2008-03"}, {"_id": 316, "total_rainfall": "87.2", "month": "2008-04"}, {"_id": 317, "total_rainfall": "124.9", "month": "2008-05"}, {"_id": 318, "total_rainfall": "118.3", "month": "2008-06"}, {"_id": 319, "total_rainfall": "89.1", "month": "2008-07"}, {"_id": 320, "total_rainfall": "327.3", "month": "2008-08"}, {"_id": 321, "total_rainfall": "164.4", "month": "2008-09"}, {"_id": 322, "total_rainfall": "159.5", "month": "2008-10"}, {"_id": 323, "total_rainfall": "324.3", "month": "2008-11"}, {"_id": 324, "total_rainfall": "244.2", "month": "2008-12"}, {"_id": 325, "total_rainfall": "38.3", "month": "2009-01"}, {"_id": 326, "total_rainfall": "201.8", "month": "2009-02"}, {"_id": 327, "total_rainfall": "223.3", "month": "2009-03"}, {"_id": 328, "total_rainfall": "183.7", "month": "2009-04"}, {"_id": 329, "total_rainfall": "198.6", "month": "2009-05"}, {"_id": 330, "total_rainfall": "21.8", "month": "2009-06"}, {"_id": 331, "total_rainfall": "161", "month": "2009-07"}, {"_id": 332, "total_rainfall": "177.8", "month": "2009-08"}, {"_id": 333, "total_rainfall": "109.6", "month": "2009-09"}, {"_id": 334, "total_rainfall": "133.4", "month": "2009-10"}, {"_id": 335, "total_rainfall": "281.8", "month": "2009-11"}, {"_id": 336, "total_rainfall": "189.8", "month": "2009-12"}, {"_id": 337, "total_rainfall": "69.5", "month": "2010-01"}, {"_id": 338, "total_rainfall": "6.3", "month": "2010-02"}, {"_id": 339, "total_rainfall": "238", "month": "2010-03"}, {"_id": 340, "total_rainfall": "158.5", "month": "2010-04"}, {"_id": 341, "total_rainfall": "157.5", "month": "2010-05"}, {"_id": 342, "total_rainfall": "240.5", "month": "2010-06"}, {"_id": 343, "total_rainfall": "298.5", "month": "2010-07"}, {"_id": 344, "total_rainfall": "158.4", "month": "2010-08"}, {"_id": 345, "total_rainfall": "121.5", "month": "2010-09"}, {"_id": 346, "total_rainfall": "166.2", "month": "2010-10"}, {"_id": 347, "total_rainfall": "278.8", "month": "2010-11"}, {"_id": 348, "total_rainfall": "181.4", "month": "2010-12"}, {"_id": 349, "total_rainfall": "513.2", "month": "2011-01"}, {"_id": 350, "total_rainfall": "23", "month": "2011-02"}, {"_id": 351, "total_rainfall": "256.6", "month": "2011-03"}, {"_id": 352, "total_rainfall": "217.8", "month": "2011-04"}, {"_id": 353, "total_rainfall": "127", "month": "2011-05"}, {"_id": 354, "total_rainfall": "213", "month": "2011-06"}, {"_id": 355, "total_rainfall": "76.6", "month": "2011-07"}, {"_id": 356, "total_rainfall": "81.4", "month": "2011-08"}, {"_id": 357, "total_rainfall": "136.4", "month": "2011-09"}, {"_id": 358, "total_rainfall": "216.8", "month": "2011-10"}, {"_id": 359, "total_rainfall": "377.8", "month": "2011-11"}, {"_id": 360, "total_rainfall": "284.6", "month": "2011-12"}, {"_id": 361, "total_rainfall": "106.1", "month": "2012-01"}, {"_id": 362, "total_rainfall": "83.6", "month": "2012-02"}, {"_id": 363, "total_rainfall": "313.4", "month": "2012-03"}, {"_id": 364, "total_rainfall": "260.6", "month": "2012-04"}, {"_id": 365, "total_rainfall": "292", "month": "2012-05"}, {"_id": 366, "total_rainfall": "53", "month": "2012-06"}, {"_id": 367, "total_rainfall": "130.8", "month": "2012-07"}, {"_id": 368, "total_rainfall": "119", "month": "2012-08"}, {"_id": 369, "total_rainfall": "107.6", "month": "2012-09"}, {"_id": 370, "total_rainfall": "122.2", "month": "2012-10"}, {"_id": 371, "total_rainfall": "208.2", "month": "2012-11"}, {"_id": 372, "total_rainfall": "363.4", "month": "2012-12"}, {"_id": 373, "total_rainfall": "262", "month": "2013-01"}, {"_id": 374, "total_rainfall": "395.2", "month": "2013-02"}, {"_id": 375, "total_rainfall": "85.8", "month": "2013-03"}, {"_id": 376, "total_rainfall": "159.4", "month": "2013-04"}, {"_id": 377, "total_rainfall": "211.4", "month": "2013-05"}, {"_id": 378, "total_rainfall": "111.4", "month": "2013-06"}, {"_id": 379, "total_rainfall": "174.6", "month": "2013-07"}, {"_id": 380, "total_rainfall": "165.6", "month": "2013-08"}, {"_id": 381, "total_rainfall": "257", "month": "2013-09"}, {"_id": 382, "total_rainfall": "285.4", "month": "2013-10"}, {"_id": 383, "total_rainfall": "292.4", "month": "2013-11"}, {"_id": 384, "total_rainfall": "348.2", "month": "2013-12"}, {"_id": 385, "total_rainfall": "75.4", "month": "2014-01"}, {"_id": 386, "total_rainfall": "0.2", "month": "2014-02"}, {"_id": 387, "total_rainfall": "66", "month": "2014-03"}, {"_id": 388, "total_rainfall": "110", "month": "2014-04"}, {"_id": 389, "total_rainfall": "125.8", "month": "2014-05"}, {"_id": 390, "total_rainfall": "71.4", "month": "2014-06"}, {"_id": 391, "total_rainfall": "148.6", "month": "2014-07"}, {"_id": 392, "total_rainfall": "241", "month": "2014-08"}, {"_id": 393, "total_rainfall": "83.6", "month": "2014-09"}, {"_id": 394, "total_rainfall": "120", "month": "2014-10"}, {"_id": 395, "total_rainfall": "250.8", "month": "2014-11"}, {"_id": 396, "total_rainfall": "245.6", "month": "2014-12"}, {"_id": 397, "total_rainfall": "79.6", "month": "2015-01"}, {"_id": 398, "total_rainfall": "18.8", "month": "2015-02"}, {"_id": 399, "total_rainfall": "84.4", "month": "2015-03"}, {"_id": 400, "total_rainfall": "73.2", "month": "2015-04"}, {"_id": 401, "total_rainfall": "89", "month": "2015-05"}, {"_id": 402, "total_rainfall": "95.8", "month": "2015-06"}, {"_id": 403, "total_rainfall": "116.8", "month": "2015-07"}, {"_id": 404, "total_rainfall": "185.8", "month": "2015-08"}, {"_id": 405, "total_rainfall": "61.6", "month": "2015-09"}, {"_id": 406, "total_rainfall": "87.2", "month": "2015-10"}, {"_id": 407, "total_rainfall": "72.6", "month": "2015-11"}, {"_id": 408, "total_rainfall": "302.3", "month": "2015-12"}, {"_id": 409, "total_rainfall": "126.6", "month": "2016-01"}, {"_id": 410, "total_rainfall": "186", "month": "2016-02"}, {"_id": 411, "total_rainfall": "6.2", "month": "2016-03"}, {"_id": 412, "total_rainfall": "89.8", "month": "2016-04"}, {"_id": 413, "total_rainfall": "193.8", "month": "2016-05"}, {"_id": 414, "total_rainfall": "162.8", "month": "2016-06"}, {"_id": 415, "total_rainfall": "168.6", "month": "2016-07"}, {"_id": 416, "total_rainfall": "139.2", "month": "2016-08"}, {"_id": 417, "total_rainfall": "118.9", "month": "2016-09"}, {"_id": 418, "total_rainfall": "181", "month": "2016-10"}, {"_id": 419, "total_rainfall": "290.2", "month": "2016-11"}, {"_id": 420, "total_rainfall": "292.6", "month": "2016-12"}, {"_id": 421, "total_rainfall": "197.6", "month": "2017-01"}, {"_id": 422, "total_rainfall": "158.4", "month": "2017-02"}, {"_id": 423, "total_rainfall": "136.2", "month": "2017-03"}, {"_id": 424, "total_rainfall": "208.6", "month": "2017-04"}, {"_id": 425, "total_rainfall": "190", "month": "2017-05"}, {"_id": 426, "total_rainfall": "106", "month": "2017-06"}, {"_id": 427, "total_rainfall": "79.6", "month": "2017-07"}, {"_id": 428, "total_rainfall": "84.2", "month": "2017-08"}, {"_id": 429, "total_rainfall": "124.4", "month": "2017-09"}, {"_id": 430, "total_rainfall": "120.8", "month": "2017-10"}, {"_id": 431, "total_rainfall": "268.6", "month": "2017-11"}, {"_id": 432, "total_rainfall": "371.2", "month": "2017-12"}, {"_id": 433, "total_rainfall": "287", "month": "2018-01"}, {"_id": 434, "total_rainfall": "14.8", "month": "2018-02"}, {"_id": 435, "total_rainfall": "44.6", "month": "2018-03"}, {"_id": 436, "total_rainfall": "61.2", "month": "2018-04"}, {"_id": 437, "total_rainfall": "132.2", "month": "2018-05"}, {"_id": 438, "total_rainfall": "182.6", "month": "2018-06"}, {"_id": 439, "total_rainfall": "143.2", "month": "2018-07"}, {"_id": 440, "total_rainfall": "121.6", "month": "2018-08"}, {"_id": 441, "total_rainfall": "144.4", "month": "2018-09"}, {"_id": 442, "total_rainfall": "234.4", "month": "2018-10"}, {"_id": 443, "total_rainfall": "169.6", "month": "2018-11"}, {"_id": 444, "total_rainfall": "172.6", "month": "2018-12"}, {"_id": 445, "total_rainfall": "63.6", "month": "2019-01"}, {"_id": 446, "total_rainfall": "31.6", "month": "2019-02"}, {"_id": 447, "total_rainfall": "72.2", "month": "2019-03"}, {"_id": 448, "total_rainfall": "174.8", "month": "2019-04"}, {"_id": 449, "total_rainfall": "69", "month": "2019-05"}, {"_id": 450, "total_rainfall": "173.8", "month": "2019-06"}, {"_id": 451, "total_rainfall": "12.2", "month": "2019-07"}, {"_id": 452, "total_rainfall": "11.8", "month": "2019-08"}, {"_id": 453, "total_rainfall": "22.8", "month": "2019-09"}, {"_id": 454, "total_rainfall": "176.8", "month": "2019-10"}, {"_id": 455, "total_rainfall": "137.4", "month": "2019-11"}, {"_id": 456, "total_rainfall": "421.5", "month": "2019-12"}, {"_id": 457, "total_rainfall": "88.4", "month": "2020-01"}, {"_id": 458, "total_rainfall": "65", "month": "2020-02"}, {"_id": 459, "total_rainfall": "108.8", "month": "2020-03"}, {"_id": 460, "total_rainfall": "188", "month": "2020-04"}, {"_id": 461, "total_rainfall": "255.6", "month": "2020-05"}, {"_id": 462, "total_rainfall": "233.8", "month": "2020-06"}, {"_id": 463, "total_rainfall": "140.8", "month": "2020-07"}, {"_id": 464, "total_rainfall": "103.4", "month": "2020-08"}, {"_id": 465, "total_rainfall": "150.2", "month": "2020-09"}, {"_id": 466, "total_rainfall": "78.8", "month": "2020-10"}, {"_id": 467, "total_rainfall": "220.6", "month": "2020-11"}, {"_id": 468, "total_rainfall": "253.2", "month": "2020-12"}, {"_id": 469, "total_rainfall": "692.8", "month": "2021-01"}, {"_id": 470, "total_rainfall": "1", "month": "2021-02"}, {"_id": 471, "total_rainfall": "182.4", "month": "2021-03"}, {"_id": 472, "total_rainfall": "290.4", "month": "2021-04"}, {"_id": 473, "total_rainfall": "245.8", "month": "2021-05"}, {"_id": 474, "total_rainfall": "93.4", "month": "2021-06"}, {"_id": 475, "total_rainfall": "195.8", "month": "2021-07"}, {"_id": 476, "total_rainfall": "293.6", "month": "2021-08"}]
data = pd.DataFrame(data)
del data["_id"]
data.set_index(["month"],inplace=True)
data.index = pd.to_datetime(data.index)
data.total_rainfall = pd.to_numeric(data.total_rainfall)
data.head()


# In[67]:


# data.to_excel("monthrainfall.xlsx")


# In[68]:


# Downsampling: Convert monthly data to yearly data by sum and max
df = data
dfsum = df.resample("Y").sum()
dfsum.head()


# In[69]:


dfmax = df.resample("Y").max()
dfmax.head()


# In[70]:


# Upsampling: Convert monthly data to yearly data by sum and max
dfmax.resample('10D').asfreq()[0:5]


# In[71]:


dfmax.resample('10D').pad()[0:5]


# In[72]:


dfmax.resample('D').ffill(limit=2)[0:5]


# ## Hierarchical indexing (MultiIndex)

# ### Creating a MultiIndex

# In[73]:


iterables = [
    ["temperature","rainfall","runoff"],
    ["max","mean","min"],
]
idx = pd.MultiIndex.from_product(iterables, names=["factor", "method"])
idx


# In[74]:


df = pd.DataFrame(np.random.randn(9, 4), index=idx)
df


# In[75]:


idx = pd.MultiIndex.from_arrays(iterables, names=["factor", "method"])
idx


# In[76]:


df = pd.DataFrame(np.random.randn(3, 4), index=idx)
df


# ```pd.MultiIndex.from_tuples```, ```pd.MultiIndex.from_frame```

# ### Get index for multiindex

# In[77]:


iterables = [
    ["temperature","rainfall","runoff"],
    ["max","mean","min"],
]
idx = pd.MultiIndex.from_product(iterables, names=["factor", "method"])
df = pd.DataFrame(np.random.randn(9, 4), index=idx)
df.index


# In[78]:


df.index.get_level_values(0)


# In[79]:


df.index.get_level_values(1)


# ## Apply and Applymap
# * Apply: Apply a function along an axis of the DataFrame.
# * Applymap: Apply a function to a Dataframe elementwise. You can address each element for specfic requirements.

# In[80]:


df = pd.DataFrame(np.random.randn(3, 4))
df


# In[81]:


df.apply(np.abs)


# In[82]:


func_x3 = lambda x: x**3 # lambda functiodn
df.apply(func_x3)


# In[83]:


# This function don't have specific meaning. 
# It only defines a complex operation for each element of dataframe.
def func_range(x):
    if x > 1:
        return 1
    elif x< -1:
        return -1
    else:
        return np.abs(x)
df.applymap(func_range)


# ## Groupby
# `Groupby()` can be used to group large amounts of data and compute operations on these groups.
# 
# 

# In[84]:


iterables = [
    ["temperature","rainfall","runoff"],
    ["site1","site2","site3"],
]
idx = pd.MultiIndex.from_product(iterables, names=["factor", "method"])
df = pd.DataFrame(np.random.randn(9, 4), index=idx)
for n,subdf in df.groupby(by=["factor"]):
    print(n)
    print(subdf)


# In[85]:


df.groupby(by=["factor"]).mean()


# ## Advanced (operational)

# ## Table Visualization

# In[86]:


np.random.seed(0)
df2 = pd.DataFrame(np.random.randn(10,4), columns=['A','B','C','D'])
df2.style
def style_negative(v, props=''):
    return props if v < 0 else None
s2 = df2.style.applymap(style_negative, props='color:red;')              .applymap(lambda v: 'opacity: 20%;' if (v < 0.3) and (v > -0.3) else None)
s2


# In[87]:


def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), props, '')
s2.apply(highlight_max, props='color:white;background-color:darkblue', axis=0)


# ## Tooltips and Captions

# In[88]:


# s.set_caption("Confusion matrix for multiple cancer prediction models.")\
#  .set_table_styles([{
#      'selector': 'caption',
#      'props': 'caption-side: bottom; font-size:1.25em;'
#  }], overwrite=False)

