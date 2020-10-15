import cv2 as cv
import numpy as np

# img = cv.imread('anh.jpg')
img = np.zeros([512, 512, 4], np.uint8)

img = cv.line(img, (0, 0), (300, 300), (141, 46, 153), 10)

img = cv.arrowedLine(img, (0, 200), (300, 300), (209, 207, 86), 5)

img = cv.rectangle(img, (50, 50), (200, 200), (204, 45, 61), -1)

img = cv.circle(img, (500, 500), 50, (214, 17, 207), -1)

img = cv.putText(img, "Hello world", (000, 400), cv.FONT_HERSHEY_DUPLEX, 2, (101, 214, 139), 5)

cv.imshow('hinh anh', img)

cv.waitKey(0)
cv.destroyAllWindows()
