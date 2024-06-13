
import cv2
cap = cv2.VideoCapture('vtest.avi')
while True:
	ret, frame = cap.read()
	cv2.imshow('Frame',frame)
	k=cv2.waitKey(1) & 0xFF
	if k==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()