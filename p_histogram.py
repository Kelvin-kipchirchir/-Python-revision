#!/usr/bin/env python
print('----------------welcome to python histograms-------------')
import numpy as np
import matplotlib.pyplot as plt
mu,sigma = 172,4
x = mu + sigma * np.random.rand(10000)
plt.hist(x,100,density = True,facecolor = "blue")
plt.xlabel("Height")
plt.ylabel("probability")
plt.title("Height of Students")
plt.text(160,0.125,"u = 172,e=4")
plt.axis([155,190,0,0.15])
plt.grid(True)
plt.show()

