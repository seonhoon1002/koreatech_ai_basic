import numpy as np 
import matplotlib.pyplot as plt

x =np.linspace(-3,3,1001)

fig= plt.figure()

basic_fx=np.log2(0.5*x)
fx_1= np.log2(3*x)
fx_2= np.log2(100* x)
fx_3= np.log2(-x)

axes= fig.subplots(nrows=2, ncols=1)

axes[0,0].plot(x, basic_fx,label='$y=log_2{0.5x}$',color='k')
axes[0,0].plot(x, fx_1,label='$y=log_2{3x}$',color='r')
axes[0,0].plot(x, fx_2,label='$y=log_2{100x}$',color='g')
axes[0,1].plot(x, fx_3,label='$y=log_2{(-x)}$',color='b')

lines=[]
labels=[]

for ax in fig.axes:
    axLine, axLabel= ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)

fig.legend(lines, labels, loc='upper right')
plt.show()