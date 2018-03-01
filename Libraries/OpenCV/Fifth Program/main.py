import numpy as np
import cv2

# must be identical size images
img1 = cv2.imread ('3D-Matplotlib.png')
# img2 = cv2.imread ('mainsvmimage.png')
img2 = cv2.imread ('mainlogo.png')

# must be smaller ideally 1/4 the size

# images do not lose opaqueness
# add = img1 + img2

# whited out image, added all the pixel values together
# for example: (155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255).
# hence why it is bright white, can divide by 2 and then add
# add = cv2.add (img1, img2)

# each image has a weight, and the last parameter is gamma
# weighted = cv2.addWeighted (img1, 0.6, img2, 0.4, 0)

# cv2.imshow ('add', add)
# cv2.imshow ('weighted', weighted)

rows, cols, channels = img2.shape
# making it identical size
roi = img1[0:rows, 0:cols]

# mask, initial will be the conversion to grayscale
img2gray = cv2.cvtColor (img2, cv2.COLOR_BGR2GRAY)

# apply threshold, won't be using ret
# Binary Threshold, 0 or 1, 220, threshold value, if pixel value about 220, converted to 255
# if below 220, converted to black, flipping it because inverse
ret, mask = cv2.threshold (img2gray, 220, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow('mask', mask)

# black area of the mask
# bitwise is a lowlevel logical operation, where not mask, is a value
mask_inv = cv2.bitwise_not (mask)

img1_bg = cv2.bitwise_and (roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and (img2, img2, mask=mask)

dst = cv2.add (img1_bg, img2_fg)

img1[0:rows, 0:cols] = dst

cv2.imshow ('res', img1)
cv2.imshow ('mask_inv', mask_inv)
cv2.imshow ('img1_bg', img1_bg)
cv2.imshow ('img2_fg', img2_fg)
cv2.imshow ('dst', dst)

cv2.waitKey (0)
cv2.destroyAllWindows ()