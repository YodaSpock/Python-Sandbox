import cv2

#BASIC IMAGE
#img = cv2.imread("Resources/RachelandIsaac.jpg")
#cv2.imshow("Output", img)
#cv2.waitKey(0)

#BASIC VIDEO
#cap = cv2.VideoCapture("Resources/Order66.MOV")
#while True:
#    success, img = cap.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) &0xFF == ord('q'):
#        break

#BASIC WEBCAM CAPTURE
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
