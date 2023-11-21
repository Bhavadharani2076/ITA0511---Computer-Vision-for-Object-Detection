import cv2
import numpy as np s
cap=cv2.VideoCapture('D:\Desktop\Bhavadharani-studies\Computer Vision\input.mp4')
if(cap.isOpened()==False):
    print("Error in Opening video file")
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        cv2.imshow('Frame',frame)
        if cv2.waitKey(250) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
