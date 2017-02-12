import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')
# This code is intentionally missing!
# Read the directions on the course lab page!
df = pd.read_csv('C:\DAT207x\Programming with Python for Data Science\Module3\Datasets\wheat.data')
print df.head()

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
# 
# .. your code here ..

df.drop('id', axis=1, inplace =True)
print df.head()

#
#
# 
# .. your code here ..
plt.figure()
andrews_curves(df, 'wheat_type', alpha=0.4)

plt.show()