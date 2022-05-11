import cv2
from scipy import ndimage

cap = cv2.VideoCapture(0)
mode=2 #mode 1 = Normal mode, mode 2 = Rotated mode
# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    
    if mode==1:
        cv2.imshow('Input', frame) #Original version
    elif mode==2:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rotate=ndimage.rotate(gray, angle=45, reshape=False)
        cv2.imshow('Input', rotate) #Rotated version (better)
    elif mode==3:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Input', gray) #Rotated version (very slow)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

#*
