import cv2

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('face.xml')

while True:
    ret, img = capture.read()
    
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=3, minSize=(28,28))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255))
        
    cv2.imshow('Test', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()