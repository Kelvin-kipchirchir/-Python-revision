#!/usr/bin/env python
print("------------doing some matplotlib plotting------------")
import numpy as np
import matplotlib.pyplot as plt
x_values = np.linspace(0,20,100)#creating an array of 100 values 
#in order to plot we need the x-values or the inputs and the y-values or the output
y_values = np.sin(x_values)
plt.plot(x_values,y_values)#we do this by using the function plot and passing our x-values and the y-values
#plt.show()#at the end call the show function to display our plot

x = np.linspace(0,10,100)
y = (6*x-30)**2
plt.plot(x,y)
#plt.show()

# VISUALIZING VALUES
numbers = 10 * np.random.random(100)
plt.plot(numbers,'bo')#first letter-blue second -dots
#plt.show()

#  MULTIPLE GRAPHS
x2 = np.linspace(0,5,200) #first generate 200 x-values form 0 to 5
y1 = 2 * x2
y2 = x2 ** 2
#y3 = np.log(x2)
plt.plot(x2,y1)
plt.plot(x2,y2)
#plt.plot(x2,y3)
#plt.show()

#  SUBPLOTS
# sometimes we want to draw multiplegraphs but we dont want them in the sane plot
d = np.linspace(0,5,200)
e1 = np.sin(d)
e2 = np.sqrt(d)
#plt.subplot(211)
plt.figure(1)
plt.plot(d,e1,'r-')
#plt.subplot(212)
plt.figure(2)

plt.subplot(d,e2,'g--')
plt.show()

