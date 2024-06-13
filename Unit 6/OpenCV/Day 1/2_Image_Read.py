import cv2 as cv

#IMREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here.  1
#IMREAD_GRAYSCALE loads the image as an intensity one      0
#IMREAD_UNCHANGED loads the image as is (including the alpha channel if present)        -1


img = cv.imread('lena.jpg', cv.IMREAD_GRAYSCALE)

if img is not None:
    cv.imshow("My Image", img)
    k = cv.waitKey(0)
    if k == ord("q"):
        cv.destroyAllWindows()
else:
    print('Could not open image')

