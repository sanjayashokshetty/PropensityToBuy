
# coding: utf-8

# In[29]:


import pandas as pd


# In[30]:


get_ipython().system('ls')


# In[31]:


mt=pd.read_csv('master_table.csv')


# In[32]:


mt


# In[33]:


uid=[]
for i in range(mt.shape[0]):
    if mt["MF_cnt"][i]>0:
        uid.append(mt["user_id"][i])


# In[34]:


acc=pd.read_csv('acc.csv')


# In[35]:


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


# In[36]:


import pickle
dictionary=load_obj('month_dict')
dictionary_year=load_obj('dict')


# In[44]:


column=[0 for _ in range(acc.shape[0])]
column_year=[0 for _ in range(acc.shape[0])]


# In[45]:


acc


# In[47]:


for i in range(acc.shape[0]):
    if str(acc['acc_id'][i]) in dictionary.keys():
        column[i]=dictionary[str(acc['acc_id'][i])]
        column_year[i]=dictionary_year[str(acc['acc_id'][i])]


# In[48]:


column=pd.DataFrame({'start_month':column,'start_year':column_year})


# In[49]:


acc=acc.join(column)


# In[50]:


acc


# In[51]:


acc_new=acc[acc.start_year>0]


# In[52]:


acc_new


# In[53]:


acc_new.shape


# In[27]:


y7=0
y8=0
y6=0
c=0
for i in acc_new['start_year']:
    if i==2018:
        y8+=1
    if i==2017:
        y7+=1
    if i==2016:
        y6+=1
    c+=1


# In[28]:


print("2016 :",y6," 2017: ",y7," 2018 : ",y8)


# In[54]:


acc_new.to_csv('year.csv')

