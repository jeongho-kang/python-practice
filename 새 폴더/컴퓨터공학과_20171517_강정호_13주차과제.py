# 컴퓨터공학과_20171517_강정호_ 13주차 과제

import cv2

img = cv2.imread('snowrian.jpg') # 원본
img2 = cv2.resize(img,(300,300)) # 사이즈 줄이기
img3 = img[200:,:900] # 자르기
img4 = cv2.blur(img,(30,30)) # 블러처리
img5 = cv2.imread('snowrian.jpg', cv2.IMREAD_GRAYSCALE) # 그레이 스케일
img6 = cv2.equalizeHist(img5) # 대비 효과

cv2.imshow('original', img)
cv2.imshow('resized', img2)
cv2.imshow('cropped',img3)
cv2.imshow('blurred', img4)
cv2.imshow('grayscale', img5)
cv2.imshow('equalized', img6)

cv2.waitKey()
cv2.destroyAllWindows()
