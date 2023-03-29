import cv2 as cv

img=cv.imread('C:/Users/WIN/media/soccer.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

grad_x=cv.Sobel(gray,cv.CV_32F,1,0,ksize=3)	# 소벨 연산자 적용
grad_y=cv.Sobel(gray,cv.CV_32F,0,1,ksize=3)

grad1_x=cv.Scharr(gray,cv.CV_32F,1,0)	# Scharr 연산자 적용
grad1_y=cv.Scharr(gray,cv.CV_32F,0,1)

sobel_x=cv.convertScaleAbs(grad_x)	# 절대값을 취해 양수 영상으로 변환
sobel_y=cv.convertScaleAbs(grad_y)
scharr_x=cv.convertScaleAbs(grad1_x)
scharr_y=cv.convertScaleAbs(grad1_y)

edge_strength =cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0)	#sobel 에지 강도 계산
edge_strength1 =cv.addWeighted(scharr_x,0.5,scharr_y,0.5,0)	#scharr 에지 강도 계산

cv.imshow('sobelx',sobel_x)
# cv.imshow('sobely',sobel_y)
cv.imshow('scharrx',scharr_x)
# cv.imshow('scharry',scharr_y)
cv.imshow('edge strength_sobel',edge_strength)
cv.imshow('edge strength_Scharr',edge_strength1)

cv.waitKey()
cv.destroyAllWindows()