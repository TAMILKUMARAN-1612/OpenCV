import cv2
import numpy as np
img=cv2.imread('len.jpg')
img=np.zeros((500,500,3),dtype="uint8")
cv2.rectangle(img,(100,100),(300,300),(0,255,0),3)
cv2.circle(img,(400,400),50,(255,0,0),5)    
cv2.line(img,(0,0),(500,500),(0,0,255),2)
ptr=np.array([[100,50],[200,50],[50,200],[300,200]],np.int32)
cv2.polylines(img,[ptr],False,(0,255,255),3)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'TAMIL',(200,200),font,1,(255,255,0),2,cv2.LINE_AA)
cv2.imshow('shapes',img)        
cv2.waitKey(0)  
cv2.destroyAllWindows()