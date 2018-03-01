import numpy as np
import cv2

cap = cv2.VideoCapture (0)

while True :
    # underscore means it's a value that returned from a function that needs to be there to be
    # unpacked to, but we don't care about it
    _, frame = cap.read ()
    # hue, saturation, and value, another way to define colours
    # the hue is the "color" value, how much of that color is in existence
    # saturation is the intensity, each of those is independant
    hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array ([150, 150, 50])
    upper_red = np.array ([180, 255, 150])

    mask = cv2.inRange (hsv, lower_red, upper_red)
    
    # where in there is something in the frame and the mask is true
    res = cv2.bitwise_and (frame, frame, mask=mask)

    # averaging the pixels, divide by 15 * 15, the numbers on the left
    kernel = np.ones ((15, 15), np.float32) / 255
    smoothed = cv2.filter2D (res, -1, kernel)

    blur = cv2.GaussianBlur (res, (15, 15), 0)
    median = cv2.medianBlur (res, 15)
    bilateral = cv2.bilateralFilter (res, 15, 75, 75)

    cv2.imshow ('frame', frame)
    # cv2.imshow ('mask', mask)
    cv2.imshow ('res', res)
    # cv2.imshow ('smooted', smoothed)
    # cv2.imshow ('blur', blur)
    # cv2.imshow ('median', median)
    cv2.imshow ('bilateral', bilateral)

    k = cv2.waitKey (5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows ()
cap.release ()