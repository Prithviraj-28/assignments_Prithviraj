from sklearn.preprocessing import StandardScaler
import numpy as np 

x = np.array([
    [25,20000],
    [30,40000],
    [35,80000]
]
)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(x)
print("Scaled Data is : ", scaled_data)
