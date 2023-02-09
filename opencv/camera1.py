# color scale (gray)

import cv2

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

cv2.imshow('camera', gray_frame)

cv2.imwrite('gray.jpg', gray_frame)

key = cv2.waitKey()
cam.release()

