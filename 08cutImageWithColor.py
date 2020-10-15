import cv2 as cv
import numpy as np


img = cv.imread('image.jpg', 1)

pixelBGR = img[109, 586]
pixelHSV = cv.cvtColor(np.uint8([[pixelBGR]]), cv.COLOR_BGR2HSV)
epsilon = 0
lower = np.subtract(pixelHSV, epsilon)
upper = np.add(pixelHSV, epsilon)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv, lower[0][0], upper[0][0])
result = cv.bitwise_and(img, img, mask=mask)
cv.imshow('image', result)

# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         if not np.array_equal(pixelBGR, img[i, j]):
#             img[i, j] = [0, 0, 0]
# cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows()



