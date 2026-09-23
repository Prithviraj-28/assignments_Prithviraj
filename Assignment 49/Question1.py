import numpy as np

X = np.array([6,7,8,9,10,11,12])

print('Data set is : ',X)

mean = np.mean(X)
print("Mean of Dataset is : ",mean)

varience = np.var(X)
print("Varience of Dataset is : ",varience)

standard_dev = np.std(X)
print("standard deviation of X is ", standard_dev)
