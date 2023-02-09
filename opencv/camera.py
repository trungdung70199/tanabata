import cv2

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

cv2.imshow('camera', frame)

cv2.imwrite('me.jpg', frame)

key = cv2.waitKey()
cam.release()

