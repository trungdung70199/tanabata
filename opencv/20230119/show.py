import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('image.jpg')
while(True):
    d = d + 1
    
    M = np.float32([[1,0,50], [0,1,30]])

    img_moved = cv2.warpAffine(img, M, (640, 480))

    cv2.imshow('img_moved', img_moved)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

