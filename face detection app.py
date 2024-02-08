import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


video = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = video.read()
    if not ret:
        break  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces and label them as "batman"
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
        #u can replace "the choose ur name" to any sentance u want 
        cv2.putText(frame, 'choose ur name ', (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 255), 2)

    cv2.imshow("Face Detection", frame)

    # Press 'q' to exit the loop
    key = cv2.waitKey(1)
    if key == ord('m'):
        break

video.release()
cv2.destroyAllWindows()
