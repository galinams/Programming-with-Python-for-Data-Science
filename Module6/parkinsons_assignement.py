# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 19:32:59 2017

@author: korol_000
"""
import pandas as pd
from sklearn.svm import SVC
import matplotlib.pyplot as plt

X = pd.read_csv("C:\DAT207x\Programming with Python for Data Science\Module6\Datasets\parkinsons.data")
print X.head()

y = X['status']
X.drop(labels=['name','status'], axis=1, inplace=True)

print X.head()
print y.head()

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=7, test_size=0.3)

from sklearn.preprocessing import Normalizer

#norma = Normalizer().fit(X_train)

#X_train = norma.transform(X_train)
#X_test = norma.transform(X_test)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.preprocessing import MinMaxScaler

#minmax = MinMaxScaler().fit(X_train)
#X_train = minmax.transform(X_train)
#X_test = minmax.transform(X_test)


from sklearn.preprocessing import RobustScaler

#robust = RobustScaler().fit(X_train)
#X_train = robust.transform(X_train)
#X_test = robust.transform(X_test)


from sklearn.decomposition import PCA
#pca = PCA(n_components=5, svd_solver='full')
#pca.fit(X_train)

#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)

from sklearn import manifold

iso = manifold.Isomap(n_neighbors=5, n_components=6)
iso.fit(X_train)
X_train = iso.transform(X_train)
X_test = iso.transform(X_test)


model = SVC()
model.fit(X_train,y_train)

print model.score(X_test,y_test)

best_score = 0

for C in np.arange(0.05,2.05,0.05):
    for gamma in np.arange(0.001,0.101,0.001):
        model = SVC(C=C,gamma=gamma)
        model.fit(X_train,y_train)
        score = model.score(X_test,y_test)
        if best_score < score:
            best_score = score
            print "Best score {0}, C {1}, and gamma {2}".format(best_score,C,gamma)
            