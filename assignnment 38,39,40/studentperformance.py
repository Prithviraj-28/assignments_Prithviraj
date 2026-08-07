import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report
from sklearn.tree import plot_tree

border = "-" * 100
#########################################################################

       #Step 1: Read the data from the CSV file into a pandas DataFrame

##########################################################################
#Task1 : Display the first 5 rows of the DataFrame
#Task2 : Display the last 5 rows of the DataFrame
#Task 3 : Display total number of rows and columns in the DataFrame
#Task 4 : Display the column names of the DataFrame
######################################################################

dataset = pd.read_csv("student_performance_ml.csv")

print(border)
#Task1 : Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(dataset.head(5))
print(border)

#Task2 : Display the last 5 rows of the DataFrame
print("Last 5 rows of the DataFrame:")
print(dataset.tail(5))
print(border)

#Task 3 : Display total number of rows and columns in the DataFrame
print("Total number of rows and columns in the DataFrame:")
print(dataset.shape)
print(border)

#Task 4 : Display the column names of the DataFrame
print("Column names of the DataFrame:")
print(list(dataset.columns))
print(border)


#########################################################################

       #Step 2: Exploratory Data Analysis (EDA)

##########################################################################
#Task 1. Display total number of students in the dataset 
#Task 2. Count How many students PAssed and how many students Failed in the dataset
#Task 3. Calculate and display the average study hours of the students in the dataset
#Task 4. Calculate and display the average attendance of the students in the dataset
#Task 5. Calculate and display the maximum previous score of the students in the dataset
#Task 6. Calculate and display the maximum sleep hours of the students in the dataset
##########################################################################

#Task 1. Display total number of students in the dataset 
print(f"Total number of students in the dataset: {len(dataset)}")
print(border)

#Task 2. Count How many students PAssed and how many students Failed in the dataset
p= dataset["FinalResult"].value_counts()
print(f"Number of students who Passed: {p[1]}")
print(f"Number of students who Failed: {p[0]}")
print(border)

#Task 3. Calculate and display the average study hours of the students in the dataset
average_study_hours = dataset["StudyHours"].mean()
print(f"Average study hours of the students in the dataset: {average_study_hours:.2f}")
print(border)

#Task 4. Calculate and display the average attendance of the students in the dataset
average_attendance = dataset["Attendance"].mean()   
print(f"Average attendance of the students in the dataset: {average_attendance:.2f}")
print(border)   

#Task 5. Calculate and display the maximum previous score of the students in the dataset
max_previous_score = dataset["PreviousScore"].max()
print(f"Maximum previous score of the students in the dataset: {max_previous_score}")
print(border)

#Task 6. Calculate and display the maximum sleep hours of the students in the dataset
max_sleep_hours = dataset["SleepHours"].max()
print(f"Maximum sleep hours of the students in the dataset: {max_sleep_hours}")
print(border)   



#########################################################################

       #Step 3: Decide Independent and Dependent Variables

##########################################################################
# X -->: Independent variables / Features
# Y -->: Dependent variables / Labels
##########################################################################

X = dataset [ ["StudyHours","Attendance", "PreviousScore","AssignmentsCompleted", "SleepHours"] ]
Y = dataset["FinalResult"]

print(f"X shape : {X.shape}")
print(f"Y shape : {Y.shape}")

print(border)

#########################################################################

       #Step 4 :  Visualitaion of Data set

##########################################################################
#Task 1: Plot a histogram of study hours 
#Task 2 : Create a scatter plot of study hours vs previous score
#Task 3 : Create a box plot of attendance 
#Task 4 : Create a plot showing relationship bettwen assignment completed and final result
#Task 5 : Create a plot showing relationship bettwen sleep hours and final result      
##########################################################################

#Task 1: Plot a histogram of study hours 
plt.hist(dataset["StudyHours"], bins=20)
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.title("Prithviraj Histogram of Study Hours")
plt.show()
plt.legend()
plt.grid() 

#Task 2 : Create a scatter plot of study hours vs previous score
plt.scatter(dataset["StudyHours"], dataset["PreviousScore"])
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Prithviraj Scatter Plot of Study Hours vs Previous Score")
plt.show()
plt.legend()
plt.grid()

#Task 3 : Create a box plot of attendance
plt.boxplot(dataset["Attendance"])
plt.xlabel("Attendance")
plt.ylabel("Frequency")
plt.title("Prithviraj Box Plot of Attendance")
plt.show()

#Task 4 : Create a plot showing relationship bettwen assignment completed and final result
plt.scatter(dataset["AssignmentsCompleted"], dataset["FinalResult"])
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.title("Prithviraj Scatter Plot of Assignments Completed vs Final Result")
plt.show()
plt.legend()
plt.grid()

#Task 5 : Create a plot showing relationship bettwen sleep hours and final result 
plt.scatter(dataset["SleepHours"], dataset["FinalResult"])
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.title("Prithviraj Scatter Plot of Sleep Hours vs Final Result")
plt.show()
plt.legend()
plt.grid()

#########################################################################

       #Step 5 :  Split the Dataset for traning and testing

##########################################################################
print(border)
x_train, x_test,y_train,y_test = train_test_split(X,Y, test_size=0.2, random_state=42) 

# This will split the dataset into training and testing sets, with 80% of the data used for training and 20% for testing.
# The random_state parameter ensures that the split is reproducible

print(f"X shape : {X.shape}")
print(f"Y shape : {Y.shape}")

print(f"x_train shape : {x_train.shape}")
print(f"x_test shape : {x_test.shape}")

print(f"y_train shape : {y_train.shape}")
print(f"y_test shape : {y_test.shape}")

#########################################################################

       #Step 6 :  Build The Model 

##########################################################################

print(border)
model = DecisionTreeClassifier(max_depth=3) 

#########################################################################

       #Step 7 :  Train The Model 

##########################################################################

model.fit(x_train,y_train)


#########################################################################

       #Step 8 :  Test The Model 

##########################################################################
#Task 1: Use the trained model to make predictions on the custom test data
##########################################################################
y_pred = model.predict(x_test)

print("Actual Results : ",y_test.values)
print(border)

print("Predicted Results : ",y_pred)
print(border)

#Task 1: Use the trained model to make predictions on the custom test data
custom = [[6,85,66,7,7],[4,60,50,5,6],[8,90,80,9,8]]
custom_pred = model.predict(custom)
print("Custom Prediction : ",custom_pred)

print(border)
#########################################################################

       #Step 9 :  Evaluate The Model Performance 

##########################################################################
#Task 1 : Calculate and display the accuracy of the model
#Task 2 : Calculate and display the confusion matrix of the model
#Task 3 : Calculate and display the classification report of the model
##########################################################################

#Task 1 : Calculate and display the accuracy of the model
accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy of the model: {accuracy*100}%")

#Task 2 : Calculate and display the confusion matrix of the model
cm = confusion_matrix(y_test,y_pred)
print(f"Confusion Matrix:\n{cm}")

#Task 3 : Calculate and display the classification report of the model
print(f"Classification Report:\n{classification_report(y_test,y_pred)}")


#########################################################################

       #Step 10 :  Trained Model Visualization 

##########################################################################

plt.figure(figsize=(12,8))
plot_tree(model, filled=True, feature_names=X.columns, class_names=["Fail", "Pass"])
plt.title("Decision Tree Visualization")
plt.show()