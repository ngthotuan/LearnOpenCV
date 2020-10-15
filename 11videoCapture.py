import cv2 as cv

# cap = cv.VideoCapture("file")
cap = cv.VideoCapture(0)  # camera
fourcc = cv.VideoWriter_fourcc(*'MPEG')
out = cv.VideoWriter('output.mp4', fourcc, 60.0, (1280, 720))
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
