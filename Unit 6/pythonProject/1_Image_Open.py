import cv2 as cv

img = cv.imread('lena.jpg')
cv.imshow("My Image", img)
cv.waitKey(5000)
cv.destroyAllWindows()


