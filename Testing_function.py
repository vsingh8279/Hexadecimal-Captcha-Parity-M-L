#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import os
import pickle
import numpy as np

def decaptcha(filenames):
    filenames1 = []
    
    for image in filenames:
        I = cv2.imread(image,0)  
        crop = I[0:100, 358:458]


        

        _, I_binary = cv2.threshold(crop, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        H = np.ones((3, 3), dtype=np.float32) / 9

        I_fil=I_binary

        SE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))

        # Perform morphological closing
        Iclosed = cv2.morphologyEx(I_fil, cv2.MORPH_CLOSE, SE)

        # Subtract the closed image from the filtered image
        Isub = cv2.subtract(Iclosed, I_fil)

        # Invert the subtracted image
        I_new = cv2.bitwise_not(Isub)

        # Subtract the inverted image from the filtered image
        I_clear =cv2.bitwise_not((cv2.subtract(I_new, I_fil)))
        I_clear_resized = cv2.resize(I_clear, (100, 100))  # Adjust the size as needed
        image1 = np.array(I_clear_resized).flatten()
        
        filenames1.append(image1)
        

    pick = open('model.sav', 'rb')
    model = pickle.load(pick)
    pick.close()

    prediction = model.predict(filenames1)
    
    a = len(prediction)
    labels = []

    for i in range(a):
        if prediction[i] == 0:
            labels.append("even")
        else:
            labels.append("odd")



    return labels

