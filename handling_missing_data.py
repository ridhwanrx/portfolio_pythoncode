#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
ufo = pd.read_csv('C:\\Users\\Apeh\\Desktop\\CODE\\DATASET\\ufo.csv')
ufo.head()


# In[3]:


# EXPLORE THE DATA
ufo.columns


# In[4]:


ufo.shape 


# In[5]:


# CHECKING THE MISSING DATA
ufo.isnull().head(10)


# In[6]:


# CHECKING THE VALUE OF MISSING DATA
ufo.isnull().sum()


# In[8]:


# PRINT COL THAT INVOLVE IN MISSING DATA
ufo[ufo.City.isnull()]


# In[9]:


# HANDLING THE MISSING DATA START WITH COLUMN
ufo.columns


# In[10]:


ufo.columns = ufo.columns.str.strip().str.lower().str.replace(' ','_')
ufo.columns


# In[11]:


ufo[ufo.shape_reported.isnull()].head(3)


# In[12]:


ufo.shape


# In[13]:


ufo.dropna().shape


# In[18]:


# ANOTHER APPROACH
ufo['shape_reported'].value_counts(dropna=False)


# In[19]:


ufo['shape_reported'].fillna(value='VARIOUS',inplace=True)
ufo['shape_reported'].value_counts()


# In[20]:


# CHECK ANY MISSING VA AFTER CLEANING
ufo.isnull().sum()


# In[21]:


# COLORS
ufo['colors_reported'].value_counts(dropna=False)


# In[22]:


ufo['colors_reported'].fillna(value='UNIDENTIFIED COLORS',inplace=True)
ufo['colors_reported'].value_counts()


# In[23]:


ufo.isnull().sum()

