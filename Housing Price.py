#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df = pd.read_csv('kc_house_data.csv')

df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.corr()


# In[6]:


df.drop(['id'],axis=1,inplace=True)

df.head()


# In[85]:


#df_corr=df.corr()[:]
#features = df.corr[abs(df_corr)>0.5].sort_values(ascending=False)
plt.figure(figsize=(14,8))

sns.heatmap(df.corr,annot=True,cmap='ocean')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:


df.duplicated().sum()


# In[22]:


sns.boxplot(data=df,x='bedrooms',y='price')


# In[23]:


sns.boxplot(data=df,x='bathrooms',y='price')


# In[55]:


sns.boxplot(data=df,y='price')


# In[ ]:





# In[ ]:





# In[ ]:





# In[78]:


sns.distplot(df['price'],bins=20,color='b')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:


df.groupby('waterfront')['price'].mean().plot(kind='bar')
plt.show()


# In[46]:


df['bedrooms'].value_counts(ascending=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




