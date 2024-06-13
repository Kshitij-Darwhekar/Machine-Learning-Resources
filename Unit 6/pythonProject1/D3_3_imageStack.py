import cv2
import numpy as np
img = cv2.imread('lena.jpg')
img1 = cv2.imread('butterfly.jpg')
img1 = cv2.resize(img1,(img.shape[0],img.shape[1]))

imgHor = np.hstack((img,img1,img))
imgVer = np.vstack((img,img1))

cv2.imshow('Horizantal Image',imgHor)
cv2.imshow('Vertical Image',imgVer)
cv2.waitKey(0)
cv2.destroyAllWindows()