import cv2
import numpy as np

# 0 means first webcam in the system, 1 is second
# you can also do VideoCapture ('output.avi') to get a video
cap = cv2.VideoCapture (0)

# codec to use, xvid should work for all operating systems, maybe not mac, have to use VLC
fourcc = cv2.VideoWriter_fourcc (*'XVID')
out = cv2.VideoWriter ('output.avi', fourcc, 20.0, (640, 480))

while True :brew tap homebrew/science
brew install --with-tbb opencv
    # true and false and the frame
    ret, frame = cap.read ()

    # convert color to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # write frames to the out
    out.write (frame)

    cv2.imshow ('frame', frame)
    cv2.imshow ('gray', gray)

    if cv2.waitKey (1) & 0xFF == ord('q') :
        break

# releases the capture, the camera will be released, will get error if using camera while in use
cap.release ()
# save the out file
out.release ()
cv2.destroyAllWindows ()