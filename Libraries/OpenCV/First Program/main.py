import cv2
import numpy as np
import matplotlib.pyplot as plt

# Picture and Video analysis are pretty much identical in implementation
# Since a video is a series of frames you can analyze multiple still frames

# If no filter applied, reads in as color but removes the alpha channel
# degree of opaqueness, Greyscale is much further simplified
# cv2, it's bgr, not rgb, alpha it's bgra, takes more processing 
img = cv2.imread ('watch.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# works for video also
cv2.imshow ('image', img)

# Waits for any key to be pressed
cv2.waitKey (0)
cv2.destroyAllWindows ()

# can do color but cv2 does bgr, matplotlib does rgb
# so the colors get a little wrong
# plt.imshow (img, cmap='gray', interpolation='bicubic')
# plt.plot ( [50, 100], [80, 100], 'c', lineWidth=5)
# plt.show ()

cv2.imwrite('watchgray.png', img)