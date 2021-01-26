import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

def conv_feet2peng(feet):
    return feet/35.5872


df =pd.read_csv('../train.csv')

y= df['price']
x= df['sqft_lot']
# x= conv_feet2peng(x)
y=y[x<100000]
x=x[x<100000]
plt.xlabel('$feet^2(\\times 10^6)$',fontsize=15)
plt.ylabel('$HousePrice(\\times 10^6 \\$)$',fontsize=15)
plt.scatter(x,y,c='red', s=1)
plt.show()


