import cv2
import imutils
from Human_Detection import Detector

cap = cv2.VideoCapture('sample.mp4')

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame,(980,498))
    frame = imutils.resize(frame, width=800)
    frame = Detector(frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()