import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()


    # For getting img + draw : new variable name, screen/img name[where the drawings are to been shown] = detector.findHands(screen/img name
    #hands, img = detector.findHands(img)

    # For no draw : new variable name = detector.findHands(screen/img name, draw= False)
    #hands = detector.findHands(img, draw=False)



    # cv2.flip( var, 1) + flipType=False == Perfectly flipped img.

    # To flip the img 1= horizontal , 0= vertical ; but here right becomes left and vice versa.
    img = cv2.flip(img, 1)

    # If the img is flipped i.e if right is left and vice versa :
    hands, img = detector.findHands(img, flipType=False)


    #hand contains a dict( lmList, bbox, center, type)
    # hands = hand1 + hand2 i.e two dicts
    # To acess one hand
    if hands:
        # Hand1
        # To extract the info from the dict:
        hand1 = hands[0]
        lmList1 = hand1['lmList'] #list of 21 landmarks points
        bbox1 = hand1['bbox']  #bounding box info {x,y,w,h}
        centerPoint1 = hand1['center'] #center of the hand {cx,cy}
        handType1 = hand1['type'] #left or right
        #print(handType1)
        #print(len(handType1))


        #if len(handType1) == 5:
            # To draw a circle at centre : cv2.circle( screen/img name, co-ordinates, thickness, color)
            #cv2.circle(img, centerPoint1, 12, (0, 0, 255), cv2.FILLED)

        #else:
            #cv2.circle(img, centerPoint1, 12, (30, 50, 5), cv2.FILLED)





        # To access two hands:
        if len(hands)==2:
            hand2 = hands[1]
            lmList2 = hand2['lmList']  # list of 21 landmarks points
            bbox2 = hand2['bbox']  # bounding box info {x,y,w,h}
            centerPoint2 = hand2['center']  # center of the hand {cx,cy}
            handType2 = hand2['type']  # left or right
            finger1 = detector.fingersUp(hand1)
            finger2 = detector.fingersUp(hand2)
            #print(finger2, finger1)
            x1= lmList1[20]
            x2= lmList2[20]

        #It will give an error coz fingers2 is defined inside the loop and we are printing it outside the loop but fingers1 me error nhi aayega  ?
        #print(finger2, finger1)  #Test the looping stuffs
# Loop ke aandar wali chali stuffs loop ke bahara wale stuffs ko access kr sakte he but loop ke bahar wale stuffs loop ke aandar wale stuffs ko access nhi kr sakte

            # To find the distance between two points
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)
            #print(x1, x2) #landmarks have 3 co-ordinates thts why it is showing an valueError while as centerPoints have only 2 co-ordinates.
            #print(centerPoint2,centerPoint1)
            print(length)

























    cv2.imshow('IMG', img)
    cv2.waitKey(1)
