import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


def drawCircles():
    img = np.zeros((512,512,3), np.uint8)
    cv.circle(img,(100,100), 63, (0,0,255), 1)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    # Display the resulting frame
    drawCircles()
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()