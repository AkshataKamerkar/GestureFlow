import numpy as np
import cv2
import os



from cvzone.HandTrackingModule import HandDetector

# Parameters
width, height = 1280, 720
FolderPath = 'Test'
hs, ws = 120, 213

# Cam_Setup

cam = cv2.VideoCapture(0)
cam.set(3, ws)
cam.set(4, hs)

# Presentation_Slides
# sorted_fuction
pathSlides = sorted(os.listdir(FolderPath), key=len)
# print(pathSlides)

# Variables
SlideNum = 1
gestureThreshold = 300
button_pressed = False
button_counter = 0
button_delay = 30
annotations = [[]]
annotation_number = -1
annotation_start = False

# Hand_Detector
# Here, detectionCon = the code will run if it is 80% of the oblect being a hand.
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cam.read()
    # To flip the img 1= horizontal , 0= vertical ; but here right becomes left and vice versa.
    img = cv2.flip(img, 1)
    img = cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (100, 255, 205), 10)

    pathFullSlides = os.path.join(FolderPath, pathSlides[SlideNum])
    SlideCurrent = cv2.imread(pathFullSlides)

# cv2.flip( var, 1) + flipType = False == Perfectly flipped img.
    hands, img = detector.findHands(img, flipType=False)  # flipType = Flase it will nt flip the img. right will remain right and vice versa.

    if hands and button_pressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        #land_mark_list
        lm_list = hand['lmList']


        # Constrain Region for pointer
        #np.interp(variable[fitting-size],[actual_size])
        x_val = int(np.interp(lm_list[8][0], [0, width//4], [0, width]))
        y_val = int(np.interp(lm_list[8][1], [0, height-500], [0, height]))
        index_finger = x_val, y_val

        if cy <= gestureThreshold:  #If hand is above the gestureThreshold
            #Gesture-0 Left
            if fingers == [1, 0, 0, 0, 0]:
                print('Left')

                if SlideNum > 0:
                    button_pressed = True
                    annotations = [[]]
                    annotation_number = -1
                    annotation_start = False

                    SlideNum -= 1

            # Gesture-1 Right
            if fingers == [0, 0, 0, 0, 1]:
                print('Right')
                if SlideNum < len(pathSlides)-1:
                    button_pressed = True
                    annotations = [[]]
                    annotation_number = -1
                    annotation_start = False

                    SlideNum += 1

        # Gesture-3 Pointer
        if fingers == [0, 1, 1, 0,0]:
            cv2.circle(SlideCurrent, index_finger, 12, (0, 0, 255), cv2.FILLED)

        # Gesture-4 Draw
        if fingers == [0, 1, 0, 0, 0]:
            if annotation_start is False:
                annotation_start = True
                annotation_number += 1
                annotations.append([])
            cv2.circle(SlideCurrent, index_finger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotation_number].append(index_finger)
        else:
            annotation_start = False

        # Gesture-5
        if fingers == [0, 1, 0, 0, 1]:
            if annotations:
                annotations.pop(-1)
                annotation_number -= 1
                button_pressed = True







    # Button_Pressed itreation
    if button_pressed:
        button_counter += 1
        if button_counter > button_delay:
            button_counter = 0
            button_pressed = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(SlideCurrent, annotations[i][j-1], annotations[i][j], (0, 255, 0), 12)



    # Adding WebCam Img to the Slide
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = SlideCurrent.shape
    SlideCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow('Slides', SlideCurrent)
    cv2.imshow('Image', img)

    Key = cv2.waitKey(1)
    if Key == ord('q'):
        break
