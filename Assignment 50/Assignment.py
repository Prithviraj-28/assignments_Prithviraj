import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report , confusion_matrix ,precision_score,recall_score,f1_score


#-----------------------------------------------
#Step 1 : Load the Dataset
#-----------------------------------------------
df = pd.read_csv("breast_cancer.csv")
print("Shape of Dataset : ",df.shape)

print("First few records : ")
print(df.head())

#-----------------------------------------------
#Step 2 : Seperate features and labels
#-----------------------------------------------

X = df.drop("target",axis=1)
Y = df["target"]
print("X Shape : ",X.shape)
print("Y shape : ",Y.shape)

#-----------------------------------------------
#Step 3: Split Datasets For Traning and testing 
#-----------------------------------------------

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#-----------------------------------------------
#Step 4: Scale The Features
#-----------------------------------------------

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

#-----------------------------------------------
#Step 5.1 : Create the  base model 
#-----------------------------------------------

model = LogisticRegression(random_state=42)

#-----------------------------------------------
#Step 6 : Train the model 
#-----------------------------------------------

model = model.fit(x_train,y_train)

#-----------------------------------------------
#Step 7 : TEST the model 
#-----------------------------------------------

y_pred = model.predict(x_test)

#-----------------------------------------------
#Step 8 : EVALUATE the model 
#-----------------------------------------------

print("Accuraccy :",accuracy_score(y_test,y_pred)*100,"%")
print("COnfusion Matrix :")
print(confusion_matrix(y_test,y_pred))
print("Precision :",precision_score(y_test,y_pred)*100,"%")
print("Recall :",recall_score(y_test,y_pred)*100,"%")
print("F1-Score :",f1_score(y_test,y_pred)*100,"%")
