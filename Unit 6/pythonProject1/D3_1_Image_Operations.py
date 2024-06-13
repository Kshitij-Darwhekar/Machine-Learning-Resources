import cv2
import numpy as np

img = cv2.imread('lena.jpg')
kernel = np.ones((5,5),np.uint8)

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurimg = cv2.GaussianBlur(grayimg,(7,7),0)
#blurimg = cv2.medianBlur(grayimg,5)
imgCanny = cv2.Canny(grayimg,100,200,L2gradient=True)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow('Color Image',img)
cv2.imshow('Gray Image',grayimg)
cv2.imshow('Blur Image',blurimg)
cv2.imshow('Canny Image',imgCanny)
cv2.imshow('Dilation Image',imgDilation)
cv2.imshow('Eroded Image',imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()