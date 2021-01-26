import numpy as np 
import matplotlib.pyplot as plt

x =np.linspace(-10,10,1001)
fx =x *x
x_axis= x *0
y =np.linspace(-10,10,1001)
y_axis= y *0

# #0
# m_fx= (x)**2
# plt.plot(x, x_axis,'b')
# plt.plot(y_axis,y,'b')
# plt.plot(x, m_fx)
# plt.show()

# # 1
# m_fx= (x+3)**2
# plt.plot(x, x_axis,'b')
# plt.plot(y_axis,y,'b')
# plt.plot(x, m_fx)
# plt.show()

# #2
# m_fx= (x+3)**2 -4
# plt.plot(x, x_axis,'b')
# plt.plot(y_axis,y,'b')
# plt.plot(x, m_fx)
# plt.show()

# #3
# m_fx= (x+3)**2 +4
# plt.plot(x, x_axis,'b')
# plt.plot(y_axis,y,'b')
# plt.plot(x, m_fx)
# plt.show()

# #4
# m_fx= (-x)**2
# plt.plot(x, x_axis,'b')
# plt.plot(y_axis,y,'b')
# plt.plot(x, m_fx)
# plt.show()

# #5
# m_fx= -(x)**2
# plt.plot(x, x_axis,'b')
# plt.plot(y_axis,y,'b')
# plt.plot(x, m_fx)
# plt.show()

# #6
# m_fx= -(-(x+3))**2-4
# plt.plot(x, x_axis,'b')
# plt.plot(y_axis,y,'b')
# plt.plot(x, m_fx)
# plt.show()

#6

plt.plot(x, x_axis,'b')
plt.plot(y_axis,y,'b')

for a in range(100):
    m_fx= 1/(a+1)*x
    plt.plot(x, m_fx,'g')
plt.show()