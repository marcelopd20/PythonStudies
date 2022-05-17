import cv2


def detectSquare(c):
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    x, y, w, h = cv2.boundingRect(approx)
    if len(approx) != 4:
        return False
    else:
        ar = w / float(h)
        return True if 0.95 <= ar <= 1.05 else False

"""    peri = cv2.arcLength(c, True)
approx = cv2.approxPolyDP(c, 0.04 * peri, True)
for c in cnts:
    area = cv2.contourArea(c)
    print(area)
    print(cv2.boundingRect(c))
    if min_area < area < max_area:
        x, y, w, h = cv2.boundingRect(c)
        #cv2.imshow(img[y:y+h, x:x+w])
        #cv2.waitKey(0)
        cv2.rectangle(img, (x,y), (x+w, y+h), (36,255,12),2)
        cv2.imshow("", img)
        cv2.waitKey(0)
        print(x, y, w, h)
        return True
    else:
        return False"""

