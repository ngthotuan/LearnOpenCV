import cv2 as cv
import datetime

cap = cv.VideoCapture(0)  # camera

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        (height, width) = frame.shape[:2]
        label_width = 370
        frame = cv.putText(frame, time, (int((width - label_width) / 2),  height - 5),
                           cv.FONT_ITALIC, 1, (0, 255, 0), 1)
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
