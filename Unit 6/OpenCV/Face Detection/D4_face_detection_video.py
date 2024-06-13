import cv2
import numpy as np
import face_recognition

cap = cv2.VideoCapture(0)

imgElon = face_recognition.load_image_file('GaneshAttarde2.jpeg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

#imgTest = face_recognition.load_image_file('GaneshAttarde3.jpeg')
#imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
#cv2.rectangle(imgElon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,255,0),2)

while cap.isOpened():
    ret,frame = cap.read()
    imgTest = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    facelocTest = face_recognition.face_locations(imgTest)[0]
    encodeTest = face_recognition.face_encodings(imgTest)[0]
    cv2.rectangle(frame,(facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(255,255,0),2)

    results = face_recognition.compare_faces([encodeElon],encodeTest)
    faceDis = face_recognition.face_distance([encodeElon],encodeTest)

    print(results)
    print(faceDis)
    if(results[0] ==  True):
        cv2.putText(frame, 'Ganesh Attarde',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow('Video',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()