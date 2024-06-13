import cv2
import numpy as np

def getMouseClickPoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

img  = cv2.imread('cards.jpeg')
cv2.imshow('Original Image',img)
cv2.setMouseCallback('Original Image',getMouseClickPoints)
cv2.waitKey(0)
cv2.destroyAllWindows()