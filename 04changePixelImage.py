import cv2 as cv

img = cv.imread('anh.jpg', 1)

width = len(img)
height = len(img[0])

for i in range(width):
    for j in range(height):
        if 100 < img[i][j][0] < 180:
            img[i][j] = [0, 0, 0]

cv.imwrite('anh-copy.jpg', img)
