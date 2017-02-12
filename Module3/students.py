# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 18:35:24 2017

@author: korol_000
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

data = pd.read_csv('C:\DAT207x\Programming with Python for Data Science\students.data', index_col=0)

print data.head()
my_series = data.G3
my_dataframe = data[['G3','G2','G1']]
plt.figure()
my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5)
plt.show()
data.plot.scatter(x='G1',y='G3')

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')
ax.scatter(data.G1, data.G3, data['Dalc'], c='r', marker='.')
plt.show()