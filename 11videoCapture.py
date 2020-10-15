import cv2 as cv

# cap = cv.VideoCapture("file")
cap = cv.VideoCapture(0)  # camera
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv.imshow('frame', frame)
        out.write(frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
