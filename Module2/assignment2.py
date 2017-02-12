import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset

#
df = pd.read_csv('C:/DAT207x/Programming with Python for Data Science/Module2/Datasets/tutorials.csv')

print df.head()
print df.describe()
print df.loc[2:4, 'col3']
# TODO: Print the results of the .describe() method
#
# .. your code here ..



# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..

