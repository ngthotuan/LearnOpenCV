import cv2 as cv

img = cv.imread('anh.jpg', 1)
cv.line(img, (0, 0), (300, 300), (0, 0, 0), 10)
cv.imwrite('anh-copy.jpg', img)

cv.destroyAllWindows()
