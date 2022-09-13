# 넘파이로 BMI 계산하기
'''
import numpy  as np
heights = [183,176,169,186,177,173]
weights = [86,74,59,95,80,68]

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi = np_weights / (np_heights / 100) ** 2

print("대상자들의 키 : ", np_heights)
print("대상자들의 몸무게 : ", np_weights)
print("대상자들의 BMI : ", bmi)
'''
# 넘파이로 선수 정보 추출하기
'''
import numpy as np
players = [[170,76.4],
           [183,86.2],
           [181,78.5],
           [176,80.1]]
np_players = np.array(players)

weights = np_players[np_players[:,1]>= 80]
heights = np_players[np_players[:,0]>= 180]

print("몸무게가 80이상인 선수 정보 : ", weights)
print("가 180이상인 선수 정보 : ", heights)
'''
# 교통사고통계분석

import numpy as np
data = np.genfromtxt('교통사고통계.csv',delimiter = ',')
count = data[:,1]
print("연간 교통사고 평균 : ", np.mean(count))
