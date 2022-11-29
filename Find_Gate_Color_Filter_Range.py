import cv2


def nothing(x):
    pass


img_original = cv2.imread("p1.png")
img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)

cv2.namedWindow("colors")

cv2.createTrackbar('LowerbH', "colors", 0, 255, nothing)
cv2.createTrackbar('LowerbS', "colors", 0, 255, nothing)
cv2.createTrackbar('LowerbV', "colors", 0, 255, nothing)
cv2.createTrackbar('UpperbH', "colors", 255, 255, nothing)
cv2.createTrackbar('UpperbS', "colors", 255, 255, nothing)
cv2.createTrackbar('UpperbV', "colors", 255, 255, nothing)

while (1):
    lowerbH = cv2.getTrackbarPos('LowerbH', "colors")
    lowerbS = cv2.getTrackbarPos('LowerbS', "colors")
    lowerbV = cv2.getTrackbarPos('LowerbV', "colors")
    upperbH = cv2.getTrackbarPos('UpperbH', "colors")
    upperbS = cv2.getTrackbarPos('UpperbS', "colors")
    upperbV = cv2.getTrackbarPos('UpperbV', "colors")

    img_target = cv2.inRange(
        img_original, (lowerbH, lowerbS, lowerbV), (upperbH, upperbS, upperbV))

    img_specifiedColor = cv2.bitwise_and(
        img_original, img_original, mask=img_target)
    cv2.imshow("colors", img_specifiedColor)
    #cv2.imshow("colors", img_target)

    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
