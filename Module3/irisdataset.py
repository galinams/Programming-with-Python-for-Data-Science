# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 20:27:36 2017

@author: korol_000
"""

from sklearn.datasets import load_iris
from pandas.tools.plotting import andrews_curves
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
print df.columns
print df.head()
print data
df['target_names'] = [data.target_names[i] for i in data.target]
plt.figure()
andrews_curves(df, 'target_names')
plt.show()