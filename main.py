import cv2
import serialModule
import HandTrackingModule

cap= cv2.VideoCapture(0) #0 =laptop camera capture video
detector = HandTrackingModule.HandDetector(maxHands=1) #this project detect one hand only
mySerial= serialModule.SerialObject('COM6',9600,1)

while True:
    success, img = cap.read() #read the image of the camera = img
    hands,img = detector.findHands(img)
    #hand =>(lmlist,bbox,center,type)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        print(fingers1)
        mySerial.sendData(fingers1)

    cv2.imshow("image", img) #video window's name
    cv2.waitKey(1) #delay time