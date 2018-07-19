
# coding: utf-8

# In[1]:


#the code to get start date of product account for users who own the perticular product
import pandas as pd
data=pd.read_csv('analysis.mf_acc_xns.txt',sep='\t')


# In[2]:


data.shape


# In[35]:


dictionary={}
for i in range(data.shape[0]):
    a_id=str(data['acc_id'][i])
    year=int(data['xn_date'][i].split('-')[0])
    if a_id in dictionary.keys():
        if year<dictionary[a_id]:
            dictionary[a_id]=year
    elif a_id not in dictionary.keys():
        dictionary[a_id]=year


# In[24]:


int(data['xn_date'][0].split('-')[1])


# In[ ]:


dictionary={}
dictionary1={}
for i in range(data.shape[0]):
    a_id=str(data['acc_id'][i])
    year=int(data['xn_date'][i].split('-')[0])
    month = int(data['xn_date'][i].split('-')[1])
    if a_id in dictionary.keys():
        print('Found')
        if year<dictionary[a_id] :
            dictionary[a_id]=year
#             dictionary[a_id].append(data['xn_date'][i].split('-')[1])
            if month<dictionary1[a_id]:
                dictionary1[a_id]=month
            print(year)
            #dictionary[a_id].append(month)
    elif a_id not in dictionary.keys():
        print(" not found")
        print(year)
        dictionary[a_id]=year
        dictionary1[a_id]=month
        #dictionary[a_id].append(month)


# In[32]:


dictionary1


# In[36]:


count=0
for k,v in dictionary.items():
    if v==2018:
        count+=1


# In[37]:


count


# In[18]:


acc_id_18=[]
for k,v in dictionary.items():
    if v==1:
        acc_id_18.append(int(k))


# In[19]:


len(acc_id_18)


# In[40]:


get_ipython().system('ls')


# In[10]:


user_acc=pd.read_csv('acc.csv')


# In[7]:


user_id=[]
count=0
for k,v in dictionary.items():
    try:
        index=user_acc["acc_id"][data["acc_id"]==int(k)].index[0]
        user_id.append(user_acc['user_id'][index])
    except:
        count+=1


# In[9]:


print(user_id)


# In[39]:


import pickle
def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
save_obj(dictionary1,"month_dict")

