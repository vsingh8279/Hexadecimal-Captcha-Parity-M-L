#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle
import matplotlib.pyplot as plt



pick = open('model.sav','rb')
model = pickle.load(pick)
pick.close()

xtrain, xtest, ytrain, ytest = train_test_split(features, labels, test_size=0.01)

prediction = model.predict(xtest)

accuracy = model.score(xtest, ytest)

categories = ['even', 'odd']

print('ACCURACY:', accuracy)

print('Prediction is:', categories[prediction[0]])

mycap = xtest[0].reshape(100, 100)
plt.imshow(mycap, cmap='gray')
plt.show()

