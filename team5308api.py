import cv2
import numpy as np
import __data__ as data

class team5308(object):
    'basic vision class for team5308 CRC 2018. By Wu_Yuanhun'   

    camera = 0
    
    numberPic = 0

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        team5308.numberPic = 0

    def release(self, time=30):
        'time(ms)'
        cv2.waitKey(time)
        self.cap.release()
        cv2.destroyAllWindows()

    #Camera Operation
    def caActived(self):
        'get camera\'s situaion'
        return self.cap.isOpened()

    def caRead(self):
        'grab a traget pic from camera'
        if(self.caActived()):
            __,self.png = self.cap.read()
            return self.png
        else:
            return 'open Camera Fail'

    #Pic operation
    def show(self):
        'show target pic on jetson\'s screen'
        cv2.namedWindow('test')
        cv2.imshow('test',self.caRead())
    
    def cvtHSV(self):
        'cvt RGB Pic to HSV Pic'
        self.HSVPic = cv2.cvtColor(self.png, cv2.COLOR_BGR2HSV)
        return self.HSVPic

    def saveLocal(self, sit=1 ):
        '''
        save current pic to local\n
        @sit situation code\n
        @sit 1 for only pic\n
        @sit 2 for only HSVpic\n
        @sit 0 for both\n
        '''
        if(sit==1 or sit==0):
            cv2.imwrite('pic' + str(team5308.numberPic) + '.png', self.png)
        if(sit==2 or sit==0):
            cv2.imwrite('HSVpic' + str(team5308.numberPic) + '.png', self.HSVPic)
        
        team5308.numberPic += 1

    def findcase(self):
        '''
        find case based on color\n
        color range from data.py
        '''
        self.ST = cv2.inRange(self.HSVPic, (data.iMinH, data.iMinS, data.iMinV), (data.iMaxH, data.iMaxS, data.iMaxV))
        ele = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        self.ST = cv2.morphologyEx(self.ST, cv2.MORPH_CLOSE, ele)

        cv2.namedWindow('yello')
        cv2.imshow('yello', self.ST)


    def scanAndFix(self):
        '''
        scan the whole ST pic\n
        then try to fix more smoothly\n
        '''
        tempST = self.ST
        
        for i in range(1,self.png.shape[0]-2):
            for j in range(1,self.png.shape[1]-2):
                tempR = 0
                for ii in range(2):
                    for jj in range(2):
                        tempR += tempST[i+ii][j+jj]/255
                        if(tempR >= 5):
                            self.ST[i][j] = 255
                #print(str(i)+' '+str(j)+' done\n')
        cv2.namedWindow('aft')
        cv2.imshow('aft',self.ST)

    def scanAndFix2(self):
        tempST = self.ST
        edges = cv2.Canny(tempST, 50, 150, apertureSize = 3)
        lines = cv2.HoughLines(edges, 1, np.pi/180, 100)
        self.drawLines(self.png, lines)

    def drawLines(self,img, lines):
        for i in lines:
            for (rho, theta) in i:
                a = np.cos(theta)
                b = np.sin(theta)
#           变换到x-y坐标系
                x0 = a * rho
                y0 = b * rho
#           用点和斜率得到直线上的两个点
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

        cv2.namedWindow('lines')
        cv2.imshow('lines', img)
