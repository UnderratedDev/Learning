import numpy as np
import cv2

img = cv2.imread ('watch.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]

# print (px)

img[55, 55] = [255, 255, 255]

# Region of image, sub image of an image
# Region of interest is the more formal name
roi = img[100:150, 100:150] = [255, 255, 255]

# print (roi)

#107 - 37 = 74 pixels, same with 194 - 111
watch_face = img[37:111, 107:194]

# have to be the same size
img[0:74, 0:87] = watch_face

cv2.imshow ('image', img)

cv2.waitKey (0)
cv2.destroyAllWindows ()