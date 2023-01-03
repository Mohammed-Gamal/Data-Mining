import pandas as pd

#---- Importing the dataset
Data_set = pd.read_csv("Breast_Cancer.csv", delimiter=",")
print(Data_set.shape)  # 4024 rows, 16 columns
print(Data_set)


#---- Choosing, retrieving and formatting the target/goal (i.e., differentiate feature)
target_name = 'Status'

target = Data_set[target_name].tolist()
target = list(set(target))  # we used a set to retrieve the unique names only

print(target)


#---- Getting the desired features (i.e., columns) from the dataset
print(f'{Data_set.shape[0]} rows, {Data_set.shape[1]} columns\n')  # 4024, 16

Features_names = Data_set.columns[0:Data_set.shape[1]-1]  # all except the 'Status' column
print(Features_names)


# Getting the values of the retrieved columns
X = Data_set[Features_names].values
print(X)


#---- Data Preprocessing Step (Categorical data to numeric data, for distance functions)
# LabelEncoder() is used to encode categorical data as numeric data
from sklearn import preprocessing

for index, feature in enumerate(Features_names):

  # Ignore numerical features
  if (Data_set.dtypes[feature] == 'object'):
    print(f'{index}: {feature} → {Data_set.dtypes[feature]}')

    # 1) Get the unique values
    label = Data_set[feature].tolist()
    label = list(set(label))
    print(label, end='\n\n')

    # 2) Convert to numerical
    label_numeric = preprocessing.LabelEncoder()
    label_numeric.fit(label)
    X[:, index] = label_numeric.transform(X[:, index])

print(X)


#---- Splitting the dataset into training and testing sets
import pandas as pd
from sklearn.model_selection import train_test_split

Y = Data_set[target_name]  # Terget/Goal
print(Y)

# Dimensions of the dataset
print(Data_set.shape)  # 4024, 16

# Split the data into 80% for training and 20% for testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

print(X_train.shape)
print(X_test.shape)

print(Y_train.shape)
print(Y_test.shape)


# ----------------  KNN (K-Nearest Neighbors) Classifier  ----------------
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from math import sqrt

# Choosing the best value for n. 'sqrt(n)'
n = int(sqrt(Data_set.shape[0]))
print(n)

# Apply the KNN classifier with n neighbors
neigh = KNeighborsClassifier(n_neighbors=n)  


# Train the Model using Training Sets (i.e. Classified data)
neigh.fit(X_train, Y_train)


# Do prediction on the testing set
predicted = neigh.predict(X_test)
print(predicted.shape)
print("\nPredicted by KNN:\n", predicted)


# Compare the predicted results with the predefined data (i.e., Accuracy)
results = metrics.confusion_matrix(Y_test, predicted)
print("\nKNN confusion matrix:\n", results)

print("\nKNN Accuracy: ", metrics.accuracy_score(Y_test, predicted))


# ----------------  Naive Bayes Classifier  ----------------
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

# Create a GaussianNB Classifier
model = GaussianNB()

# Train the Model using Training Sets (i.e. Classified data)
model.fit(X_train, Y_train)


# Do prediction on the testing set
predicted = model.predict(X_test)
print(predicted.shape)
print("\nPredicted by Naive Bayes:\n", predicted)


# Compare the predicted results with the predefined data (i.e., Accuracy)
results = metrics.confusion_matrix(Y_test, predicted)
print("\nNaive Bayes confusion matrix:\n", results)

print("\nNaive Bayes Accuracy: ", metrics.accuracy_score(Y_test, predicted))
