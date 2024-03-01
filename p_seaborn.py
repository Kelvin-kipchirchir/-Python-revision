#!/usr/bin/env python
print('hello world')
import tensorflow as tf
import seaborn as ss
print(ss.__version__)
print(tf.__version__)

x = tf.constant(1)
y = tf.constant(2)
z = tf.add(x,y)
from tensorflow.keras.layers import Dense
layer = Dense(units=1,kernel_initializer='ones',use_bias=False)
data = tf.constant([[1.0,2.0,3.0]])

result = layer(data)
print(result)
print(result.numpy())

hello = tf.constant('hello tensorflow')

with tf.compat.v1.Session() as sess:
    print(sess.run(hello))

