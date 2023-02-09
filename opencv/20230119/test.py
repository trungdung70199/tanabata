import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

camera = cv2.VideoCapture(0)
ret, frame = camera.read()

cv2.imshow('camera', frame)
cv2.imwrite('image.jpg', frame)
cv2.waitKey(0)
camera.release()
cv2.destroyAllWindows()


