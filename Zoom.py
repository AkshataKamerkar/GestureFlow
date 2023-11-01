
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
start_distance = None
cx, cy = 500, 500
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)  # To see hand on the img.
    img1 = cv2.imread('3.jpg')

    # To overlay the img on the screen we use slicing
    # To shift the img we hav to add the values throughtout
    # img[0:222, 0:222] og
    img[10:232, 10:232] = img1  # Shifted by 10

    if len(hands) == 2:
        # For gesture to see which fingers are up or down.
       #detector.fingersUp(hands[0]), detector.fingersUp(hands[1])

        # \ To let it knw tht it continues
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and\
                detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            hand1 = hands[0]
            hand2 = hands[1]

            lmList1 = hand1['lmList']
            lmList2 = hand2['lmList']

            # Point 8 is the tip of the index finger
            # To find the distance b/w the tips of the index fingers
            center_point1 = hand1['center']
            center_point2 = hand2['center']
            # Syntax = detector.findDistance( strt pt, end pt, var)
            p1 = lmList1[8]
            p2 = lmList2[8]

            if start_distance is None:

                length, info, img = detector.findDistance(center_point1, center_point2, img)
                start_distance = length

            length, info, img = detector.findDistance(center_point1, center_point2, img)
            scale = length - start_distance
            print(scale)

    else:
        start_distance = None

    try:

        h1, w1, _ = img1.shape
        print(h1,w1)
        newW, newH = ((h1+ scale)//2)*2, ((w1+ scale)//2)*2
        img1 = cv2.resize(img1, (newW,newH))

        img1[cy-h1:cy+h1, cx-w1:cx+w1]= img1

    except:
        pass


    cv2.imshow('Image', img)
    cv2.waitKey(1)






