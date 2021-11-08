#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install gTTS')


# In[5]:


from gtts import gTTS
myText = 'Hello everyone welcome to Kuala Lumpur'
language = 'en'
myObj = gTTS(text=myText, lang=language, slow=False)
myObj.save('D:\\csv_savefiles\\greetings_bot.mp3')

