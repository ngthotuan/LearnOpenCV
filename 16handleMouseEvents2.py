import cv2 as cv
import numpy as np


def mouse_click(event, x, y, flags, param):
    cv.imshow('image', img)
    if event == cv.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv.circle(img, (x, y), 5, (0, 0, 255), -1, 10)
        if len(points) >= 2:
            cv.line(img, points[-2], points[-1], (255, 0, 0), 5)
        cv.imshow('image', img)
    if event == cv.EVENT_RBUTTONDOWN:
        colorPicker = np.zeros(img.shape, np.uint8)
        colorPicker[:] = img[y, x]
        cv.imshow('color', colorPicker)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread('anh.jpg')
points = []
cv.imshow('image', img)
cv.setMouseCallback('image', mouse_click)

cv.waitKey()
cv.destroyAllWindows()
