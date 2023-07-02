import pandas as pd

df=pd.read_csv('3-3read.csv',encoding='utf-8',sep=",")

a=df.groupby('居住縣市')['居住縣市'].count()

print(a.sort_values(ascending=False))

b=df.groupby('感染國家')['感染國家'].count()

print(b.sort_values(ascending=False).head())

c=df[df['居住縣市']=='台北市']

print(c.groupby('居住鄉鎮')['居住鄉鎮'].count())

print('發病日:',c['發病日'].max())

