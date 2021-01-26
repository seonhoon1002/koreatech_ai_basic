import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

def rough_func(x):
    return x

def mse(pred, target):
    pred= pred.to_numpy()
    target= target.to_numpy()

    return np.mean(np.sqrt((pred-target)**2))

def main():
    df =pd.read_csv('train.csv')
    price= df['price']
    sqft_lot=df['sqft_lot']
    pred_price= rough_func(sqft_lot)

    print("mse", mse(pred_price, price))

    plt.xlabel('$feet^2(\\times 10^6)$',fontsize=15)
    plt.ylabel('$HousePrice(\\times 10^6 \\$)$',fontsize=15)
    
    plt.scatter(sqft_lot,price,c='red', s=1)
    plt.scatter(sqft_lot,pred_price,c='green', s=1)
    plt.show()
if __name__ == "__main__":
    main()