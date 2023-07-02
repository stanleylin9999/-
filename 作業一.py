import numpy as np

seed=123

np1=np.random.RandomState(seed).randint(5,16,size=15)

print("隨機正整數 : ",end="")

print(np1)

np2=np1.reshape(3,5)

print("X矩陣內容 : ")

print(np2)

print("最大 : ",end="")

print(np1.max())

print("最小 : ",end="")

print(np1.min())

print("總和 : ",end="")

print(np1.sum())

list1=list()

list1.append(np2[0,0])

list1.append(np2[0,4])

list1.append(np2[2,0])

list1.append(np2[2,4])

np3=np.array(list1)

np4=np3.reshape(2,2)

print("四個角落元素 : ")

print(np4)