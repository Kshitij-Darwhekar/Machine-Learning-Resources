import cv2
import numpy as np

img = cv2.imread('cards.jpeg')
print(img.shape)
width,height = 400,600

pts1 = np.float32([[414,5],[699,168],[171,470],[460,635]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
outImg = cv2.warpPerspective(img,matrix,(width,height))

for x in range(0,4):
    p = int(pts1[x][0])
    q = int(pts1[x][1])
    cv2.circle(img,(p,q),8,(0,0,255),cv2.FILLED)

cv2.imshow('Original Image',img)
cv2.imshow('Output Image',outImg)
cv2.waitKey(0)
cv2.destroyAllWindows()