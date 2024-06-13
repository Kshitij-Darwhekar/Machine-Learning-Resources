import cv2
import numpy as np

img = cv2.imread('lena.jpg')
print(img.shape)
resizedimg = cv2.resize(img,(1024,1024))
print(resizedimg.shape)

imgCropped = img[0:256,0:256]
cv2.imshow('Original Image',img)
cv2.imshow('Resized Image',resizedimg)
cv2.imshow('Cropped Image',imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()