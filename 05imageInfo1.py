import cv2 as cv

img = cv.imread('anh.jpg', 1)


cv.imwrite('anh-copy.jpg', img)
