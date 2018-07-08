import cv2
import team5308api as wyh

team = wyh.team5308(1)

team.show()
team.cvtHSV()
cv2.imshow('testHSV',team.HSVPic)
team.findcase()
#team.scanAndFix()


print("begin scan and Fix 2")
team.scanAndFix2()
print("scan and Fix completed")


team.saveLocal(0)



team.release(10000000)