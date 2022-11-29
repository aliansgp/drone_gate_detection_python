# Drone Gate Detection Python

to find what is our gate color range, convert our RGB image to HSV and with HSV feature, HSV Trackbar, find gate color range.

use a filter with cv2.iRange and founded color range to make the gate image ,a binary image.
in result gate pixles are 1 (white) and other pixles are 0 (balck).

for better accuracy and less noise, we use morphology(open and close).

using findcontour to find gate contours will get 2 contours(internal & external) because we want to previde crash with gate, we use sort to detect internal contour.

to find center of contour, we use contour moments (https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html)




