import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread ('opencv-python-foreground-extraction-tutorial.jpg')
mask = np.zeros (img.shape[:2], np.uint8)

bgdModel = np.zeros ((1, 65), np.float64)
fgdModel = np.zeros ((1, 65), np.float64)

# only need to change rectangle for new images
rect = (161, 79, 150, 150)

cv2.grabCut (img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# other options 1, 3
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype ('uint8')
img = img * mask2[:,:,np.newaxis]
plt.imshow (img)
plt.colorbar ()
plt.show ()