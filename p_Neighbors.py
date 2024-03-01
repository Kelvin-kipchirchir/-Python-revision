#!/usr/bin/env python

#importing relevant imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer

#loading our dataset
data = load_breast_cancer()

#print('Summary of our dataset\n',data.describe())
print(data.feature_names)
print(data.target_names)

#We load the data with the load_breast_cancer function and get the names of the features and targets. Our features are all parameters that should help to determine the label or the target. For the targets, we have two options in this dataset: malignant and benign .

# PREPARING DATA
# again we convert our data back to Numpy arrays and split them into training and test data
X = np.array(data.data)
Y = np.array(data.target)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.1)

#The data attribute refers to our features and the target attribute points to the classes or labels. We again choose a test size of ten percent.

# TRAINING AND TESTING
# We start by first defining our K-Nearest-Neighbors classifier and thentraining it.
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train,Y_train)
# The n_neighbors parameter specifies how many neighbor points we want to consider. In this case, we take five. Then we test our model again for its accuracy.
accuracy = knn.score(X_test,Y_test)
print('calculating the accuracy of our model:\n',accuracy)

#    DETERMINING THE BEST ALGORITHM
#import other libararies other than KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Of course, we need to import all the modules first. We can then create five different classifiers to train and test them with the exact same data.
clf1 = KNeighborsClassifier(n_neighbors = 5)
clf2 = GaussianNB()
clf3 = LogisticRegression()
clf4 = DecisionTreeClassifier()
clf5 = RandomForestClassifier()

clf1.fit(X_train, Y_train)
clf2.fit(X_train, Y_train)
clf3.fit(X_train, Y_train)
clf4.fit(X_train, Y_train)
clf5.fit(X_train, Y_train)

print (clf1.score(X_test, Y_test))
print (clf2.score(X_test, Y_test))
print (clf3.score(X_test, Y_test))
print (clf4.score(X_test, Y_test))
print (clf5.score(X_test, Y_test))

#When you run this program a couple of times, you will notice that we can’t really say which algorithm is the best. Every time we run this script, we will see different results, at least for this specific data set.Again, we can again make predictions for new, unknown data. The chance of success in the classification is even very high. We just need to pass an array of input values and use the predict function .

X_new = np.array([...])
Y_new = clf.predict(X_new)

