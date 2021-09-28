#!/usr/bin/env python
# coding: utf-8

# # Advanced

# The following content is the **Advanced**  part. Please make sure you have studied the **Basic**  part before you start.

# In[1]:


import pandas as pd
import numpy as np


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


# ```pd.MultiIndex.from_tuples```, ```pd.MultiIndex.from_frame```

# ### Get index for multiindex

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


iterables = [
    ["temperature","rainfall","runoff"],
    ["site1","site2","site3"],
]
idx = pd.MultiIndex.from_product(iterables, names=["factor", "method"])
df = pd.DataFrame(np.random.randn(9, 4), index=idx)
for n,subdf in df.groupby(by=["factor"]):
    print(n)
    print(subdf)


# In[14]:


df.groupby(by=["factor"]).mean()


# ## Table Visualization

# In[15]:


np.random.seed(0)
df2 = pd.DataFrame(np.random.randn(10,4), columns=['A','B','C','D'])
df2.style
def style_negative(v, props=''):
    return props if v < 0 else None
s2 = df2.style.applymap(style_negative, props='color:red;')              .applymap(lambda v: 'opacity: 20%;' if (v < 0.3) and (v > -0.3) else None)
s2


# In[16]:


def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), props, '')
s2.apply(highlight_max, props='color:white;background-color:darkblue', axis=0)


# ## Tooltips and Captions

# In[17]:


# s.set_caption("Confusion matrix for multiple cancer prediction models.")\
#  .set_table_styles([{
#      'selector': 'caption',
#      'props': 'caption-side: bottom; font-size:1.25em;'
#  }], overwrite=False)

