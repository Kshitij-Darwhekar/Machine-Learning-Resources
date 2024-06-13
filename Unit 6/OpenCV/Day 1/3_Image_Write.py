
import cv2 as cv
import sys
img = cv.imread('lena.jpg')
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("My Image", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("new image.png", img)