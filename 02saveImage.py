import cv2 as cv

img = cv.imread('anh.jpg')
cv.imwrite('anh-copy.jpg', img)
