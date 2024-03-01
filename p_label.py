#!/usr/bin/env python
print('--------------------labeling diagrams------------')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
# using above we can label the axes,give windows title

x = np.linspace(0,50,100)
y = np.sin(x)
plt.title('Sine Function')
plt.suptitle('Data Science')
plt.figure('MyFigure')
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.grid(True)
plt.plot(x,y)
plt.show()

