import cv2

face_cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

eye_cascade_path = 'haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

cam = cv2.VideoCapture(0)
ret, src = cam.read()
cv2.imshow('face', src)

src_gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

# cv2.imshow('face_gray', src_gray)
# cv2.waitKey()
# cam.release()

faces = face_cascade.detectMultiScale(src_gray)
# eyes = eye_cascade.detectMultiScale(eye_gray)
print(faces)
# print(eyes)

# for (x, y, w, h) in faces:
#     cv2.rectangle(src, (x, y), (x + w, y+h), (0,0,300), 4)

for x, y, w, h in faces:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face = src[y: y + h, x: x + w]
    face_gray = src_gray[y: y + h, x: x + w]
    eyes = eye_cascade.detectMultiScale(face_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('face', src)
cv2.waitKey()

