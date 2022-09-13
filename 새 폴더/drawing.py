# 5주차 과제 터틀 그래픽 정다각형 그리기 프로그램

from turtle import *
while True :
    n = int(input("모양 선택(3~6): "))
    print(">>>")
    clear()
    for _ in range(n) :
        fd(100)
        rt(360/n)
done()
input()
