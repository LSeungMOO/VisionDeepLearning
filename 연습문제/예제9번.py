import cv2 as cv
import sys

img=cv.imread('C:/Users/WIN/Downloads/media/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
BrushSize=5
LColor,RColor=(255,0,0),(0,0,255)

def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN: 
        cv.circle(img,(x,y),BrushSize,LColor,-1)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),BrushSize,RColor,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSize,LColor,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSize,RColor,-1)
        
    cv.imshow('Painting',img)
    
cv.namedWindow('Painting')
cv.imshow('Painting',img)

cv.setMouseCallback('Painting',painting)

while(True):
    if cv.waitKey(1)==ord('x'):
        cv.destroyAllWindows()
        break
    elif cv.waitKey(1)==ord('+'):
        BrushSize+=1
    elif cv.waitKey(1)==ord('-'):
        BrushSize-=1
        if BrushSize < 1:
            BrushSize = 1