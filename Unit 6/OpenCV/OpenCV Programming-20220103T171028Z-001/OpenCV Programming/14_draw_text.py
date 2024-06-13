
import cv2
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))
	img = cv2.putText(frame,"GB Softronics",(400,height-10),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),5,cv2.LINE_AA)
	cv2.imshow('Frame',img)
	k=cv2.waitKey(1) & 0xFF
	if k==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()