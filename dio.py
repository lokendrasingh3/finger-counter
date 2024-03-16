import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=1)

while True:
    status,frame=cap.read()
    hands, frame = detector.findHands(frame, draw=True, flipType=True)
    if hands:
        lmlist=hands[0]
        fingerUp=detector.fingersUp(lmlist)
        print(fingerUp)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,"finger_count=0",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,"finger_count=1",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[0,0,1,0,0]:
            cv2.putText(frame,"finger_count=1",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[0,0,0,1,0]:
            cv2.putText(frame,"finger_count=1",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[0,0,0,0,1]:
            cv2.putText(frame,"finger_count=1",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[1,0,0,0,0]:
            cv2.putText(frame,"finger_count=6",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,"finger_count=2",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[0,1,0,1,0]:
            cv2.putText(frame,"finger_count=2",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,"finger_count=3",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,"finger_count=4",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
        if fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,"finger_count=5",(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1,cv2.LINE_AA)
    cv2.imshow("hands",frame)


    if(cv2.waitKey(1) & 0xFF==ord('x')):
        break
cap.release()
cv2.destroyAllWindows()
