#!/usr/bin/env python
# SUPPORT VECTOR MACHINES
# Now things get mathematically a bit more demanding. This chapter is about Support Vector Machines . These are very powerful, very efficient machine learning algorithms and they even achieve much better results than neural networks in some areas. We are again dealing with classification here but the methodology is quite different.What we are looking for is a hyperplane that distinctly classifies our data points and has the maximum margin to all of our points. We want our model to be as generalized as possible.

# We are looking for the two points that are the farthest away from the other class. In between of those, we draw our hyperplane so that the distance to both points is the same and as large as possible. The two parallel line are the support vectors. In between the orange and the blue line there are no data points. This is our margin. We want this margin to be as big as possible because it makes our predictions more reliable.
#           KERNELS
# The data we have looked at so far is relatively easy to classify because it is clearly separated. Such data can almost never be found in the real world.Also, we are oftentimes working in higher dimensions with many features.This makes things more complicated.

from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#Besides the libraries we already know, we are importing the SVC module.This is the support vector classifier that we are going to use as our model.Notice that we are also importing the KNeighborsClassifier again, since we are going to compare the accuracies at the end.
data = load_breast_cancer()
X = data.data
Y = data.target

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.1,random_state = 30)

#This time we use a new parameter named random_state . It is a seed thatalways produces the exact same split of our data. Usually, the data gets split randomly every time we run the script. You can use whatever number you want here. Each number creates a certain split which doesn’t change no matter how many times we run the script. We do this in order to be able to objectively compare the different classifiers.

# TRAINING AND TESTING
model = SVC(kernel = 'linear',C = 3)
model.fit(X_train,Y_train)
# We are using two parameters when creating an instance of the SVC class.The first one is our kernel and the second one is C which is our soft margin.Here we choose a linear kernel and allow for three misclassifications.Alternatively we could choose poly, rbf, sigmoid, precomputed or a selfdefined kernel. Some are more effective in certain situations but also a lot more time-intensive than linear kernels.

accuracy = model.score(X_test,Y_test)
print('accuracy of SVC:\n',accuracy)

# Using the KNeighborsClassifier with the same random_state
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train,Y_train)
knn_accuracy = knn.score(X_test,Y_test)
print('accuracy of knn:\n',knn_accuracy)


#The results is only a tiny bit worse but when the data becomes larger and more complex we might see a quite bigger diffference

