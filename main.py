import cv2

import HandTrackingModule
import PoseModule

cap= cv2.VideoCapture(0) #0 =laptop camera capture video
detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.7)
Pose = PoseModule.PoseDetector


while True:
    success, img = cap.read()
    cv2.imshow("image", img)  # video window's name
    hand = detector.findHands(img) #use the cvzone to find hand
    lmList, bbox = Pose.findPosition(img)


    cv2.waitKey(1) #delay time