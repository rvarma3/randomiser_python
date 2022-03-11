#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os as os
from itertools import filterfalse
import fnmatch

from IPython.display import Markdown, display
print ('Done')


# In[2]:



os.listdir('.')




# In[3]:


#file_name = 'Randomiser test data'

a =[]
b =[]
c =[]
for file in os.listdir('.'):
    if fnmatch.fnmatch(file,  "*.xlsx"):
        a = file
    elif fnmatch.fnmatch(file,  "*.csv"):
        b = file
    elif fnmatch.fnmatch(file,  "*.txt"):
        c = file
print ('Done')


# In[4]:


#read in the data file that will feed the randomizer

# check the format and assign the dataframe

if os.path.isfile('./{}'.format(a)) & (os.path.splitext('./{}'.format(a))[1] == '.xlsx'):
    df = pd.read_excel('./{}'.format(a) , converters=  {'Membership no' : str  } )
elif os.path.isfile('./{}'.format(b) ) & (os.path.splitext('./{}'.format(b))[1] == '.csv'):
    df = pd.read_csv('./{}'.format(b) , converters=  {'Membership no' : str  } , sep = ',' )
elif os.path.isfile('./{}'.format(c) ) & (os.path.splitext('./{}'.format(b))[1] == '.txt'):
    df = pd.read_csv('./{}'.format(c) , converters=  {'Membership no' : str  } , sep = '/t' )
        

print ('Done')


# In[5]:


# check if the firs 5 records match the excel sheet

df.head(5)


# In[6]:


# check if the last 4 records match tht excel sheet

df.tail(5)


# In[7]:


# check the number of records in the dataset and if they tally with excel sheet

df.shape


# In[8]:


# repeat the records based on the number of entries

repeat_df = df.loc[df.index.repeat(df.iloc[:,1])]


# In[9]:


repeat_df.shape


# In[10]:


# force the python to read the object as a list

random_df = list(repeat_df.iloc[:,0])
print ('Done')


# ## First Winner

# In[11]:


# shuffle the data set


np.random.shuffle(random_df)
for i in random_df[0:10]:
    print (i)


# In[12]:




# pick the first winner
first_winner = random_df[-1]
#print ('And The First Winner is:', first_winner)

display(Markdown('# **And The First Winner is:** ' + str(first_winner)))


# ### Validate number of records in file

# In[13]:


# count of records for the winner

print(len([*filter(lambda i : i == first_winner, random_df )]))
print('money spent: ', len([*filter(lambda i : i == first_winner, random_df )])*100   )


# In[14]:


for i in [*filter(lambda i : i == first_winner,random_df )]:
    print (i)


# ## End of Draw

# In[ ]:


# remove all records for the first winner

clean_1 = [*filterfalse (lambda i : i == first_winner,random_df )]


# In[ ]:


# check the data set if all records have been removed


random_df = clean_1
len(random_df)


# ## Second Winner

# In[ ]:


# shuffle the data set


np.random.shuffle(random_df)

# pick the Second winner
second_winner = random_df[-1]
display(Markdown('### **And The Second Winner is:** ' + str(second_winner)))
    


# In[ ]:


# repeat steps

clean_2 = [*filterfalse (lambda i : i == second_winner,random_df )]

# check the data set if all records have been removed

random_df = clean_2
len(random_df)


# ## Third Winner

# In[ ]:


# shuffle the data set


np.random.shuffle(random_df)

# pick the Third winner
third_winner = random_df[-1]
display(Markdown('### **And The Third Winner is:** ' + str(third_winner)))
    


# In[ ]:


# repeat steps

clean_3 = [*filterfalse (lambda i : i == third_winner,random_df )]

# check the data set if all records have been removed

random_df = clean_3
len(random_df)


# ## Fourth Winner

# In[ ]:


# shuffle the data set


np.random.shuffle(random_df)

# pick the Fourth winner
fourth_winner = random_df[-1]
display(Markdown('### **And The Fourth Winner is:** ' + str(fourth_winner)))
    


# In[ ]:


# repeat steps

clean_4 = [*filterfalse (lambda i : i == fourth_winner,random_df )]

# check the data set if all records have been removed

random_df = clean_4
len(random_df)


# ## Fifth Winner

# In[ ]:


# shuffle the data set


np.random.shuffle(random_df)

# pick the Fifth winner
fifth_winner = random_df[-1]
display(Markdown('### **And The Fifth Winner is:** ' + str(fifth_winner)))
    


# In[ ]:


# repeat steps

clean_5 = [*filterfalse (lambda i : i == fifth_winner,random_df )]

# check the data set if all records have been removed

random_df = clean_5
len(random_df)


# In[ ]:


print ('And finally here are the list of winners:')
print ('The First winner is: {0},        The Second winner is: {1},         The Third winner is: {2},        The Fourth winner is: {3},         The Fifth winner is: {4}'.format(first_winner, second_winner, third_winner, fourth_winner, fifth_winner))


# In[ ]:




