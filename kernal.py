import cv2
import numpy as np
img=cv2.imread('len.jpg')
resize=cv2.resize(img,(500,500))
kernel=np.ones((5,5),np.uint8)
erode=cv2.morphologyEx(resize,cv2.MORPH_OPEN,kernel)
dilate=cv2.morphologyEx(resize,cv2.MORPH_CLOSE,kernel)
cv2.imshow('original',resize)
cv2.imshow('eroded',erode)
cv2.imshow('dilated',dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()