# Loading modules
import cv2
import numpy as np 
from scipy import ndimage


video=cv2.VideoCapture(0)
s=True

while True:
    check, frame= video.read()

    # Fliping the image as said in question

    # Rotate frame
    rotate=ndimage.rotate(frame, 45)
    # Displaying the video feed
    if s==False:
        cv2.imshow("Video Feed ",rotate)
        key=cv2.waitKey(1)
    else:
        cv2.imshow("Video Feed ",frame)
        key=cv2.waitKey(1)

    if key==ord('q'):
        break

    if key==ord('s'):
        rotate=ndimage.rotate(frame, -45)
        


video.release()
cv2.destroyAllWindows