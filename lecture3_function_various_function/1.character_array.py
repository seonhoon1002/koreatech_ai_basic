import numpy as np 
import matplotlib.pyplot as plt

x =np.linspace(-1,1,1001)
y =np.linspace(-1,1,1001)
y1 =np.linspace(-1,1,1001)

fig= plt.figure()

y[y<0.5] =0
y[y>0.5] =1
axes= fig.subplots(nrows=1, ncols=2)

axes[0].plot(x, y,label='if x<0.5, then 0 else 1',color='k')

y1[y1<0.3] =0
y1[y1>0.3]=1
axes[1].plot(x, y1,label='if x<0.3, then 0 else 1',color='g')

lines=[]
labels=[]

for ax in fig.axes:
    axLine, axLabel= ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)

fig.legend(lines, labels, loc='upper right')
plt.show()