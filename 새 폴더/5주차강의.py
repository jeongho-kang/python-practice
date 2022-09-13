# 조건식으로 반복 제어 (환영합니다 5번)
'''
x = 0
while x < 5 :
    print("환영합니다.")
    x = x+1
'''
# 암호를 입력 받아 로그인하기
'''
password = ""

while password != "1234" :
    password = input("암호를 입력하세요 : ")
    
print("**로그인 성공**")
'''
#1부터 100까지 정수중에서 홀수만 출력하기
'''
x = 1
while x <= 100 :
    print(x, end = " ") #end 함수는 띄어쓰기 해주는 함수
    x = x + 2
'''
#양수를 하나 입력하고 1부터 양수중에서 홀수만 출력
'''
x =1
number = int(input("양수를 입력하시오 : "))

while x <= number :
    print(x, end = " ")
    x = x + 2
'''
#반복문의 흐름제어
'''
x = 0
while True :
    x = x + 1
    if x > 20 :
        break
    if x % 3 == 0:
        continue
    print(x)
'''
# 숫자 맞히기 게임
'''
from random import *
comp = randint (1,20)
number = 0
print("게임을 시작합니다.")
while True :
    number = int(input("숫자 입력(1~20): "))
    if number < 1 or number > 20 :
        print("1부터 20 사이의 숫자를 사용하세요.")
        continue
    
    if number > comp :
        print("↘")
    elif number < comp :
        print("↗")
    else:
        print("정답!")
        break
print("게임을 종료합니다.")
'''
# 1부터 100까지 홀수 출력하기
'''
for x in range(1,101,2) :
    print(x)
'''
# 구구단 출력하기
'''
dan = int(input("몇 단을 출력할까요?: "))
for x in range(1, 10) :
    print(dan , "X", x, "=", dan * x)
input() # 엔터를 누르면 cmd창이 꺼지면서 프로그램이 끝난다.
'''
# 터틀 그래픽스
'''
from turtle import *
setup(250,250)
color('blue', 'yellow')
begin_fill()
circle(50)
end_fill()
'''
# 사각형 그리기
'''
from turtle import *
setup(250,250)
for _ in range(4) :
    fd(100)
    lt(90)
done() # cmd 에서 실행하고 나서 프로그램이 종료되지않음.
'''
# 5주차 과제 터틀 그래픽 정다각형 그리기 프로그램
'''
from turtle import *
while True :
    n = int(input("모양 선택(3~6): "))
    if n < 3 or n > 6 :
        print("3~6까지 입력하세요: ")
        continue
    clear()
    for _ in range(n) :
        fd(100)
        lt(360/n)
done()
'''
