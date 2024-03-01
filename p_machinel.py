#!/usr/bin/env python
print('-----------machine learning---------')
# NUMPY
# numpy module allows us to efficiently work with vectors,matrices and multidimentional arrays.Crucial for linear algebra and numerical analysis.it basically replaces the primitive and inefficient python list with very powerful numpy arrays
# MATPLOTLIB
# PANDAS
# SCIKIT-LEARN
# TENSORFLOW

# LINEAR REGRESSION
# the easiest and most basic machine learning algorithm.Its a supervised learning algorithm meaning we both need inputs and outputs to train our model.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = pd.read_csv("C:/Users/Kelvin Walker/Downloads/Compressed/student/student-mat.csv",sep=';')
#we change our separator to semicolon,since the default separator for CSV files is a comma and our files is separated by a semicolons
#next step we think about our features(columns)are relevant where we fetch the following
print(data.columns)

# DOING SOME CLEANING
data = data.dropna(axis=0)

data = data[[ 'age', 'sex', 'studytime', 'absences', 'G1', 'G2', 'G3']]

print("Describing our data\n",data.describe())

print("Printing the head\n",data.head())


#the columns G1,G2,G3 are the three grades that the student get.our goal is to predict the third and final grade by looking at other values like first grade,age,sex etc
#summerized that means that we only select these columns from our dataframe,out of the 33 possible.G3 is our labe and the rest are our features.Each feature is an axis in the coordinate system and each point is in a record ie one row in the table.
# Looking closely the sex feature is not numeric but stored as F(female) or M(male).For this to work with it and register it in the coordinate system,we have to convert it into numbers
data['sex'] = data['sex'].map({'F':0,'M':1})
# we do this by using the map function.Here we map a dictionary to our feature.Each F becomes a zero and every M becomes a one.We can work on it
# Finally we define the column of the desired label as a variable to make it easier to work with 
prediction = 'G3'

#    PREPARING DATA
# our data is now fully loaded and selected.However in order to use it as training and testing data for our model we have to reformat them.The sklearn models do not accept pandas data frames but only numpy arrays.Thats why we turn our features into an x-array and our labels into a y-array
X = np.array(data.drop([prediction],1))
Y = np.array(data[prediction])

#The method np.array converts the selected columns into an array.The drop function returns the data frame without the specified column.Our X array now contains all of our columns,except the final grade.The final grade is in the Y array
# In order to train and test our model, we have to split our available data. The first part is used to get the hyperplane to fit our data as well as possible. The second part then checks the accuracy of the prediction, with previously unknown data.

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.1)

# With the function train_test_split , we divide our X and Y arrays into four arrays. The order must be exactly as shown here. The test_size parameter specifies what percentage of records to use for testing. In this case, it is 10%. This is also a good and recommended value. We do this to test how accurate it is with data that our model has never seen before.
#         TRAINING AND TESTING
# Now we can start training and testing our model.For that we first define our model
model = LinearRegression()
model.fit(X_train,Y_train)

#By using the constructor of the LinearRegression class, we create our model. We then use the fit function and pass our training data. Now our model is already trained. It has now adjusted its hyperplane so that it fits all of our values. In order to test how well our model performs, we can use the score method and pass our testing data.

accuracy = model.score(X_test,Y_test)
print(accuracy)

# Actually, 91 percent is a pretty high and good accuracy. Now that we know that our model is somewhat reliable, we can enter new data and predict the final grade
x_new = np.array([[18,1,3,40,15,16]])
Y_new = model.predict(x_new)
print("Estimated final grade is:",Y_new)

# Here we define a new NumPy array with values for our features in the right order. Then we use the predict method, to calculate the likely final grade for our inputs.

#  VISUALIZING CORRELATIONS
# Since we are dealing with high dimensions here, we can’t draw a graph of our model. This is only possible in two or three dimensions. However what we can visualize are relationships between individual features.

#plt.scatter(data['studytime'],data['G3'])
#using these we see the relationship is not really strong.The data is very diverse and you cannot see a clear pattern.
#method 2
plt.scatter(data['G2'],data['G3'])
# if we look at the correlation between the second grade and the final grade we see a much stronger correlation
plt.title('Correlation')
plt.xlabel('Study Time')
plt.ylabel('Final Grade')
plt.show()

# Here we draw a scatter plot with the function scatter, which shows therelationship between the learning time and the final grade.


#     CLASSIFICATION
#an example is the the K-Nearest-Neighbor classifier. Here we already have a decent amount of classified elements. We then add a new one (represented by the stars) and try to predict its class by looking at its nearest neighbors.

# CLASSIFICATION ALGORITHMS
# There are various different classification algorithms and they are often used for predicting medical data or other real life use-cases. For example, by providing a large amount of tumor samples, we can classify if a tumor is benign or malignant with a pretty high certainty.

#  K-NEAREST-NEIGHBORS
# As already mentioned, by using the K-Nearest-Neighbors classifier, we assign the class of the new object, based on its nearest neighbors. The K specifies the amount of neighbors to look at. For example, we could say that we only want to look at the one neighbor who is nearest but we could alo say that we want to factor in 100 neighbors.Notice that K shouldn’t be a multiple of the number of classes since itemight cause conflicts when we have an equal amount of elements from one class as from the other..

#  NAIVE-BAYES
# The Naive Bayes algorithm might be a bit confusing when you encounter it the first time. However, we are only going to discuss the basics and focus more on the implementation in Python later on.Imagine that we have a table like the one above. We have four input values (which we would have to make numerical of course) and one label or output. The two classes are Yes and No and they indicate if we are goin to play outside or not.What Naive Bayes now does is to write down all the probabilities for the individual scenarios. So we would start by writing the general probability of playing and not playing. In this case, we only play three out of eight times and thus our probability of playing will be 3/8 and the probability of not playing will be 5/8.Also, out of the five times we had a high humidity we only played once,whereas out of the three times it was normal, we played twice. So our probability for playing when we have a high humidity is 1/5 and for playing when we have a medium humidity is 2/3. We go on like that and note all the probabilities we have in our table. To then get the classification for a new entry, we multiply the probabilities together and end up with a prediction.
#     LOGISTIC REGRESSION
# Another popular classification algorithm is called logistic regression . Even though the name says regression , this is actually a classification algorithm.It looks at probabilities and determines how likely it is that a certain event happens (or a certain class is the right one), given the input data. This is done by plotting something similar to a logistic growth curve and splitting the data into two. Since we are not using a line (and thus our model is not linear), we are also preventing mistakes caused by outliers.
#     DECISION TREES
#With decision tree classifiers, we construct a decision tree out of our training data and use it to predict the classes of new elements.This classification algorithm requires very little data preparation and it isalso very easy to understand and visualize. On the other hand, it is very easy to be overfitting the model. Here, the model is very closely matched to the training data and thus has worse chances to make a correct prediction on new data.
#   RANDOM FOREST
# The last classification algorithm of this chapter is the random forest classifier. It is based on decision trees. What it does is creating a forest of multiple decision trees. To classify a new object, all the various trees determine a class and the most frequent result gets chosen. This makes the result more accurate and it also prevents overfitting. It is also more suited to handle data sets with higher dimensions. O generation of the forest is random , you have very little control over yourmodel.
