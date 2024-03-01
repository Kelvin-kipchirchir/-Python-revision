#!/usr/bin/env python
print('hello tensorflow')
import tensorflow.compat.v1 as tf
hello = tf.constant('hello tensor')
sess = tf.Session()
print(sess.run(hello))
