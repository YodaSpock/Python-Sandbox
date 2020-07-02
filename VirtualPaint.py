import cv2
import numpy as np

# BASIC IMAGE
# img = cv2.imread("Resources/RachelandIsaac.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# BASIC VIDEO
# cap = cv2.VideoCapture("Resources/Order66.MOV")
# while True:
#    success, img = cap.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) &0xFF == ord('q'):
#        break

# BASIC WEB-CAM CAPTURE
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)

# while True:
# success, img = cap.read()
#      cv2.imshow("Video", img)
#      if cv2.waitKey(1) &0xFF == ord('q'):
#       break


# BASIC Modifications
# img = cv2.imread("Resources/RachelandIsaac.jpg")

# kernel = np.ones((5, 5), np.uint8)

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# imgCanny = cv2.Canny(img, 150, 200)
# imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Canny", imgCanny)
# cv2.imshow("Dilation", imgDilation)
# cv2.imshow("Eroded", imgEroded)
# cv2.waitKey(0)

#Basic Resizing and Cropping
# img = cv2.imread("Resources/RachelandIsaac.jpg")

# print(img.shape)

# imgResize = cv2.resize(img, (400, 534))
# print(imgResize.shape)

# imgCropped = img[0:200, 200:500]

# cv2.imshow("Regular", img)
# cv2.imshow("Resize", imgResize)
# cv2.imshow("Cropped", imgCropped)

# cv2.waitKey(0)

#Basic Shapes and Texts

# img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)

# img[:] = 255,0,0

# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# cv2.putText(img, "OPENCV", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

# cv2.imshow("Image", img)

# cv2.waitKey(0)

#Basic Warp Perspective

img = cv2.imread()

