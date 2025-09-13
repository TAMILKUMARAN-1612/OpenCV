import cv2
cap=cv2.VideoCapture('movies.mp4')  
forcc= cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',forcc,30.0,(500,500))  
while cap.isOpened():
    ret,frame=cap.read()
    frame=cv2.resize(frame,(500,500))
    if ret==True:
        out.write(frame)  
        cv2.imshow('Output',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()