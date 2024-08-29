#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle

dir = 'new'

categories = ['even', 'odd']

data = []
for category in categories:
    path = os.path.join(dir, category)
    label = categories.index(category)

    for img in os.listdir(path):
        imgpath = os.path.join(path, img)
        cap_img = cv2.imread(imgpath, 0)
        try:
            cap_img = cv2.resize(cap_img, (100, 100))
            image = np.array(cap_img).flatten()
            
            data.append([image, label])  # Corrected variable name from 'image' to 'cap_img'
        except Exception as e:
            pass
    
print(len(data))

pick_in = open('data1.pickle', 'wb')
pickle.dump(data,pick_in)
pick_in.close()

