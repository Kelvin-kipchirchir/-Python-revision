#!/usr/bin/env python
# STRUCTURE OF A NEURAL NETWORK
# With neural networks we are trying to build our models based on the structure of the human brain, namely with neurons. The human brain is composed of multiple billions of neurons which are interconnected. Neural networks are structures which try to use a similar principle.In the figure above, we can see three layers. First the input layer , at the end the output layer and in between the hidden layer .Obviously the input layer is where our inputs go. There we put all the things which are being entered or sensed by the script or the machine. Basically these are our features.We can use neural networks to classify data or to act on inputs and the output layer is where we get our results. These results might be a class or action steps. Maybe when we input a high temperature into our model, the output will be the action of cooling down the machine.All the layers between input and output are called hidden layers . They make the model more abstract and more complex. They extend the internal logic. The more hidden layers and neurons you add, the more sophisticated the model gets.Here for example we have two hidden layers, one with four neurons andone with three neurons. Notice that every neuron of a layer is connected to every neuron of the next layer.

# STRUCTURE OF A NEURON
#In order to understand how a neural network works in general, we need to understand how the individual neurons work.As you can see, every neuron has a certain input, which is either the output of another neuron or the input of the first layer.This number (which is the input) now gets multiplied by each of the weights (w1, w2, w3…) . After that, we subtract the bias b . The results of these calculations are the outputs of the neuron.
#What I have just explained and what you can see on the picture is an outdated version of a neuron called a perceptron . Nowadays, we are using more complex neurons like the sigmoid neurons which use more sophisticated activation functions to calculate the outputs.Now you can maybe imagine to some degree how complex these systems get when we combine hundreds of thousands of these neurons in one network

# HOW NEURAL NETWORKS WORK
# But what has all this to do with artificial intelligence or machine learning? Since neural networks are structures with a huge amount of parameters that can be changed, we can use certain algorithms so that the model can adjust itself. We input our data and the desired outcome. Then the model tries to adjust its weights and biases so that we can get from our inputs to the respective outputs. Since we are dealing with multiple thousands of neurons, we can’t do all this manually.

#We use different algorithms like backpropagation and gradient descent , to optimize and train our model. We are not going to deep into the mathematics here. Our focus will be on the coding and the implementation.

# RECOGNIZING HANDWRITTEN DIGITS
# Up until now, we always used the sklearn module for traditional machinelearning. Because of that all our examples were quite similar. In this chapter, we will use Tensorflow . We will need the following imports:

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# LOADING DATA
# The handwritten digits data that we are going to use in this chapter is provided by the Tensorflow Keras datasets. It is the so-called MNIST dataset which contains 70,000 images of handwritten digits in the resolution of 28x28 pixels.
mnist = tf.keras.datasets.mnist
(X_train,Y_train),(X_test,Y_test) = mnist.load_data()

#The mnist class that we import here has the function load_data . This function returns two tuples with two elements each. The first tuple contains our training data and the second one our test data. In the training data we can find 60,000 images and in the test data 10,000. The images are stored in the form of NumPy arrays which contain the information about the individual pixels. Now we need to normalize our data to make it easier to handle.

X_train = tf.keras.utils.normalize(X_train)
X_test = tf.keras.utils.normalize(X_test)

#By normalizing our data with the normalize function of the keras.utils module, we scale our data down. We standardize it as we have already done in the last chapter. Notice that we are only normalizing the X-values since it wouldn’t make a lot of sense to scale down our results, which are the digits from 0 to 9.
# BUILDING THE NEURAL NETWORK
# We have prepared our data so that we can now start building our network.Tensorflow offers us a very easy way to construct neural networks. We just create a model and then define the individual layers in it.
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape =(28,28)))
model.add(tf.keras.layers.Dense(units = 128,activation = 'relu'))
model.add(tf.keras.layers.Dense(units = 128,activation = 'relu'))
model.add(tf.keras.layers.Dense(units = 10,activation = tf.nn.softmax))

#First we define our model to be a Sequential . This is a linear type of model where which is defined layer by layer. Once we have defined the model, we can use the add function to add as many different layers as we want.The first layer that we are adding here is the input layer. In our case, this is a Flatten layer. This type of layer flattens the input. As you can see, we have specified the input shape of 28x28 (because of the pixels). What Flatten does is to transform this shape into one dimension which would here be 784x1.
#All the other layers are of the class Dense . This type of layer is the basic one which is connected to every neuron of the neighboring layers. We always specify two parameters here. First, the units parameter which statesthe amount of neurons in this layer and second the activation which specifies which activation function we are using.
#We have two hidden layers with 128 neurons each. The activation function that we are using here is called relu and stands for rectified linear unit . This is a very fast and a very simple function. It basically just returns zero whenever our input is negative and the input itself whenever it is positive.We use it because it is quite simple, quite powerful, very fast and prevents negative values.
#For our output layer we only use ten neurons (because we have ten possible        digits to classify) and a different activation function. This one is called softmax and what it does is it picks output values so that all of our end results add up to one. Because of this we are getting ten different probabilities for each digit, indicating its likelihood.Our model is now defined but before we can start working with it, we have to compile it first. By doing this we define certain parameters and configure it for training and testing.


model.compile(optimizer = 'adam',loss = 'sparse_categorical_crossentropy',metrics = ['accuracy'])

#Here we define three things, namely the optimizer , the loss function and the metrics that we are interested in. We are not going to go into the math of the adam optimizer or the sparse_categorical_crossentropy loss function.However, these are very popular choices, especially for tasks like this one.

# TRAINING AND TESTING
#The training and testing of the model is quite simple and very similar to the way we did it with sklearn models.

model.fit(X_train,Y_train,epochs = 3)
loss,accuracy = model.evaluate(X_test,Y_test)
print('Loss: ',loss)
print('Accuracy: ',accuracy)

