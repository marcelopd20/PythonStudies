import cv2
import numpy


def detectGreen(self):
    hsv = cv2.cvtColor(self, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0,100,0), (86, 255, 255))
    imask = mask>0
    green = numpy.zeros_like(self, numpy.uint8)
    green[imask] = self[imask]
    return green
