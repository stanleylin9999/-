import matplotlib.pyplot as plt

import pandas as pd

url = 'https://data.cip.gov.tw/API/v1/dump/datastore/A53000000A-110025-003'

df=pd.read_csv(url)

df['場館']=df['場館'].str.replace('台灣原住民','花蓮縣')

df['縣市']=df['場館'].str[:3]

df=df.iloc[:,2:]

for i in range(2,14):
    df.iloc[:,i]=pd.to_numeric(df.iloc[:,i], errors="coerce")
    
df1= df.groupby('年度').sum()

df1= df1.sum(axis=1)

df2=df.sum(axis=0)

df2=df2[2:14]

df3=df.groupby('縣市').sum().sum(axis=1)

list1=['臺北市','新北市','桃園市','臺中市','臺南市','高雄市']

cap=df3[list1].sum()

notcap=df3.sum()-cap

df4=[cap,notcap]

title=['六都','非六都']

plt.figure(figsize=(15,10),dpi=300)

plt.rcParams['font.sans-serif']='Microsoft JhengHei'

plt.subplot(2,2,1) 

plt.xticks([107,108,109,110])

plt.title('年度總參觀人次',fontsize=16)

plt.xlabel('民國年度')

plt.ylabel('觀光人次')

for i in df1.index:
    plt.text(i,df1[i]-20000,int(df1[i]),ha='center',va='top',color='w')
    
plt.bar(list(df1.index),list(df1))

plt.subplot(2,2,2) 

plt.title('各月份總參觀人次',fontsize=16)

plt.grid()

plt.ylim(50000,450000)

for i in df2.index:
    plt.text(i,df2[i],int(df2[i]),ha='center',va='bottom')
    
plt.plot(df2,color='orange')

plt.subplot(2,2,3) 

plt.title('各縣市總參觀人次',fontsize=16)

plt.xticks(fontsize=6)

for i in df3.index:
    if df3[i]<200000:
        plt.text(i,df3[i]+10000,int(df3[i]),ha='center',va='bottom',fontsize=12,rotation=90)
    else:
        plt.text(i,df3[i]-10000,int(df3[i]),ha='center',va='top',fontsize=12,rotation=90,color='w')
        
plt.bar(list(df3.index),list(df3),color='green')

plt.subplot(2,2,4) 

plt.title('六都與非六都總參觀人數比',fontsize=16)

plt.pie(df4,labels=title,autopct='%.1f%%')

plt.savefig('作業4')
