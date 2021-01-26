import numpy as np 
import matplotlib.pyplot as plt

x =np.linspace(-3,3,1001)

fig= plt.figure()

basic_fx= 3**(x)
fx_1= 10 **(x)
fx_2= 3**(x-10)
fx_3= (0.5) **x

axes= fig.subplots(nrows=2, ncols=2)

axes[0,0].plot(x, basic_fx,label='$y=3^{x}$',color='k')
axes[0,1].plot(x, fx_1,label='$y=10^{x}$',color='r')
axes[1,0].plot(x, fx_2,label='$y=3^{x-10}$',color='g')
axes[1,1].plot(x, fx_3,label='$y=0.5^{x}$',color='b')

lines=[]
labels=[]

for ax in fig.axes:
    axLine, axLabel= ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)

fig.legend(lines, labels, loc='upper right')
plt.show()