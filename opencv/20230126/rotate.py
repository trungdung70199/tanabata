import cv2
# image prepare
img = cv2.imread('image.png')
cv2.imshow('image_file', img)
# image of size
rows, cols = img.shape[:2]

print(rows)
print(cols)
d = 0
while(True):
    d = d + 1
    # To make rotate data
    M = cv2.getRotationMatrix2D((cols/2, rows/2), d, -60, 1.0)
    # -60: Degree rotate
    # 1.0: Big - Small
    # Rotate
    img_rotated = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('img_rotated', img_rotated)
    # (q) 押すと終わり
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# End
cv2.destroyAllWindows()

