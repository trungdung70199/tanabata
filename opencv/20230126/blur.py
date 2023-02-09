import cv2

img = cv2.imread('image.png')
b = 5
img_blurred = cv2.blur(img, (b, b))

b = 10
img_blurred1 = cv2.blur(img, (b, b))

b = 20
img_blurred2 = cv2.blur(img, (b, b))

cv2.imshow('image_file', img)
cv2.imshow('image_blurred', img_blurred)
cv2.imshow('image_blurred1', img_blurred1)
cv2.imshow('image_blurred2', img_blurred2)

cv2.imwrite('image_blurred.png', img_blurred)
cv2.imwrite('image_blurred1.png', img_blurred1)
cv2.imwrite('image_blurred2.png', img_blurred2)

cv2.waitKey(0)
cv2.destroyAllWindows()
