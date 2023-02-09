import cv2
import numpy as np

cam = cv2.VideoCapture(1)

ret, frame = cam.read()

frame_width = int(cam.get(3))
frame_height = int(cam.get(4))
video_in = cv2.VideoWriter_fourcc(*'XVID')
video_out = cv2.VideoWriter('cap_video.cvi', video_in, 30, (frame_width, frame_height))
# img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# img_edge = cv2.Canny(img_gray, 180, 300)

# cv2.imshow("img_gray", img_gray)
# cv2.imshow("img_edge", img_edge)

# cv2.imwrite("img_gray.png", img_gray)
# cv2.imwrite("img_edge.png", img_edge)

while(True):
    ret, frame =cam.read()
    if ret == True:
        video_out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitkey(1) & 0xFF == ord('q'):
            break
    else:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

