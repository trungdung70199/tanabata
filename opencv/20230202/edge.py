import cv2

img = cv2.imread('image.png')

cv2.imshow('image', img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img_gray', img_gray)

img_edge = cv2.Canny(img_gray, 180, 300)

cv2.imshow('image_edge', img_edge)

cv2.waitKey(0)

cv2.destroyAllWindows()
