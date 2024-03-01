#!/usr/bin/env python
# CLUSTERING
# Up until now, we have only looked at supervised learning algorithms.Clustering however is an unsupervised learning algorithm, which means that we don’t have the results for our inputs. We can’t tell our model what is right and wrong. It has to find patterns on its own.The algorithm gets raw data and tries to divide it up into clusters . KMeans-Clustering is the method that we are going to use here. Similar to KNearest-Neighbors, the K states the amount of clusters we want.

# HOW CLUSTERING WORKS
# The clustering itself works with so-called centroids . These are the points,which lie in the center of the respective clusters.
#For the clustering algorithm, we will use a dataset of handwritten digits.Since we are using unsupervised learning, we are not going to classify the digits. We are just going to put them into clusters. The following imports are necessary:

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits

#Besides the KMeans module and the load_digits dataset, we are also importing the function scale from the preprocessing library. We will use this function for preparing our data.

digits = load_digits()
data = scale(digits.data)

#After loading our dataset we use the scale function, to standardize our data.We are dealing with quite large values here and by scaling them down tosmaller values we save computation time.
#  TRAINING AND PREDICTING
# we can now train our model the dame way we trained the supervised learning models up until now
clf = KMeans(n_clusters = 10,init = 'random',n_init = 10)
clf.fit(data)

#Here we are passing three parameters. The first one (n_clusters ) defines the amount of clusters we want to have. Since we are dealing with the digits 0 to 9, we create ten different clusters.
# With the init parameter we choose the way of initialization. Here we chose random , which obviously means that we just randomly place the centroids somewhere. Alternatively, we could use k-means++ for intelligent placing.The last parameter (n_init ) states how many times the algorithm will be run with different centroid seeds to find the best clusters.Since we are dealing with unsupervised learning here, scoring the model is not really possible. You won’t be able to really score if the model is.clustering right or not. We could only benchmark certain statistics like completeness or homogeneity .What we can do however is to predict which cluster a new input belongs to.
clf.predict([...])


#In this case, inputting data might be quite hard, since we would need tomanually put in all the pixels. You could either try to write a script what converts images into NumPy arrays or you could work with a much simpler data set.Also, since we are working with huge dimensions here, visualization is quite hard. When you work with two- or three-dimensional data, you canuse the Matplotlib knowledge from volume three, in order to visualize your model.
