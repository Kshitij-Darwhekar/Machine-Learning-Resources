import cv2
import numpy as np
ObjectType = None
def getCountours(img):
    countours,hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        peri = cv2.arcLength(cnt,True)
        print(peri)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        print(len(approx))
        objcor = len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        ObjectType = None
        if objcor == 3: ObjectType = "Tri"
        elif objcor == 4:
            aspRatio = w/float(h)
            if aspRatio > 0.95 and aspRatio < 1.05: ObjectType = "Square"
            else: ObjectType = "Rectangle"
        elif objcor >4:
            ObjectType = "Circle"
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(imgContour,ObjectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

img = cv2.imread('shapes.png')
imgContour = img
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getCountours(imgCanny)
cv2.imshow('Original',img)
cv2.imshow('Gray Image',imgGray)
cv2.imshow('Blur Image',imgBlur)
cv2.imshow('Output',imgContour)
cv2.imshow('Canny Image',imgCanny)
#cv2.imshow(('Output',imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()
