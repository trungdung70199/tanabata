import cv2
import numpy as np
# image prepare
img = cv2.imread('image.png')
cv2.imshow('image_file', img)
# Big -> Small
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 0, 0.5)
img_rotated = cv2.warpAffine(img, M, (cols, rows))
# Move Small image 
M = np.float32([[1, 0, 50], [0, 1, 30]])
img_moved = cv2.warpAffine(img_rotated, M, (cols, rows))
# Sendan data prepare
pts1 = np.float32([[40, 40], [400, 50], [10, 220]])
pts2 = np.float32([[20, 100], [400, 50], [100, 270]])
M = cv2.getAffineTransform(pts1,pts2)
rows, cols = img.shape[:2]
# Sendan
img_sendan = cv2.warpAffine(img, M, (cols, rows))
# Sendan show image
cv2.imshow('img_sendan', img_sendan)
cv2.imwrite('img_sendan.png', img_sendan)
# End
cv2.waitKey(0)
cv2.destroyAllWindows()

