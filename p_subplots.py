#!/usr/bin/env python
print('----------subplots-----------------')
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,5,200)
y1 = np.sin(x)
y2 = np.sqrt(x)
plt.subplot(211)
plt.plot(x,y1,'r-')
plt.subplot(212)
plt.plot(x,y2,'g--')
plt.show()

