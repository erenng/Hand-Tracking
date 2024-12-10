import cv2 
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)

mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils #kırmızı ve beyaz kısımları oluşturuyor el üzerindeki

tipIDs=[4,8,12,16,20]

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)
            
            for id,lm in enumerate(handLms.landmark):
                h , w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                
                ##işaret uç parmak 8
                #if id == 20:
                #    cv2.circle(img, (cx,cy), 9, (255,0,0), cv2.FILLED)
                #
                ##işaret uç parmak 6
                #if id == 18:
                #    cv2.circle(img, (cx,cy), 9, (0,0,255), cv2.FILLED) 
    if len(lmList) != 0:
        fingers =[]
        
        #baş parmak için
        
        if lmList[tipIDs[0]][1] < lmList[tipIDs[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        
        for id in range(1,5):
            if lmList[tipIDs[id]][2] < lmList[tipIDs[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        
        totalF = fingers.count(1)
        #print(totalF)
        cv2.putText(img, str(totalF), (30,150) ,cv2.FONT_HERSHEY_TRIPLEX , 3, (179,53,0),5)
    
    
    cv2.imshow("img", img)
    cv2.waitKey(1)
























