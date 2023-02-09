import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('image.jpg')
# Làm ảnh chuyển sang màu đen trắng
img_gray = cv2.imread('image.jpg', 0)
# Làm size ảnh nhỏ đi
img_small= cv2.resize(img, (250, 180))
# Chuyển màu bgr
img_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Di chuyển vị trí của ảnh ảnh gốc sang phải
M = np.float32([[1,0,100], [0,1,100]])
img_moved = cv2.warpAffine(img, M, (640, 480))

def show_imgs(img01, img02):
    plt.subplot(121)
    plt.imshow(img01)
    plt.title('img01')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(122)
    plt.imshow(img02)
    plt.title('img02')
    plt.xticks([])
    plt.yticks([])

    show_imgs(img, img_gray)

# Hiện ảnh gốc
cv2.imshow('image', img)
# Hiện ảnh đen trắng
cv2.imshow('image_gray', img_gray)
# Hiện ảnh với size nhỏ 
cv2.imshow('image_small', img_small)
# Hiện ảnh màu brg
cv2.imshow('image_bgr', img_bgr)
# Hiện ảnh sau khi thay đổi vị trí
cv2.imshow('img_moved', img_moved)

# Lưu ảnh
cv2.imwrite('image_gray.jpg', img_gray)
cv2.imwrite('image_bgr.jpg', img_bgr)
cv2.imwrite('image_small.jpg', img_small)
cv2.imwrite('image_moved.jpg', img_moved)

cv2.waitKey(0)

cv2.destroyAllWindows()


