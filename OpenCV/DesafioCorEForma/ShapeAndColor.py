import numpy
import ColorDetection
import SquareDetection
import imutils
import cv2

cont = True
while cont:
    try:
        image = cv2.imread('.\imgs\quadradoverde.jpg')  # leitura da imagem
        cd = ColorDetection
        image = cd.detectGreen(image)
        cv2.imshow('img', image)
        cv2.waitKey(0)
        resized = imutils.resize(image, width=300)
        ratio = image.shape[0] / float(resized.shape[0])

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
        contour = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #contour = imutils.grab_contours(contour)
        contour = contour[0] if len(contour) == 2 else contour[1]
        print(contour)
        sd = SquareDetection
        for c in contour:
            M = cv2.moments(c)
            if M["m00"] > 0:
                cX = int((M["m10"] / M["m00"]) * ratio)
                cY = int((M["m01"] / M["m00"]) * ratio)
            if sd.detectSquare(c):
                print("Quadrado:", True)
                cont = False
        cont = False
    except EOFError:
        break








