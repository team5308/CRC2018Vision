import cv2
import __data__ as data
import numpy

cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')

while cap.isOpened():
    _ , png = cap.read()
    cv2.imshow('Test',png)
    picpng =  cv2.cvtColor(png, cv2.COLOR_BGR2HSV)
    
    #st = cv2.inRange(picpng, (data.iMinH, data.iMinS, data.iMinV), (data.iMaxH, data.iMaxS, data.iMaxV)

    # cv2.imshow('trt', st)
    q = cv2.waitKey(200000000)

cv2.destroyAllWindows()
cap.release()
