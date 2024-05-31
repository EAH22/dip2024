import sys # to access the system
import cv2
img = cv2.imread("test1.jpg", cv2.IMREAD_ANYCOLOR)
 
while True:
    cv2.imshow("CHAMPLOO", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes
 

