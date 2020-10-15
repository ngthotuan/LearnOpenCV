import cv2 as cv


def printScreenInfo(capture):
    print('Width: {} px, Height: {} px'.format(
        capture.get(cv.CAP_PROP_FRAME_WIDTH),
        capture.get(cv.CAP_PROP_FRAME_HEIGHT)
    ))


cap = cv.VideoCapture(0)  # camera
printScreenInfo(cap)

cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
printScreenInfo(cap)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
