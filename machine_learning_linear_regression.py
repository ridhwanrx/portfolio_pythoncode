#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Predict Student Marks on the Basis of Number of Hours Studied

# Load the Dataset
import pandas as pd
data = pd.read_csv('C:\\Users\\Apeh\\Desktop\\CODE\\DATASET\\Grade_Set_1.csv')
data


# In[22]:


# Explore Data
data.columns


# In[23]:


data.shape


# In[24]:


# Missing Value?
data.isnull().sum()


# In[25]:


# Convert the Categorical Value
from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()
data.Status = lb.fit_transform(data.Status)


# In[26]:


data


# In[27]:


# Dependent & Independent Variables
import numpy as np
x = data.Hours_Studied.values
x = x.reshape(9,1)


# In[28]:


x.shape
x


# In[29]:


y = data.Test_Grade.values
y


# In[30]:


# Train the Dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()


# In[31]:


lin_reg.fit(x,y)


# In[32]:


pred_val = lin_reg.predict(x)
pred_val


# In[34]:


# Compare the predicted val with original val
data['predicted_values'] = pred_val
data[['Hours_Studied','predicted_values','Test_Grade']]


# In[35]:


# Evaluate Model Performance
from sklearn.metrics import  r2_score
accuracy = r2_score(y,pred_val)
print('Accuracy : ', accuracy)


# In[36]:


# Final Prediction
hrs = float(input('How many hours have you studied? : '))
marks = lin_reg.predict([[hrs]])
print('Student who strudies for', hrs,
      'hours will going to score', marks, 'marks.')

