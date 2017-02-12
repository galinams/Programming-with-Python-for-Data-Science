import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
from os import listdir
path = "C:/DAT207x/Programming with Python for Data Science/Module4/Datasets/ALOI/32/"
files = listdir(path)
samples1 = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
for fname in files:
    img = misc.imread(path+fname)
    samples1.append((img[::2,::2]/255.0).reshape(-1))


# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
path2 = "C:/DAT207x/Programming with Python for Data Science/Module4/Datasets/ALOI/32i/"
files2 = listdir(path2)
samples2=[]
for fname in files2:
    img = misc.imread(path2+fname)
    samples2.append((img[::2,::2]/255.0).reshape(-1))

samples = samples1.append(samples2)
#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 

df = pd.DataFrame(samples)

print df.head()

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 

from sklearn import manifold
iso = manifold.Isomap(n_components=3,n_neighbors=6)
iso.fit(df)
manifold = iso.transform(df)


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(manifold[:,0],manifold[:,1], marker='.',alpha=0.7)



#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(manifold[:,0],manifold[:,1], manifold[:,2], marker='.',alpha=0.7)

plt.show()

