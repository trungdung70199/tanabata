import cv2

img = cv2.imread('image.png')

while(True):

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img_edge = cv2.Canny(img_gray, 180, 300)
    
    cv2.imshow('image_edge', img_edge)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
