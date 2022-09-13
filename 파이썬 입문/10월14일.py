'''
# for i in range 반복문

for i in range (5,16):
    print(i)
for i in range (0,21,2):
    print(i)
for i in range(-100,101,4):
    print(i)

#피보나치 수열
a=0; b=1
for i in range(20):
    print(a,end=" ")
    n = a+b
    a = b
    b = n

#짝,홀 생성
a = int(input("홀수 1, 짝수 2 :"))
for i in range(a,101,2):
    print(i)
    

# for 문 break , continue
for i in range(2, 979):
    if 979%i ==0 :
        break
    print(i)

a = int(input("마지막 숫자는 :"))
b = int(input("뛰어넘을 숫자는 :"))
for i in range(a+1):
    if i == b :
        continue
    print(i)

# 구구단 출력하기 한단만
a = int(input("구구단을 외자 ~ 몇 단 ? :"))
print(a, "단 시작 ===========")
for i in range(1,10):
    print(a ,'X', i ,'=', a*i)

# 구구단 출력하기 3단부터 9단
n = int(input("구구단을 외자 ~ 몇 단 ? :"))
for a in range(n,10):
    print(a,"단 시작 ============")
    for b in range(1,10) :
        print(a ,'X', b ,'=', a*b)

#터틀 그래픽스
from turtle import *
for _ in range(5):
   forward(100)
   left(144)

from turtle import *

for _ in range(15):
    left(20)
    for _ in range(4):
        forward(100)
        left(90)
'''

    

