
# coding: utf-8

# In[15]:


import pandas as pd


# In[33]:


#the data has count and amount as feature for every month expenditure in each categoty for each user
#ex acc_id	  CNT_TRANSFER_M1	 AMT_TRANSFER_M1  CNT_TRANSFER_M2  AMT_TRANSFER_M2  CNT_TRANSFER_M3
#      xyz	        0.0	           0	              0.0	           0	            0.0	
data=pd.read_csv("xns_16_wo_fin_categoryData.csv")


# In[35]:


import numpy as np
col=list(data.columns)
x=1
y=1
listsum=np.array([0 for i in range(data.shape[0])])
columns=[]
def sumoflist(listofamount):
    global x,listsum
    tmp=[listsum,listofamount]
    listsum=np.sum(tmp,axis=0)
    x+=1
for i in range(1,len(col),2):
    if x<4:
        sumoflist(list(data[col[i]]))
    else:
        y+=1
        columns.append(listsum)
        listsum=np.array([0 for i in range(data.shape[0])])
        x=1
        sumoflist(list(data[col[i]]))
columns.append(listsum)
print(np.array(columns).shape)
x=1
y=1
listsum=np.array([0 for i in range(data.shape[0])])
for i in range(2,len(col)+1,2):
    if x<4:
        sumoflist(list(data[col[i]]))
    else:
        y+=1
        columns.append(listsum)
        listsum=np.array([0 for i in range(data.shape[0])])
        x=1
        sumoflist(list(data[col[i]]))
columns.append(listsum)


# In[36]:


np.array(columns).shape


# In[37]:


data.shape


# In[38]:


columns=np.array(columns).transpose()


# In[39]:


columns.shape


# In[40]:


