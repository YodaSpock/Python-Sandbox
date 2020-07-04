import cv2
#Basic Resizing and Cropping
img = cv2.imread("../Resources/RachelandIsaac.jpg")

print(img.shape)

imgResize = cv2.resize(img, (400, 534))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Regular", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)