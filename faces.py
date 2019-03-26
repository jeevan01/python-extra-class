import cv2

face_cascade = cv2.CascadeClassifier("/home/jeevan/Desktop/python-extra-class/viseocode/opencv/data/haarcascades/haarcascade_frontalface_alt.xml")
video = cv2.VideoCapture(0)
while True :
    check,frame = video.read()
    print (frame)
    face = face_cascade.detectMultiScale(frame, scaleFactor =1.05 ,minNeighbors=5)
    print(face)
    for x,y,w,h in face:
        hello = cv2.rectangle(frame,(x,y),(x+w,y+h),(500,0,0),2) 
    cv2.imshow("GO GREEN",frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()