# symbols   = ['TRANSFER',  'WITHDRAWAL', 'INVESTMENT EXPENSE', 'BANK CHARGES', 'INTEREST', 'UTILITIES', 'CREDIT CARD', 'INVESTMENT INCOME', 'SHOPPING', 'TRAVEL', 'REVERSAL', 'DIVIDEND', 'SALARY', 'DEPOSIT', 'DINING', 'TAX', 'HOUSING', 'INSURANCE', 'AUTO', 'PERSONAL LOAN', 'CASH WITHDRAWAL', 'MEDICAL', 'INTEREST CHARGES', 'ENTERTAINMENT', 'BUSINESS EXPENSE', 'OTHER INCOME', 'POLICY MATURITY', 'RENT RECEIVED', 'EDUCATION', 'CASH BACK', 'HOUSE RENT', 'LOAN', 'PERSONAL CARE', 'PENSION', 'FAMILY EXPENSES', 'MISC', 'CASH DEPOSIT', 'AIR FARE', 'SERVICES', 'WAGES', 'CONSULTING', 'GIFTS GIVEN', 'VACATION', 'CHARITY', 'TAX REFUND', 'SHARE PURCHASE', 'FOREIGN CURRENCY', 'MUTUAL FUND', 'HOME REPAIR', 'SUBSCRIPTIONS', 'TRADE', 'BUSINESS INCOME', 'MUTUAL FUNDS', 'MONEY GIVEN', 'GIFT RECEIVED', 'BUSINESS TRAVEL', 'OFFICIAL EXPENSE', 'VSM', 'REIMBURSEMENT', 'MY SALARY', 'INVESTMENT', 'LEGAL/PROF FEES', 'SHARE SELL', 'BUSINESS SALARY', 'PARENTAL CARE', 'RENT DEPOSIT', 'WEBSITE CHARGES', 'DEBT REPAYMENT', 'TRANSFER-IN', 'ASSET SALE', 'CHILD CARE', 'INVESTMENTS', 'TRANSFER-OUT', 'SHARES', 'DOMESTIC SALE', 'TRANSFER TO', 'SELF TRANSFER', 'INCOME FROM', 'TRANSFER FROM', 'GROCERIES', 'CLUB MEMBERSHIP', 'FAMILY FUNCTION', 'RECONCILED TRANSFERS', 'FIXED DEPOSIT', 'D-EXPENSES', 'MF INVESTMENT', 'BUSINESS ', 'MF BROKERAGE', 'BONUS', 'CONTRA']
symbols=['TRANSFER', '<SPECIFY>', 'WITHDRAWAL', 'INVESTMENT EXPENSE', 'BANK CHARGES', 'INTEREST', 'UTILITIES', 'CREDIT CARD', 'INVESTMENT INCOME', 'SHOPPING', 'TRAVEL', 'REVERSAL', 'DIVIDEND', 'SALARY', 'DEPOSIT', 'DINING', 'TAX', 'HOUSING', 'INSURANCE', 'AUTO', 'PERSONAL LOAN', 'CASH WITHDRAWAL', 'MEDICAL', 'INTEREST CHARGES', 'ENTERTAINMENT', 'BUSINESS EXPENSE', 'OTHER INCOME', 'POLICY MATURITY', 'RENT RECEIVED', 'EDUCATION', 'CASH BACK', 'HOUSE RENT', 'LOAN', 'PERSONAL CARE', 'PENSION', 'FAMILY EXPENSES', 'MISC', 'CASH DEPOSIT', 'AIR FARE', 'SERVICES', 'WAGES', 'CONSULTING', 'GIFTS GIVEN', 'VACATION', 'CHARITY', 'TAX REFUND', 'SHARE PURCHASE', 'FOREIGN CURRENCY', 'MUTUAL FUND', 'HOME REPAIR', 'SUBSCRIPTIONS', 'TRADE', 'BUSINESS INCOME', 'MUTUAL FUNDS', 'MONEY GIVEN', 'GIFT RECEIVED', 'BUSINESS TRAVEL', 'OFFICIAL EXPENSE', 'VSM', 'REIMBURSEMENT', 'MY SALARY', 'INVESTMENT', 'LEGAL/PROF FEES', 'SHARE SELL', 'BUSINESS SALARY', 'PARENTAL CARE', 'RENT DEPOSIT', 'WEBSITE CHARGES', 'DEBT REPAYMENT', 'TRANSFER-IN', 'ASSET SALE', 'CHILD CARE', 'INVESTMENTS', 'TRANSFER-OUT', 'SHARES', 'DOMESTIC SALE', 'TRANSFER TO', 'SELF TRANSFER', 'INCOME FROM', 'TRANSFER FROM', 'GROCERIES', 'CLUB MEMBERSHIP', 'FAMILY FUNCTION', 'RECONCILED TRANSFERS', 'FIXED DEPOSIT', 'D-EXPENSES', 'MF INVESTMENT', 'BUSINESS ', 'MF BROKERAGE', 'BONUS', 'CONTRA', 'REIMBURSIBLE TAX', 'MF PURCHASE', '3 EXPENSIS', 'VENDOR PAYMENT', 'MONEY RECEIVED', 'BROKERAGE', 'VINAY', 'REFUND', 'HOUSEHOLD EXPENSES', 'PROFESSIONAL INCOME', '1 VENDORS', 'RETAILER PAYMENT', 'AAZ NO', 'EQ ICICI', 'HOUSE CONSTRUCTION', 'HUSAMSONS SALE', 'JAAZE CREATIONS', 'COMMISSION -', 'REIMBURSEMENTS', 'EXPENSE', 'FD INTEREST', 'FLEXI DEPOSIT', 'ACCOUNT TO', '_NKS AGRO', 'JOULES', 'HOUSEHOLD', 'FIRST STEP', 'EXPENSE REIMBURSEMENT', 'RET-INCOME (RAMANA)', 'HOUSEHOLD EXPENCES', 'CASH EXPENSES', 'MF SIP', 'HDFC-0150', 'RECURRING DEPOSIT', 'COMMISSION', 'MY INCOME', 'SIP INVESTMENT', 'LOAN TRANSFERS', 'FIXED DEPOSITS', 'LAB', 'INVESTMENT TRANSFERS', 'SPLIT', 'TRANSFER -', 'EMI FOR', 'DIGI PAYMENT', 'CHAWLAS2', 'BROK REVERSAL', 'KRUTI -', 'MY CASH', 'RAILDR', 'TRANSFER WITHIN', '1 WSEA', 'HOME EXPENSES', 'HOME LOAN', 'BANGALORE EXPENSES', 'ACCOUNT', 'INTEREST--SR', 'SALARY TO', 'CHITRA PURCHASES', 'SWIPE TRANSFER', 'KULKARNI', 'BUSINESS PURCHASES', 'INTER FAMILY', 'MF-INVESTMENT', 'EXPENSES-123', 'LOANS EMI', 'PAYUMONEY', 'NYKA ADVISORY', 'TAX FREE', 'FEES', 'SNS', 'FEES RECIEVED', 'TRADING ACCOUNT', 'PSVK', '_CAFE', 'MF INV', "SHANKAR'S NEST", 'MF REDEMPTION', 'CAFE SALES', 'LOANS', 'INTER BANK', 'RD ACCOUNT', 'A CUSTOM', 'MUTUL FUND', 'PERSONAL EXPENSES', 'MARGIN', 'A TRANSFER', 'FEDEX EXPRESS', '8.G&A-EXPENSES', 'CORP BANK', 'RIDA BUSINESS', 'LOAN REPAYMENT', 'MOD B/F', 'ANNUITY', 'SALARIES', 'WINSOME', 'HOUSHOLD', 'SIP TRANSACTION', 'PAYMENT FROM', 'SIP MF', 'MF BUY', 'INCOME-123', 'BANK INTEREST', 'DOT SOLUTIONS', 'MF INVEST', 'INVESTMENT TRANSFER', 'PAYTM', 'LOAN GIVEN']
headers=["user_id"]
y=1
for i in symbols:
    headers.append("CNT_"+i+"_Q1")
    headers.append("CNT_"+i+"_Q2")
    headers.append("CNT_"+i+"_Q3")
    headers.append("CNT_"+i+"_Q4")
for i in symbols:
    headers.append("AMT_"+i+"_Q1")
    headers.append("AMT_"+i+"_Q2")
    headers.append("AMT_"+i+"_Q3")
    headers.append("AMT_"+i+"_Q4")


# In[41]:


headers


# In[42]:


acc_id=list(data["acc_id"])


# In[43]:


df=pd.DataFrame(columns,columns=headers[1:])


# In[44]:


df.insert(0,column="ACC_ID",value=acc_id)


# In[45]:


df.to_csv('final_mf_wo_data.csv')


# In[ ]:




