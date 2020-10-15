import cv2 as cv

img = cv.imread('anh.jpg', 1)
subImg1 = img[200:400, 200:400]
subImg2 = img[100:300, 300:500]
result = cv.add(subImg1, subImg2)
cv.imshow('image', subImg1)
cv.waitKey(0)
cv.imshow('image', subImg2)
cv.waitKey(0)
cv.imshow('image', result)
cv.waitKey()
cv.destroyAllWindows()
