import cv2

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)

#img = cv2.imread('lena.jpg')
#imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

while cap.isOpened():
    ret , frame = cap.read()
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Result',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()