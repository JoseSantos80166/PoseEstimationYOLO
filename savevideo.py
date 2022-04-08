import numpy as np
import cv2
from scipy import ndimage

width, height = 400, 400
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))



# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (width,height))
#out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
i=0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # write the flipped frame
        frame=ndimage.rotate(frame, i,reshape=False)
        out.write(frame)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('u'):
            i=i+45
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

#python train.py --img 415 --batch 16 --epochs 30 --data data.yaml --weights yolov5m.pt --cache --hyp hyp.scratch-med.yaml --freeze 9