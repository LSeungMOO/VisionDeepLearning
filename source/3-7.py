import cv2 as cv
import numpy as np

# 이미지 불러오기
img = cv.imread('C:/Users/WIN/Downloads/media/soccer.jpg')
img = cv.resize(img, dsize=(0, 0), fx=0.4, fy=0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 텍스트 추가
cv.putText(gray, 'soccer', (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# 가우시안 스무딩
gaussian1 = cv.GaussianBlur(gray, (5, 5), 0.0)
gaussian2 = cv.GaussianBlur(gray, (9, 9), 0.0)
gaussian3 = cv.GaussianBlur(gray, (15, 15), 0.0)
gaussian = np.hstack((gaussian1, gaussian2, gaussian3))

# 메디안 스무딩
median1 = cv.medianBlur(gray, 5)
median2 = cv.medianBlur(gray, 9)
median3 = cv.medianBlur(gray, 15)
median = np.hstack((median1, median2, median3))

# 디스플레이
cv.imshow('Original', img)
cv.imshow('Gaussian Smoothing', gaussian)
cv.imshow('Median Smoothing', median)

cv.waitKey()
cv.destroyAllWindows()