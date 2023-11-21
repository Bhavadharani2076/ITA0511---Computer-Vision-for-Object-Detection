import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
path='D:\Desktop\Bhavadharani-studies\Computer Vision\input.webp'
img=cv2.imread(path)
img=cv2.resize(img,(1000,1000))
cv2.imshow('Image',img)
cv2.waitKey(0)
