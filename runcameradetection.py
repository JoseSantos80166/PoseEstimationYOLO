# Loading modules
import cv2
import numpy as np 
from scipy import ndimage
from detect import run


video=cv2.VideoCapture(0)
s=True

while True:
    check, frame= video.read()

    # Fliping the image as said in question
    flip = cv2.flip(frame,1)

    # Rotate frame
    rotate=ndimage.rotate(flip, 45)
    # Displaying the video feed
    if s==False:
        run('best.pt',flip)
        #cv2.imshow("Video Feed ",rotate)
        key=cv2.waitKey(1)
    else:
        run('best.pt',rotate)
        #cv2.imshow("Video Feed ",flip)
        key=cv2.waitKey(1)

    if key==ord('q'):
        break

    if key==ord('s'):
        if s == True:
            s = False
        else:
            s = True 
        


video.release()
cv2.destroyAllWindows