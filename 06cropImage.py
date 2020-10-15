import cv2 as cv

img = cv.imread('anh.jpg', 1)
subImg = img[190:400, 190:528]
subImg = subImg[:, :, 1]    # doi mau
cv.imshow('image', subImg)
cv.waitKey()
cv.destroyAllWindows()
