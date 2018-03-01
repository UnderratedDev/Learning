import numpy as np
import cv2

# threshold, extreme simplification of an image

img = cv2.imread ('bookpage.jpg')

# lowlight, any pixel value > 12, is a 1, white, below 12 is black
retval, threshold = cv2.threshold (img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold (grayscaled, 12, 255, cv2.THRESH_BINARY)

# gaussian adaptive threshold, adaptive based on the region we are in

# int block_size=115, double param1=1
# blockSize – Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on.
# C – Constant subtracted from the mean or weighted mean (see the details below). Normally, it is positive but may be zero 
# or negative as well.﻿
gaus = cv2.adaptiveThreshold (grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
retval3, otsu = cv2.threshold (grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow ('original', img)
cv2.imshow ('threshold', threshold)
cv2.imshow ('threshold2', threshold2)
cv2.imshow ('gaus', gaus)
cv2.imshow ('otsu', otsu)


cv2.waitKey (0)
cv2.destroyAllWindows ()