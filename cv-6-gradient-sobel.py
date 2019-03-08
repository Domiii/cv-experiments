import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/sudoku.jpg')

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
sobely8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
# abs_sobel64f = np.absolute(sobelx64f)
# sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel x'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobely8u,cmap = 'gray')
plt.title('Sobel y'), plt.xticks([]), plt.yticks([])

plt.show()