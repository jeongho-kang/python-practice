from random import *

count=0 #5보다 클 경우 게임 종료
gameon='y'
number=0; answer=0

while gameon=='y':
    print('게임 시작=======')
    answer=randint(10,99) #정답

    while number != answer:
        count+=1
        if count>5:
            print('♬횟수 초과♬')
            break;
    
        number=int(input("예상 숫자를 입력하세요(10~99): "))
        if answer>number:
            print('UP')
        elif answer<number:
            print('DOWN')
        elif answer==number:
            print('♥정답♥')
            
    count=0
    gameon=input("게임을 다시 할래요?(y/n)")
print('=======게임 종료')
    
