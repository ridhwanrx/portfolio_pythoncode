#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[4]:


# GENERATE A LINE GRAPH
from matplotlib import style
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label='Line One',linewidth=5)    
plt.plot(x2,y2,'c',label='Line Two',linewidth=5)  
plt.title('Info')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()                                      
plt.grid(True,color='k')
plt.show()


# In[5]:


# GENERATE A BAR GRAPH
plt.bar([1,3,5,7,9],[5,2,7,8,2],label='Example One')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='Example Two')
plt.legend()
plt.title('Bar Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()


# In[6]:


# SCATTER PLOT
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
plt.scatter(x,y,label='Scatter',color='g',
            s=25,marker='v')   
plt.title('Scatter Plot')                     
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()


# In[8]:


#PIE CHART
slices = [7,2,2,13]
activities = ['Sleeping','Eating','Playing','Working']
cols = ['c','m','r','y']
plt.pie(slices,
        labels = activities,
        colors = cols,
        startangle = 90,
        shadow = True,
        explode = (0,0.1,0,0),
        autopct = '%1.1f%%')
plt.show()


# In[10]:


# USING DIFFERENT STYLE
from matplotlib import style
style.use('classic')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,label='Line One')    
plt.plot(x2,y2,label='Line Two')  
plt.title('Info')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()                                       
plt.grid(True)
plt.show()


# In[12]:


import pandas as pd
df = pd.read_csv('C:\\Users\\Apeh\\Desktop\\CODE\\DATASET\\Grade_Set_1.csv')
df


# In[13]:


from matplotlib import style
style.use('dark_background')


# In[14]:


plt.scatter(df.Hours_Studied,df.Test_Grade,color='red')
plt.plot(df.Hours_Studied,df.Test_Grade,color='green',label='Loaded from URL')
plt.xlabel('Hours')
plt.ylabel('Marks')
plt.title('Student Grade Pradiction')
plt.legend()
plt.grid(True)
plt.show()

