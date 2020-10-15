import cv2 as cv

img = cv.imread('anh.jpg', 1)
cv.imshow('image', img)

cv.waitKey()
cv.destroyAllWindows()
