import cv2 as cv
import sys
img=cv.imread('C:/Users/WIN/Downloads/media/smile_girl.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img,(600,40),(1000,600),(0,0,255),2)
cv.putText(img,'laugh',(300,30),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv.arrowedLine(img,(380,60),(500,150),(200,40,0),2)

cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()