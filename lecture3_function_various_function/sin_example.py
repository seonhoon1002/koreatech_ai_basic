import numpy as np 
import matplotlib.pyplot as plt

x =np.linspace(-3,3,1001)

fig= plt.figure()

basic_fx=np.sin(x)
fx_1= np.sin(10*x)
fx_2= np.sin(0.5* x)
fx_3= np.sin(x-0.5)

axes= fig.subplots(nrows=2, ncols=2)

axes[0,0].plot(x, basic_fx,label='$y=sin{x}$',color='k')
axes[0,1].plot(x, fx_1,label='$y=sin{10x}$',color='r')
axes[1,0].plot(x, fx_2,label='$y=sin{0.5x}$',color='g')
axes[1,1].plot(x, fx_3,label='$y=sin{x-0.5}$',color='b')

lines=[]
labels=[]

for ax in fig.axes:
    axLine, axLabel= ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)

fig.legend(lines, labels, loc='upper right')
plt.show()