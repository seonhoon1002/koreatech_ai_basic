import numpy as np 
import matplotlib.pyplot as plt

fig= plt.figure()
x =np.linspace(-5,5,1001)
basic_fx=np.log2(0.5*x)
fx_1= np.log2(3*x)
fx_2= np.log2(100* x)
fx_3= np.log2(-x)

axes= fig.subplots(nrows=2, ncols=2)

axes[0,0].plot(x, np.sqrt(x-1) + 3*x +1,label='$f+g= 3x+ \\sqrt{x-1}$',color='k')
axes[0,1].plot(x, np.sqrt(x-1) + 3*x -1,label='$f-g= 3x- \\sqrt{x-1}$',color='r')
axes[1,0].plot(x, np.sqrt(x-1) * (3*x +1),label='$fg= 3x(\\sqrt{x-1})$',color='g')
axes[1,1].plot(x, (3*x +1)/np.sqrt(x-1) ,label='$\\frac{f}{g}=\\frac{3x}{\\sqrt{x-1}}$',color='b')

lines=[]
labels=[]

for ax in fig.axes:
    axLine, axLabel= ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)

fig.legend(lines, labels)
plt.show()