import numpy as np 
import matplotlib.pyplot as plt

x =np.linspace(-10,10,1001)
basic_fx=np.log2(0.5*x)
fx_1= np.log2(3*x)
fx_2= np.log2(100* x)
fx_3= np.log2(-x)


plt.plot(x, (x)**2,label='$y=x^2$',color='k')
plt.plot(x, (x+3)**2,label='$y=(x+3)^2$',color='r')
plt.plot(x, (x+3)**2 -4,label='$y+4=(x+3)^2$',color='g')
plt.plot(x, (x+3)**2 +4,label='$y-4=(x+3)^2$',color='b')
plt.legend()
plt.show()

