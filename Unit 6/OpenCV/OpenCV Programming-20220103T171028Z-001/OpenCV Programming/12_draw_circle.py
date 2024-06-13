
import cv2
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))
	img = cv2.circle(frame,(300,300),100,(0,255,255),-1)
	cv2.imshow('Frame',img)
	k=cv2.waitKey(1) & 0xFF
	if k==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()