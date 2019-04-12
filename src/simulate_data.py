"""
This Script is to simulate the data
"""


import numpy as np
import scipy.stats as stt
import pandas as pd

np.random.seed(12345)
a = np.random.randint(30,60)
b = 100 - a

dct = {"cat":[0]*a+[1]*b}


# both are nomal and the no differenf
x = np.random.normal(scale=2,size=a)
y = np.random.normal(loc=0.05, scale=2,size=b)
dct["norm_norm_not_sig"] = list(x)+list(y)

# both are nomal and the differenf
x = np.random.normal(scale=2,size=a)
y = np.random.normal(loc=2, scale=2,size=b)
dct["norm_norm_sig"] = list(x)+list(y)

# one is nomal and they are the same
x = np.random.normal(scale=2,size=a)
y = np.random.random(size=b)

dct["norm_no_norm_not_sig"] = list(x)+list(y)



# one is nomal and they are not same
x = np.random.normal(loc=2,scale=2,size=a)
y = np.random.random(size=b)
dct["norm_no_norm_sig"] = list(x)+list(y)


# not nomal and they are but sam
x = np.random.random(size=a) + 0.05
y = np.random.random(size=b)
dct["no_norm_no_norm_not_sig"] = list(x)+list(y)



# not nomal and they are not same
x = np.random.random(size=a) + 2
y = np.random.random(size=b)
dct["no_norm_no_norm_sig"] = list(x)+list(y)
dct = pd.DataFrame(dct)
dct = dct.sample(100)
dct.to_csv("../demo_data/demo.csv", index=False)

