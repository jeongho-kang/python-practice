'''
# 영장 프로그램

gen = input("[남],[여] 중 하나를 입력하세요 : ")
age = int(input("현재 나이를 입력하세요 : "))
school = input("[재],[휴]를 입력하세요 : ")
if gen == '남'and age >=20 and school == '휴' :
    print("영장을 보냅니다.")
else :
    print("종료합니다.")
    
# 자동판매기 프로그램

print("사이다(700원) 콜라(800원) 물(1200원)")
money = int(input("얼마를 입력하시겠습니까 ?: "))
drink = int(input("선택1) 1:사이다 2:콜라 3:물 : "))
if drink == 1 and money >= 700 :
    print("사이다가 나왔습니다, 덜컹")
    print("잔돈",money - 700 , "원 반환합니다.")
elif drink == 2 and money >= 800 :
    print("콜라가 나왔습니다 덜컹")
    print("잔돈",money - 800 , "원 입니다.")
elif drink == 3 and money >= 1200 :
    print("물이 나왔습니다. 덜컹")
    print("잔돈",money - 1200,"원 입니다.")
else :
    print("음료수를 뽑을 수 없습니다.")
    print("잔돈",money,"반환합니다.")


# 홀수만 출력하기
i = 1
while i <100 :
    print(i)
    i = i+2
'''
for a in (e,f,g,h) :
    print(a)
