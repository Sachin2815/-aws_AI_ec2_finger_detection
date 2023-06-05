import cv2
cap  = cv2.VideoCapture(0)


while True:
  status , photo = cap.read()
  cv2.imshow("my photo" , photo)
  
  if cv2.waitKey(100) == 13:
    break
   
cv2.destroyAllWindows()


import cv2
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(maxHands=1 , detectionCon=0.8 )
cap = cv2.VideoCapture(0)
while True:
    ret, photo = cap.read()
    hand = detector.findHands(photo, draw=False)
    cv2.imshow("my photo" , photo)
    if hand != []:
        detectHand = hand[0]
        print(detector.fingersUp(detectHand))
    if cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()
cap.release()
