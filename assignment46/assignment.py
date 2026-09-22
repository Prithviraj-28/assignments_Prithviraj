import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score


def rajregression(datapath):
    border = "**"*60


    #################################################################################################
    #Step 1 : Load the data
    #################################################################################################
    print(border)
    print("Step 1 : Load the data")
    print(border)

    df = pd.read_csv(datapath)

    print("Shape of Model : ",df.shape)
    print(df.head())
    

    #################################################################################################
        #Step 2 : Exploratory Data Analysis
    #################################################################################################
    print(border)
    print("Step 2 : Exploratory Data Analysis")
    print(border)

    #Remove Unwanted Columns 
    print("Remove Unwanted Columns")
    if "Unnamed: 0" in df.columns :
        df = df.drop(columns="Unnamed: 0")
        print(df.head())
    print(border)

    #Find Missing Values 
    print("Total Missing  Files :")
    print(df.isnull().sum())

    #Statistical Summary
    print(border)
    print("Statistical Summary : ")
    print(df.describe())

    #Corelation
    print(border)
    print("Corelation : ")
    print(df.corr())

    #################################################################################################
        #Step 3 : Split Independent And Dependent Variables
    #################################################################################################
    print(border)
    print("Step 3 : Split Independent And Dependent Variables ")
    print(border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent Variables :")
    print(X.head())

    print(border)

    print("Dependent Variables : ")
    print(Y.head())

    #################################################################################################
        #Step 4 : Split The Dataset
    #################################################################################################
    print(border)
    print("Step 4 : Split The Dataset ")
    print(border)

    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Traning Data : ",x_train.shape)
    print("Testing Data : ",x_test.shape)

    #################################################################################################
        #Step 5 : Create And Train Model 
    #################################################################################################
    print(border)
    print("Step 5 : Create And Train Model ")
    print(border)

    model = LinearRegression()
    model = model.fit(x_train,y_train)
    print("Model Gets Trained Sucessfully")

    #################################################################################################
        #Step 6 :  Test The  Model 
    #################################################################################################
    print(border)
    print("Step 6 :  Test The  Model")
    print(border)

    y_pred = model.predict(x_test)

    print("Expected Answers : ")
    print(y_test[::5])

    print("Predicted Answers : ")
    print(y_pred[::5])

    #################################################################################################
        #Step 7 :  Evaluate The  Model 
    #################################################################################################
    print(border)
    print("Step 7 :  Evaluate The  Model")
    print(border)

    MSE = mean_squared_error(y_test,y_pred)
    RMSE = np.sqrt(MSE)

    R2 = r2_score(y_test,y_pred)

    print("MSE :",MSE)
    print("RMSE :",RMSE)
    print("R2 :",R2)

    #################################################################################################
        #Step 8 :  Display Coefficient
    #################################################################################################
    print(border)
    print("Step 8 :  Display Coefficient")
    print(border)

    print("TV Coefficient : ",model.coef_[0])
    print("Radio Coefficient : ",model.coef_[1])
    print("Newspaper Coefficient : ",model.coef_[2])

    print("Intercept : ",model.intercept_)



def main():
    rajregression("Advertising.csv")
    
if __name__ == "__main__":
    main()
