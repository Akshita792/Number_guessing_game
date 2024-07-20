#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Number guessing game


# In[23]:


# importing libraries


# In[24]:


import math
import random


# In[25]:


# taking inputs


# In[26]:


a = int(input("Enter an upper bound:")) 


# In[27]:


b = int(input("Enter a lower bound:"))


# In[31]:


x=random.randint(b,a)
# print(x)


# In[29]:


numb = int(input("Guess a number:"))


# In[30]:


if x==numb:
    print ("You won!")
else:
    print ("You lost")


# In[ ]:





# In[ ]:




