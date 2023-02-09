import cv2

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

cv2.imshow('cam', frame)

cv2.imwrite('image.png', frame)

cv2.waitKey(0)

cam.release()

cv2.destroyAllWindows()
