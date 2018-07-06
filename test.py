import cv2
import __data__ as data

cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')

while cap.isOpened():
    _ , png = cap.read()
    cv2.imshow('Test',png)
    picpng =  cv2.cvtColor(png, cv2.COLOR_RGB2HSV)
    
    #st = cv2.inRange(picpng, (data.iMinH, data.iMinS, data.iMinV), (data.iMaxH, data.iMaxS, data.iMaxV))
    
    st = cv2.inRange(picpng, (1, 1, 1), (0, 0, 0))

    cv2.imshow('trt', st)
    q = cv2.waitKey(20)
    if( q == 'q'):
        break

cv2.destroyAllWindows()
cap.release()
