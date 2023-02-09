import cv2

# Camera prepare
cam = cv2.VideoCapture(0)
# Take photo
ret, image = cam.read()
# Save
cv2.imshow('cam', image)
cv2.imwrite('image.png', image)
# End
cv2.waitKey(0)
cam.release()
cv2.destroyAllWindows()


