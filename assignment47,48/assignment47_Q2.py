import pandas as pd 
from sklearn.linear_model import LinearRegression
data = {
    "Study hours" : [1,2,3,4,5],
    "Sleep hours" : [7,6,7,6,8],
    "Marks" : [50,55,60,65,70]
    }
df = pd.DataFrame(data)

X = df[["Study hours","Sleep hours"]]
Y = df[["Marks"]]

model = LinearRegression()
model.fit(X,Y)

print("Coefficient 1 :", model.coef_[0][0])
print("Coefficient 2 :", model.coef_[0][1])

print("Intercept:", model.intercept_)

