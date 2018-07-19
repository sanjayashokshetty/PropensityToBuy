
# coding: utf-8

# In[16]:


import pandas as pd


# In[17]:


data=pd.read_csv('mf_fin.csv')


# In[18]:


data.shape


# In[24]:


from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest,chi2,mutual_info_classif
from sklearn.decomposition import PCA
from sklearn.utils import resample
def model(X_train,X_test,y_train,y_test):
    mlp = MLPClassifier(hidden_layer_sizes=(500,500,200,100),max_iter=500,activation='logistic',verbose=True,learning_rate='adaptive',random_state=123)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    mlp.fit(X_train,y_train)
    pred=mlp.predict(X_test)
    count_0,count_1=0,0
    for i in y_train:
        if i==0:
            count_0+=1
        if i==1:
            count_1+=1    
    print("train 0: ",count_0," train 1: ",count_1)
    print(confusion_matrix(y_test,pred))
    print(classification_report(y_test,pred))
    print(accuracy_score(pred,y_test))
    print(mlp.predict_proba(X_test),y_test)
    return mlp,X_test,y_test,p_values,scores,pred


# In[25]:


df_majority = data[data.res==0]
df_minority = data[data.res==1]
print(df_majority.shape)
print(df_minority.shape)
df_minority_train=df_minority[:81]
df_minority_ups_train = resample(df_minority_train, 
                                replace=True,     # sample with replacement
                                 n_samples=2000,    # to match majority class
                                 random_state=123)
df_train=pd.concat([df_majority[:4648],df_minority_ups_train])
df_test=pd.concat([df_majority[4648:],df_minority[81:]])
print(df_train.shape)
print(df_test.shape)

X_train=df_train.drop(['res','ACC_ID'],axis=1)
user_id_train=df_train['ACC_ID']
X_test=df_test.drop(['res','ACC_ID'],axis=1)
user_id_test=df_test['ACC_ID']
y_train=df_train['res']
y_test=df_test['res']


# In[26]:


test = SelectKBest(score_func=mutual_info_classif,k=50)
fit = test.fit(X_train.as_matrix(),y_train.as_matrix())
p_values=test.pvalues_
scores=test.scores_
X_train = fit.transform(X_train.as_matrix())
X_test=fit.transform(X_test.as_matrix())


# In[27]:


mlp,X_test,y_test,p_values,scores,pred=model(X_train,X_test,y_train.as_matrix(),y_test.as_matrix())


# In[11]:


from sklearn.externals import joblib
lmodel=joblib.load('model4_30.pkl')


# In[271]:


print(confusion_matrix(y_test,lmodel.predict(X_test)))


# In[272]:


joblib.dump(lmodel,'model4_30.pkl')


# In[28]:


class_0=[]
class_1=[]
c=0
for i in lmodel.predict_proba(X_test):
    class_0.append(i[0])
    class_1.append(i[1])


# In[33]:


pd.DataFrame({'user_id':user_id_test,'Prob_class0':class_0,'Prob_class1':class_1,'actual':y_test,'pred':lmodel.predict(X_test)}).to_csv("analysis.csv")

