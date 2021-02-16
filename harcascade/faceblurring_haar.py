import cv2
# Read Input Image
image = cv2.imread('../testimage1')
# Haar Cascade for Face Detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# Detect the faces in Images
faces = face_cascade.detectMultiScale(image,1.3,5)

for (x,y,w,h) in faces:
    # Enclose the detected faces inside a rectangular box
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
    # Select the detected face area
    face_color = image[y:y + h, x:x + w]
    # Blur the detected face
    blur = cv2.GaussianBlur(face_color, (51, 51), 0)
    image[y:y + h, x:x + w] = blur

# Display the Blurred Faces Image
cv2.imshow('Face Detected Blurred Image',image)
# Hold output for 20 sec
cv2.waitKey(20000)
cv2.destroyAllWindows()