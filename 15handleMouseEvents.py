import cv2 as cv
import numpy as np


def mouse_click(event, x, y, flags, param):
    cv.imshow('image', img)
    if event == cv.EVENT_LBUTTONDOWN:
        cv.putText(img, '({}, {})'.format(x, y), (x, y),
                   cv.FONT_ITALIC, .5, (255, 0, 0))
        cv.imshow('image', img)
    if event == cv.EVENT_RBUTTONDOWN:
        cv.putText(img, '({d[0]}, {d[1]}, {d[2]})'.format(d=np.array(img[y, x])), (x, y),
                   cv.FONT_ITALIC, .5, (255, 0, 0))
        cv.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread('anh.jpg')
cv.imshow('image', img)
cv.setMouseCallback('image', mouse_click)

cv.waitKey()
cv.destroyAllWindows()
