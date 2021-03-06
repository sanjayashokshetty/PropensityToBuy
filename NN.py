'''
neural network model
'''

import pandas as pd
data=pd.read_csv('mf_fin.csv')

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

#upsampling the data
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

#Feature selection using mutual information
test = SelectKBest(score_func=mutual_info_classif,k=50)
fit = test.fit(X_train.as_matrix(),y_train.as_matrix())
p_values=test.pvalues_
scores=test.scores_
X_train = fit.transform(X_train.as_matrix())
X_test=fit.transform(X_test.as_matrix())

#get to know the selected featues
for i,j in zip(columns,fit.get_support()):
    if j==True:
        print(i)

#train the model and get test
mlp,X_test,y_test,p_values,scores,pred=model(X_train,X_test,y_train.as_matrix(),y_test.as_matrix())

#save model
from sklearn.externals import joblib
lmodel=joblib.load('model4_30.pkl')
