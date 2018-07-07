import cv2
import team5308api as wyh

team = wyh.team5308()

team.show()
team.cvtHSV()
cv2.imshow('testHSV',team.HSVPic)
team.findcase()
#team.scanAndFix()

team.scanAndFix2()

team.saveLocal(0)



team.release(10000000)