import numpy as np
import cv2

img = cv2.imread ('watch.jpg', cv2.IMREAD_COLOR)

# (where to draw line, where does the line start, where does the line end, color, line width in pixels)
# in computers, adding more green makes it brighter, in real life makes it darker, bgr
cv2.line (img, (0,0), (150, 150), (255, 255, 255), 15)

# (where to draw rectangle, top left coordinate, bottom right coordinate, color, width in pixels)
cv2.rectangle (img, (15, 25), (200, 150), (0, 255, 0), 5)

# (where to draw circle, where is the center of the circle, what is the radius of the circle, color, width)
# using -1 in the last parameter fills in the circle
cv2.circle (img, (100, 63), 55, (0, 0, 255), -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)

# reshapes the array to a 1 by 2, which is already the case, due to the opencv docs, this is recomended
# pts = pts.reshape((-1, 1, 2))

# true specifys if we want to connect the final point to the first point
cv2.polylines (img, [pts], True, (0, 255, 255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX

# text to show, where to start text, font to use, size, color, thickness of letters, anti-aliasing
# can use decimals for font size
cv2.putText (img, 'OpenCV tuts!', (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)

cv2.imshow ('image', img)

cv2.waitKey (0)
cv2.destroyAllWindows ()
