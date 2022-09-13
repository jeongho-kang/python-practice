# 컴퓨터공학과 20171517 강정호 11주차 과제

import numpy as np

np.random.seed(1000)
a = np.random.rand(3,3)

print("배열 a의 값 : \n", a)
print("=============================================")
print("a의 원소들 중 최대값 : ", np.max(a))
print("a의 원소들 중 최소값 : ", np.min(a))

input()
