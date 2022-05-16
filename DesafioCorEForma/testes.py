# importing cv2
import cv2

# path
import numpy

path = '.\imgs\circuloverde.png'

# Using cv2.imread() method
img = cv2.imread(path)

# Displaying the image
cv2.imshow('image', img)
cv2.waitKey(0)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv)
lower_range = numpy.array([36, 0, 0])
upper_range = numpy.array([86, 255, 255])
mask = cv2.inRange(hsv, lower_range, upper_range)
cv2.imshow("image", mask)
cv2.waitKey(0)