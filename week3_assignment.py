#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Suppose you have ridden a bicycle from New York City to Key West, Florida.  
# Your bicycle odometer shows the total miles, which you have dutifully logged at the end of each day 
# with paper and pencil.  Your first two entries might be 55 and 120, 
# indicating that you rode your bike 55 miles on day 1 and 65 miles on day 2.  

# Your task is to create a pandas Series object that holds the cumulative miles at the end of each day, 
# then use your Python skills to show the total miles that you rode each day.  
# Consider how you should best present this information in a Jupyter notebook.  
# You should save your Jupyter Notebook to your GitHub repository, 
# and provide a link in your assignment submission.

# Saar Turjeman
# assignment# 3
# cuny_sps - spring_2024


# In[1]:


import numpy as np
import pandas as pd


# In[5]:


# series of two days, first day indicating 55 miles, 2nd day indicating 65 miles
s = pd.Series([55, 65], index=('day1 day2'.split()))
s


# In[11]:


# total miles rode on day1 and day2
total_miles = s.sum()
total_miles


# In[15]:


# print the total miles rode
print(f'The total miles ridden is {total_miles} miles')


# In[ ]:




