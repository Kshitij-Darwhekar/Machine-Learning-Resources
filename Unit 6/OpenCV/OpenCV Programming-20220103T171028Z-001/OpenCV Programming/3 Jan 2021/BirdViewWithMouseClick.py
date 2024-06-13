import cv2
import numpy as np

circles = np.zeros((4,2),np.int)
counter = 0

def getMouseClickPoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(x,y)
        circles[counter] = x,y
        counter = counter + 1
        print(circles)

while True:
    img = cv2.imread('pancard.jpeg')
    if counter == 4:
        width,height = 300,200
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        outImg = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow('Output Image', outImg)

    for x in range(0,4):
        p = int(circles[x][0])
        q = int(circles[x][1])
        cv2.circle(img,(p,q),8,(0,0,255),cv2.FILLED)

    cv2.imshow('Original Image',img)
    cv2.setMouseCallback('Original Image',getMouseClickPoints)

    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()