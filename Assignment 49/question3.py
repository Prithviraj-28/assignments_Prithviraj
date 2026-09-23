from sklearn.metrics import confusion_matrix,classification_report


actual_values = [1, 1, 1, 1, 0, 0, 0, 0]
predicted_values = [1, 1, 0, 1, 0, 1, 0, 0]

confusion = confusion_matrix(actual_values, predicted_values)
print("Confusion Matrix is : \n", confusion)

classification = classification_report(actual_values, predicted_values)
print("Classification Report is : \n", classification)
