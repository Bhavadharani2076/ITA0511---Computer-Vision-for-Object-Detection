import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path='D:\Desktop\Bhavadharani-studies\Computer Vision\input.webp'
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(imgBlur,100,200)
imgdilate=cv2.dilate(imgCanny,kernel,iterations=10)
imgerode=cv2.erode(imgCanny,kernel,iterations=2)
cv2.imshow('Image to Dilated image',imgdilate)
cv2.waitKey(0)
