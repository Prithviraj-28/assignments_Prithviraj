from sklearn.datasets import load_wine
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , confusion_matrix 
from sklearn.preprocessing import StandardScaler

def Rajclassifier(datapath):
    border = "-"*60


    ##################################################################
    #Step 1 : :Load the dataset from CSV file
    ##################################################################

    print(border)
    print(" Step 1 : :Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(datapath)

    print("Some entries form dataset : ")
    print(df.head())

    print(border)


##################################################################
    #Step 2 : : Clean the datasets
##################################################################

    print(border)
    print("Step 2 : : Clean the datasets")
    print(border)
    

    df.dropna(inplace=True)

    print("Total records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])


    ##################################################################
    #Step 3 : : Seperate Independent and Dependent Variables
    ##################################################################

    print(border)
    print("Step 3 : : Seperate Independent and Dependent Variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of Independent Variables or Features : ",X.shape)
    print("Shape of Dependent Variables or Labels : ",Y.shape)

    print(border)
    print("Input Columns : ",X.columns.to_list())
    print("Output Columns: Class")


    ##################################################################
    #Step 4 : : Split the dataset for traning and testing 
    ##################################################################
    print(border)
    print("Step 4 : : Split the dataset for traning and testing")
    print(border)

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 42,stratify=Y)

    print("Details of traning and testing Data : ")
    print("Shape of X_train : ",X_train)
    print("Shape of X_test : ",X_test)
    print("Shape of Y_train : ",Y_train)
    print("Shape of Y_test : ",Y_test)

    ##################################################################
        #Step 5 : Feature Scaling 
    ##################################################################
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scaler = StandardScaler()

    X_train_scaled_ = scaler.fit_transform(X_train)
    X_test_scaled_ = scaler.fit_transform(X_test)

    print("Features Scaling Done Sucesfully ")

    
    ##################################################################
            #Step 6 : Hyper parameter Tuning  
    ##################################################################
    print(border)
    print("Step 6 : Hyper parameter Tuning ")
    print(border)
    accuracy_scores = []

    k_values = range(1,21)

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train_scaled_,Y_train)
        y_pred = model.predict(X_test_scaled_)
        accuracy = accuracy_score(Y_test,y_pred)
        accuracy_scores.append(accuracy)

    print("Accuracy Report : ")
    for i in accuracy_scores:
        print(i)

    print(border)

    ##################################################################
                #Step 7 : Graphical Representation 
    ##################################################################
    print(border)
    print("Step 7 : Graphical Representation ")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(k_values,accuracy_scores,marker='*')
    plt.title("K Values Vs Accuracy")
    plt.xlabel = ("Value of K")
    plt.ylabel = ("Accuracy")
    plt.grid(True)
    plt.show()

def main():
    Rajclassifier("winepredictor.csv")

if __name__ == "__main__":
    main()
