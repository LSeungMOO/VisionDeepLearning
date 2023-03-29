import cv2 as cv

img = cv.imread('C:/Users/WIN/media/soccer.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny1=cv.Canny(gray,0,100)
canny2=cv.Canny(gray,100,200)
canny3=cv.Canny(gray,100,200,apertureSize=3)
canny4=cv.Canny(gray,100,200,apertureSize=7)
canny5=cv.Canny(gray,100,200,L2gradient=True)
canny6=cv.Canny(gray,100,200,L2gradient=False)

cv.imshow('Original',gray)
cv.imshow('Canny1',canny1)
cv.imshow('Canny2',canny2)
cv.imshow('Canny3',canny3)
cv.imshow('Canny4',canny4)
cv.imshow('Canny5',canny5)

cv.waitKey()
cv.destroyAllWindows()