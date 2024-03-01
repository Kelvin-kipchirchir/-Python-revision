#!/usr/bin/env python
print('---------------------matplotlib legends-------------')
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(10,50,100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x/3)
plt.plot(x,y1,'b-',label = "Sine")
plt.plot(x,y2,'r-',label = "Cosine")
plt.plot(x,y3,'g-',label = "Logarithm")
plt.legend( loc = 'upper left')
plt.show()

# SAVING DIAGRAMS
#plt.savefig('functions.png')

