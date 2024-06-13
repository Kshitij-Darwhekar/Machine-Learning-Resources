import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))
	pts = np.array([[100, 50], [200, 300], [700, 200], [500, 100]], np.int32)
	img = cv2.polylines(frame, [pts], True, (0, 255, 255), 3)
	cv2.imshow('Frame',img)
	k=cv2.waitKey(1) & 0xFF
	if k==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()