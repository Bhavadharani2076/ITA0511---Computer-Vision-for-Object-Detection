import cv2
import numpy as np
img = cv2.imread("D:\Desktop\Bhavadharani-studies\Computer Vision\input.webp")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gradient_x=cv2.Sobel(gray,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=3)
gradient_y=cv2.Sobel(gray,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=3)
gradient_magnitude=np.sqrt(gradient_x**2+gradient_y**2)
mask=(gradient_magnitude>30).astype(np.uint8)
sharpened=cv2.multiply(img,cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR))
cv2.imshow('Output',sharpened)
cv2.waitKey(0)
