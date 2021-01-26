import numpy as np 
import matplotlib.pyplot as plt

x =np.linspace(-40,40,1001)
basic_fx=np.log2(0.5*x)
fx_1= np.log2(3*x)
fx_2= np.log2(100* x)
fx_3= np.log2(-x)


plt.plot(x, (-x)**2,label='$y=(-x)^2$',color='k')
plt.plot(x, -(x+3)**2,label='$-y=(x)^2$',color='b')
plt.plot(x, ((x+3))**2 +200,label='$(y-200)=((x+3))^2$',color='g')
plt.plot(x, -(-(x+3))**2 +200,label='$-(y-200)=(-(x+3))^2$',color='g')
plt.scatter(-3,200,s=20,c='red')
plt.legend()
plt.show()

