import numpy as np
import cv2

img = cv2.imread ('opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
gray = np.float32 (gray)

# img, how many are we willing to find up to, 0.01 is quality, minimum distance between corners
corners = cv2.goodFeaturesToTrack (gray, 100, 0.01, 10)
corners = np.int0 (corners)

for corner in corners :
    x, y = corner.ravel ()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow ('corners', img)

cv2.waitKey (0)
cv2.destroyAllWindows ()