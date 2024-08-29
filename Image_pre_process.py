#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

# Load the image
I= cv2.imread("location/image.png")
crop = I[0:100, 358:458]


# Display the original image

cv2.waitKey(0)

# Convert the image to grayscale
I_gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)


# Perform contrast adjustment
I_adj = cv2.equalizeHist(I_gray)


# Perform adaptive thresholding
_, I_binary = cv2.threshold(I_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


# Define the average filter kernel
H = np.ones((3, 3), dtype=np.float32) / 9

# Apply average filtering
# I_fil = cv2.filter2D(I_binary, -1, H, borderType=cv2.BORDER_REPLICATE)
# cv2.imshow("fil", I_fil)
I_fil=I_binary

# Define the disk-shaped structuring element
SE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))

# Perform morphological closing
Iclosed = cv2.morphologyEx(I_fil, cv2.MORPH_CLOSE, SE)

# Subtract the closed image from the filtered image
Isub = cv2.subtract(Iclosed, I_fil)

# Invert the subtracted image
I_new = cv2.bitwise_not(Isub)

# Subtract the inverted image from the filtered image
I_clear =cv2.bitwise_not((cv2.subtract(I_new, I_fil)))
I_new = cv2.filter2D(I_clear, -1, H, borderType=cv2.BORDER_REPLICATE)
# cv2.imshow("fil", I_fil)

# Display the cleared image
cv2.imshow("Cleared Image", I_new)
cv2.waitKey(0)
cv2.destroyAllWindows()

