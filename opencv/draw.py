import numpy as np
import cv2

# draw address 
canvas = np.zeros((300, 300, 3), np.uint8)

# draw
cv2.circle(canvas, (100, 100), 50, (0, 255, 0), thickness=-1)
cv2.rectangle(canvas, (200, 150), (150, 200), (0, 255, 0), thickness=-1)
cv2.imshow('canvas', canvas)

# Gray Scale
gray = cv2.cvtColor(canvas, cv2.COLOR_RGB2GRAY)
cv2.imshow('gray', gray)

#binnary
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)

#contour
contour,_ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
border = cv2.drawContours(canvas, contour, -1, (255, 0, 0, 3), thickness=3)
cv2.imshow('border', border)

cv2.imwrite('canvas.jpg', canvas)
cv2.imwrite('gray.jpg', gray)
cv2.imwrite('binary.jpg', binary)
cv2.imwrite('border.jpg', border)

key = cv2.waitKey()
cv2.destroyAllWindows()

