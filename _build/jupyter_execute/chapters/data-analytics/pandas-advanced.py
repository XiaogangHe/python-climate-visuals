#!/usr/bin/env python
# coding: utf-8

# # Pandas tutorial (Advanced)

# The following content is the **Advanced**  part. Please make sure you have studied the **Basic**  part before you start.

# In[1]:


import pandas as pd
import numpy as np
np.random.seed(0)


# ## Hierarchical indexing (MultiIndex)

# ### Creating a MultiIndex

# In[2]:


iterables = [
    ["temperature","rainfall","runoff"],
    ["max","mean","min"],
]
idx = pd.MultiIndex.from_product(iterables, names=["factor", "method"])
idx


# In[3]:


df = pd.DataFrame(np.random.randn(9, 4), index=idx)
df


# In[4]:


idx = pd.MultiIndex.from_arrays(iterables, names=["factor", "method"])
idx


# In[5]:


df = pd.DataFrame(np.random.randn(3, 4), index=idx)
df


# You can  use `pd.MultiIndex.from_tuples()`, `pd.MultiIndex.from_frame()` to create a MultiIndex

# ### Get single index for a MultiIndex

# In[6]:


iterables = [
    ["temperature","rainfall","runoff"],
    ["max","mean","min"],
]
idx = pd.MultiIndex.from_product(iterables, names=["factor", "method"])
df = pd.DataFrame(np.random.randn(9, 4), index=idx)
df.index


# In[7]:


df.index.get_level_values(0)


# In[8]:


df.index.get_level_values(1)


# ## Apply and Applymap
# * Apply: Apply a function along an axis of the DataFrame.
# * Applymap: Apply a function to a Dataframe elementwise. You can address each element for specfic requirements.

# In[9]:


df = pd.DataFrame(np.random.randn(3, 4))
df


# In[10]:


df.apply(np.abs)


# In[11]:


func_x3 = lambda x: x**3 # lambda functiodn
df.apply(func_x3)


# In[12]:


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

# In[13]:


df = pd.DataFrame(np.random.randn(9, 4), index=idx)
for n,subdf in df.groupby(by=["factor"]):
    print(n)
    print(subdf)


# In[14]:


df.groupby(by=["factor"]).mean()


# The dataframe generated is daily rainfall of Changi station in 2020. The columns and index represent no. of month and day, respectively.

# In[15]:


df = pd.read_csv('../../assets/data/Changi_daily_rainfall.csv', index_col=0, header=0, parse_dates=True)
df1 = df.copy(deep=True)
df1 = pd.concat([i[1].reset_index(drop=True) for i in df1.loc['2020',:].groupby(pd.Grouper(freq='M'))], axis=1)
df1.columns = range(1, 13)
df1.index = range(1, 32)
df1.columns.name = 'month'
df1.index.name = 'day'
df1


# The dataframe generated is monthly rainfall of Changi station from 2010 to 2020. The columns and index represent no. of year and month, respectively.

# In[16]:


dfmonth = df.resample('M').sum()
dfmonth = pd.concat([i[1].reset_index(drop=True) for i in dfmonth.loc['2015':'2020',:].groupby(pd.Grouper(freq='Y'))], axis=1)
dfmonth.columns = range(2015, 2021)
dfmonth.index = range(1, 13)
dfmonth.columns.name = 'year'
dfmonth.index.name = 'month'
dfmonth


# ## Table Visualization

# ### Styler Functions

# In[17]:


# highlight monthly rainfall which is greater than 200 mm and less than 50 mm
def highlight_G200(s, props=''):
    return props if s>200 else None
def highlight_L50(s, props=''):
    return props if s<50 else None
s = dfmonth.style
s.precision = 1
s.applymap(highlight_G200, props='color:#3333ff')
s.applymap(highlight_L50, props='color:#ff3333')


# In[18]:


def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), 'background-color:#3399ff', '')
def highlight_min(s, props=''):
    return np.where(s == np.nanmin(s.values), 'background-color:#c0c0c0', '')
s = dfmonth.style
s.precision = 1
s.apply(highlight_max, axis=0)
s.apply(highlight_min, axis=0)


# In[19]:


# since version 1.3.0
v = pd.__version__.split('.') 
if int(v[0]) >= 1 and int(v[1]) >= 3:
    pass
else:
    raise Exception('Please make sure your pandas version >= 1.3.0, Current version is {}'.format(pd.__version__))
tt = pd.DataFrame([['A typhoon landed this month!',
                    "There was a severe drought this month!"]],
                  index=[3,12], columns=[2016,2017])
s.set_tooltips(tt, props='visibility: hidden; position: absolute; z-index: 1; border: 1px solid #000066;'
                         'background-color: white; color: #000066; font-size: 0.8em;'
                         'transform: translate(0px, -24px); padding: 0.6em; border-radius: 0.5em;')
# move mouse over (3,2016) and (12,2017)


# ### Builtin Styles

# #### Highlight maximum and minmum

# In[20]:


s = dfmonth.style.highlight_max(axis=0, color='#3399ff')
s.precision = 1
s.highlight_min(axis=0, color='#c0c0c0')


# #### Bar charts

# In[21]:


s = dfmonth.style.bar(color='#3399ff')
s.precision = 1
s


# ## Chart Visualization

# Plots of this section are  based on the `matplotlib` which will be introduced in the following tutorial in this book. You can call `Series.plot()` or `DataFrame.plot()` directly plot and make different charts by setting `kind` argument. 

# ### line plot

# In[22]:


df.loc['2020',:].plot(title='Daily rainfall of Changi station', color='#3399ff')


# ### bar plot

# In[23]:


import matplotlib.dates as mdates
df1 = df.loc['2020',:]
ax = df1.plot(title='Daily rainfall of Changi station in 2020', kind='bar', xticks=[])


# ### Histograms

# In[24]:


ax = df1.plot(title='Daily rainfall of Changi station in 2020', kind='hist', alpha=0.5)


# ### Box plots

# In[25]:


dfmonth = df.resample('M').sum()
dfmonth = pd.concat([i[1].reset_index(drop=True) for i in dfmonth.loc['1981':'2020',:].groupby(pd.Grouper(freq='Y'))], axis=1)
dfmonth.columns = range(1981, 2021)
dfmonth.index = range(1, 13)
dfmonth.columns.name = 'year'
dfmonth.index.name = 'month'
ax = dfmonth.plot(title='Monthly rainfall of Changi station in from 1981 to 2020', xlabel='year', 
             ylabel='Monthly rainfall (mm)', kind='box', figsize=(15,5))
ax.set_xticklabels(dfmonth.columns,rotation=45)
ax.set_xlabel('year')


# ### Area plot

# In[26]:


ax = df.loc['2020',:].resample('M').sum().plot(title='Daily rainfall of Changi station in 2020',
                                               kind='area', alpha=0.5)


# ### Scatter plot

# You need to specify the `x` and `y` arguments for scatter plot.

# In[27]:


df1 = df.loc['2020',:].resample('M').sum().reset_index()
df1.head()


# In[28]:


df1.plot(x='Date', y='Daily Rainfall Total (mm)', title='Daily rainfall of Changi station in 2020',
                                               kind='scatter')


# ### Pie plot

# In[29]:


df1 = df.loc['2020',:].resample('M').sum()
df1.index = df1.index.month
df1.head()


# In[30]:


df1.plot(y='Daily Rainfall Total (mm)', title='Daily rainfall of Changi station in 2020',
                                               kind='pie')


# ## References
# + [Pandas documentation](https://pandas.pydata.org/docs/).
# + [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
