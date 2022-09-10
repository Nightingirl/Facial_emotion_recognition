#Importing OpenCV 
import cv2 
#Importing HARR CASCADE XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


#Capture Video from web cam hence (0) or else add your own media file
cap = cv2.VideoCapture(0)

#Creating a loop to capture each frame of the video in the name of Img
while True:
    _,img = cap.read()

    #Converting to grey scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Allowing multiple face detection
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)

    #Creating Rectangle around face
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 250), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #Displaying the image 
    cv2.imshow('Detected Face Image',  img)

    #Waiting for escape key for image to close adding the break statement to end the face detection screen
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#Real-time releasing the captired frames
cap.release()

# import numpy as np
# import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# img = cv2.VideoCapture()
# while(True):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray)
#         for (ex,ey,ew,eh) in eyes:
#             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# # cv2.imshow('img',img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()