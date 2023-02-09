import numpy as np
import cv2
# from cv2 import cvtColor

canvas = np.zeros((300, 300, 3), np.uint8)

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

ret, binary = cv2.threshold(gray, 177, 255, cv2.THRESH_BINARY)

coutour,_ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
border = cv2.drawContours(canvas, coutour, -1, (255, 0, 0, 3), thickness=3)

cv2.imshow('cameara', frame)
cv2.imshow('camera_gray', gray)
cv2.imshow('camera_bw', binary)
cv2.imshow('border', border)

cv2.imwrite('camera.jpg', frame)
cv2.imwrite('camera_gray.jpg', gray)
cv2.imwrite('camera_bw.jpg', binary)
cv2.imwrite('camera_border.jpg', border)

key = cv2.waitKey()
cam.release()


