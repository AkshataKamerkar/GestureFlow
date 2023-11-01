import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 720)

detector = HandDetector(detectionCon= 0.8)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, flipType= False)
    img1= cv2.imread('3.jpg')

    if len(hands)==2:
        detector.fingersUp(hands[0]), detector.fingersUp(hands[1])
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and\
            detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            print('Set')
            lmlist1 = hands[0]['lmList']
            lmlist2 = hands[1]['lmList']


            length, info, img = detector.findDistance(lmlist1[0], lmlist2[1], img)
            print(length)


    img[10:232, 10:232] = img1
    cv2.imshow('Img', img)
    cv2.waitKey(1)








