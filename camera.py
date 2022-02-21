import time
import cv2
import uuid


cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

count = 1200

while True:
    ret,frame = cap.read()
    count += 1
    imgname = './dataset/%d.jpg' % count
    count += 1
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    time.sleep(1)

cap.release()
cap.destroyAllWindows()