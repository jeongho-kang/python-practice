'''
#피보나치 수열
i = 0; j=1; fibo = 0
while fibo < 100:
    fibo = i+j
    print(fibo)
    i = j
    j = fibo


name = ""
while name != "q":
    name = input("당신의 이름을 입력하시오 'q' 를 누르시면 종료됩니다. :")
    print(name)
    
# up & down 게임
answer = 77; number = 0
while number != answer :
    number = int(input("예상 숫자를 입력하세요 :"))
    if answer > number:
        print("UP")
    elif answer < number:
        print("DOWN")
    elif answer == number:
        print("정답")

#주사위 던지기 프로그램
from random import *
throw = 0
print("숫자를 입력하세요 :")
while throw != 'q':
    print(randint(1,6))
    throw = int(input("아무키를 누르면 주사위가 던져집니다. 종료를 원하시면 'q'를 입력해주세요"))


# 구구단 출력
num = 0;

while num != 1:
    num = int(input("(종료'1')구구단 몇단을 출력할까요 :"))
    i = 1
    while i < 10:
         print(num,"x",i,"=",num*i)
         i = i+1

# 가우스 계산기
num = 0
while num != 1:
    num = int(input("(종료'1')숫자 입력: "))
    i = 1
    sum_n = 0
    while i < num+1:
     sum_n=sum_n+i
     i = i+1
     print(sum_n)


#주인공 체력 계산
hp = 100
while hp > 0:
    print("주인공의 체력은", hp, "입니다 얼마의 데미지를 입히시겠습니까 ?")
    damage = int(input("얼마의 데미지를 입히시겠습니까 ?"))
    hp = hp - damage
    print("주인공이 죽었습니다.")

#소수인지 확인하는 프로그램
i=2
while i<979:
    print(i)
    if 979%i==0:
        break
 i=i+1

i = 1
while True :
    print(i)
    if i == 50:
        print("끝")
        break
    i = i+1

# 자판기 프로그램
menu = 0
while menu < 4 :
    menu = int(input("메뉴(1:커피 2:생수 3:주스) :"))
    if menu == 1:
        print("커피")
    elif menu == 2:
        print("생수")
    elif menu == 3:
        
        print("주스")
    else :
        print("주문완료")

# Up & Down 게임(1)
answer = 77; number = 0
while number != answer :
    number = int(input("예상 숫자를 입력하세요 :"))
    if answer > number:
        print("UP")
    elif answer < number:
        print("DOWN")
    elif answer == number:
        print("정답")
'''
# Up & Down 게임(1)
from random import *
throw = randint(10,99)
num = 0
print("게임시작 ========")
while throw!= num :
    num = int(input("예상 숫자를 입력하시오(10~99) :"))
    if num < throw:
        print("Up")
    elif num > throw:
        print("Down")
    elif num == throw:
        print("정답")
        gameon = input("게임을 다시 할래요?(y/n)")
