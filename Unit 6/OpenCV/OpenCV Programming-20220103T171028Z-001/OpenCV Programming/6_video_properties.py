import numpy as np
import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))
print(width, height)
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('Frame',gray)
	k=cv2.waitKey(1) & 0xFF
	if k==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()