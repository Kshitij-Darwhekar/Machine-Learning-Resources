import numpy as np
import cv2

img = cv2.imread('lena.jpg')
height = img.shape[0]
print(height)
frame = np.ones((512,512,3),np.uint8)
frame=frame*255
##1. cv2.line(img,startingpoint,color,thickness,linetype
#cv2.line(img,(50,50),(200,300),(255,0,0),2,cv2.LINE_AA)
#cv2.line(img,(300,50),(50,300),(0,255,0),2,cv2.LINE_AA)

#2. cv2.rectangle(img,startingpoint,endpoint,thickness,linetype
#cv2.rectangle(img,(50,50),(200,200),(0,255,255),2)
#cv2.rectangle(img,(300,300),(400,400),(255,255,0),5)
#cv2.rectangle(img,(300,300),(400,400),(255,255,0),-1)
#thickness =-1 means filled rectangle

#3. cv2.circle(img,centerpt,radius,color,thickness,linetype)
#cv2.circle(img,(300,300),100,(255,0,255),2)
#cv2.circle(img,(200,200),150,(255,0,255),-1)

#4. cv2.ellipse(img,center,axes,angle,arcangle1,arcangle2,color,thickness)
#cv2.ellipse(img,(200,200),(200,50),360,360,0,(0,255,0),2)

#cv2.putText(img,TEXT,origin,FONT,FONTSIZE,COLOR,Thickness)
cv2.putText(img,"Lina",(100,50),cv2.FONT_ITALIC,2,(0,255,0),2)
#cv2.putText(img,"Lina",(250,height-30),cv2.FONT_ITALIC,2,(0,255,0),2)

#cv2.putText(frame,"Lina",(100,50),cv2.FONT_ITALIC,2,(0,255,0),2)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
