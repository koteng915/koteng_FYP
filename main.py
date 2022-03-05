import cv2
import cvzone

cap= cv2.VideoCapture(0) #0 =laptop camera capture video

while True:
    success, img = cap.read()

    cv2.imshow("image", img) #video window's name
    cv2.waitKey(1) #delay time