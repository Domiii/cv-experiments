import cv2
import numpy as np

#filename = 'img/chessboard.webp'
filename = 'img/mario-1.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#gray = np.float32(gray)

kernel = np.ones((5,5),np.uint8)
dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('dst',dst)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()