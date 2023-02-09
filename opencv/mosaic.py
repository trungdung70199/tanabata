import cv2
def mosaic(img, alpha):
    w = img.shape[1]
    h = img.shape[0]
    img = cv2.resize(img, (int(w*alpha), int(h*alpha)))
    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
    return img
  

face_cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)
  

cam = cv2.VideoCapture(0)
ret, src = cam.read()
#cv2.imshow('face', src)
#cv2.waitKey()
#cam.release()
  

src_gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
  
  #cv2.imshow('face_gray', src_gray)
  #cv2.waitKey()
  #cam.release()
  
  # 顔をさがす
faces = face_cascade.detectMultiScale(src_gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
print(faces)
  
  

for (x, y, w, h) in faces:
    cv2.rectangle(src, (x, y), (x + w, y+h), (0,0,300), 4)
    src[y:y+h, x:x+w] = mosaic(src[y:y+h, x:x+w], 0.05)
      
      

cv2.imshow('face', src)
cv2.waitKey()
cv2.imwrite('face_mosaic.jpg', src)