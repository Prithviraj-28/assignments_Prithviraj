import numpy as np 

X = [1,2,3,4,5]
Y = [3,4,2,4,5]

mean_X = np.mean(X)
mean_Y = np.mean(Y)

slope_M = np.sum((X - mean_X) * (Y - mean_Y)) / np.sum((X - mean_X) ** 2)

intercept_C = mean_Y - (slope_M * mean_X)

regression = slope_M * np.array(X) + intercept_C


predict = slope_M * 6 + intercept_C
print("Predicted value for X=6:", predict)
