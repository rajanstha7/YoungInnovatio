#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('data.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df=df[df.sale != 0]


# In[6]:


df.head(20)


# In[7]:


df.shape


# In[8]:


df.info()


# In[9]:


# Splitting year column into range
def Impute_year(cols):
    if cols in [2000,2001,2002,2003,2004]:
        return "2000-2004"

    elif cols in [2005,2006,2007,2008,2009]:
        return "2005-2009"

    elif cols in [2010,2011,2012,2013,2014]:
        return "2010-2014"

   
    
df['Year'] = df["year"].apply(Impute_year)


# In[10]:


df.head()


# In[11]:


df.drop("year", axis = 1, inplace = True)


# In[12]:


df.head()


# In[13]:


df1=df
df1


# In[14]:


df.groupby(["petroleum_product", "Year"], as_index=False)["sale"].count()


# In[15]:


x=df.groupby(["petroleum_product", "Year"], as_index=False)["sale"].max()
x


# In[16]:


y=df.groupby(["petroleum_product", "Year"], as_index=False)["sale"].min()
y


# In[17]:


z=df.groupby(["petroleum_product", "Year"], as_index=False)["sale"].mean()
z


# In[18]:


x['sale']


# In[19]:


y['sale']


# In[20]:


z['sale']


# In[21]:


df['Product']=x['petroleum_product']


# In[22]:


df['Year']=x['Year']


# In[23]:


df['Max']=x['sale']


# In[24]:


df['Min']=y['sale']


# In[25]:


df['Avg']=z['sale']


# In[27]:


df.drop("sale", axis = 1, inplace = True)


# In[28]:


df.drop("petroleum_product", axis = 1, inplace = True)


# In[29]:


df


# In[30]:


df.groupby('Product')


# In[37]:


x['Year']


# In[38]:


x['petroleum_product']


# In[46]:


# Creating an empty Dataframe with column names only
df2 = pd.DataFrame(columns=['Product', 'Year', 'Min','Max','Avg'])
print("Empty Dataframe ", df2, sep='\n')


# In[47]:


df2['Product']=x['petroleum_product']


# In[49]:


df2['Year']=x['Year']


# In[51]:


df2['Min']=y['sale']


# In[53]:


df2['Max']=x['sale']


# In[54]:


df2['Avg']=z['sale']


# In[55]:


df2


# In[56]:

df2.head(20)


df2.to_csv('reportgenerator.csv')

