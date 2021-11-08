#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('C:\\Users\\Apeh\\Desktop\\CODE\\DATASET\\sample.csv')
df


# In[5]:


# CHECK THE MISSING DATA
df.isnull().sum()


# In[6]:


# USING FOWARD FILL METHOD
df['Marks'].fillna(method='ffill',inplace=True)
df


# In[7]:


# BACKWARD FILL METHOS
df['Percentage'].fillna(method='bfill',inplace=True)
df


# In[8]:


# CHECK MISSING VAL AFTER CLEANING
df.isnull().sum()


# In[9]:


# OPTION : MEAN METHOD
df1 = pd.read_csv('C:\\Users\\Apeh\\Desktop\\CODE\\DATASET\\sample.csv')
df1


# In[10]:


per_mean = df1['Percentage'].mean()
per_mean


# In[11]:


df1['Percentage'].fillna(value=per_mean,inplace = True)
df1

