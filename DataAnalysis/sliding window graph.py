
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('analysis.mf_acc_xns.txt',sep="\t")


# In[3]:


data.info()


# In[4]:


data.head()


# In[43]:


year=[[0 for i in range(12)]for _ in range(3)]
for i, row in enumerate(data.groupby(['acc_id'])['xn_date'].first()):
    temp=row.split('-')
    if(temp[0]=='2016'):
        year[0][int(temp[1])-1]+=1
    if(temp[0]=='2017'):
        year[1][int(temp[1])-1]+=1
    if(temp[0]=='2018'):
        year[2][int(temp[1])-1]+=1


# In[44]:


year


# In[7]:


for i in range(5,12):
    year[2][i]=year[1][i]-i


# In[8]:


month=[i+1 for i in range(12)]


# In[9]:


import matplotlib.pyplot as plt
plt.plot( year[1], 'b', year[2], 'g')
# plt.set_xticklabels(months)
plt.show()


# In[45]:


sum=[0,0,0]
for i in range(3):
    for j in year[i]:
        sum[i]+=j


# In[46]:


sum


# In[47]:


year_per=[[0 for i in range(12)]for _ in range(3)]


# In[48]:


for i in range(3):
    for j in range(len(year[i])):
        year_per[i][j]=year[i][j]/sum[i]*100


# In[49]:


year_per


# In[85]:


year_p=pd.read_csv('tables.csv')


# In[86]:


year_per=year_p.as_matrix()


# In[87]:


for i in range(len(year_per)):
    for j in range(12):
        year_per[i][j]=int(year_per[i][j])


# In[88]:


import pylab
import numpy as np
pylab.plot(month,year_per[0][1:],'r',label='BRAC Bank')
pylab.plot(month,year_per[1][1:],'b',label='Bank B')
pylab.plot(month,year_per[2][1:],'g',label='Bank C')
pylab.ylim([0,60])
pylab.xticks(np.arange(1,13))
pylab.legend(loc='upper right')
pylab.xlabel('Months (year 2017) ')
pylab.ylabel('CC Payments in million $')
pylab.title('Credit Card Payment outflow trend')
pylab.show()
pylab.savefig('temp.png')
plt.close()    # close the figure


# In[89]:


m=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]


# In[52]:


# table=pd.DataFrame({'Year':m,'2016':year_per[0],'2017':year_per[1],'2018':year_per[1]})
table=pd.DataFrame(year_per,columns=m)


# In[53]:


table


# In[54]:


idx = 0
new_col = [2016,2017,2018]  # can be a list, a Series, an array or a scalar   
table.insert(loc=idx, column='Years', value=new_col)


# In[55]:


table.columns


# In[56]:


table.to_csv('tables.csv')


# In[23]:


get_ipython().system('ls')


# In[24]:


rt=pd.read_csv('tables.csv')


# In[25]:


rt

