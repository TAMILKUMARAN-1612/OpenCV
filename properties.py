import cv2
img=cv2.imread('len.jpg')
shape=img.shape
height=shape[0]
width=shape[1]
channel=shape[2]
size1=img.size

print("Height of image:",height)
print("Width of image:",width)
print("Number of channels:",channel)
print("Size of image:",size1)