#!/usr/bin/env python
print('-------------------------using pandas to read csv----------')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = { 'Name' : [ 'Anna' , 'Bob' , 'Charles' ,
    'Daniel' , 'Evan' , 'Fiona' ,
    'Gerald' , 'Henry' , 'India' ],
    'Age' : [ 24 , 24 , 35 , 45 , 22 , 54 , 54 , 43 , 25 ],
    'Height' : [ 176 , 187 , 175 , 182 , 176 ,
        189 , 165 , 187 , 167 ]}

df = pd.DataFrame(data)
df.to_csv('mydf.csv')
dataset = pd.read_csv('mydf.csv')
#dataset.set_index('id',inplace=True)
print('Loaded dataset becomes:\n',dataset)
dataset.sort_values(by=['Age','Height'])
dataset.hist()
plt.show()

plt.plot(dataset['Age'],'bo')
plt.show()


