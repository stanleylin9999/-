import numpy as np

import matplotlib.pyplot as plt

x=np.array(["Jun","Jul","Aug","Sep"])

y=np.array([20,30,40,10])

plt.subplot(1,2,1)

plt.xlabel("month")

plt.ylabel("size")

plt.bar(x,y)

plt.subplot(1,2,2)

lbl=["Jun","Jul","Aug","Sep"]

color=["yellowgreen","gold","skyblue","lightcoral"]

explode=[0,0,0.1,0]

plt.pie(y,explode=explode,labels=lbl,autopct="%.1f%%",colors=color)

plt.savefig('chart.png')

