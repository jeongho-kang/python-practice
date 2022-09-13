'''
age = int(input("나이를 입력하시오 :"))
if age < 14:
    print("어린이입니다.")
elif 14 <= age <= 19:
    print("청소년입니다.")
else :
    print("성인입니다.")


grade = int(input("성적을 입력하시오: "))
if grade >= 90 :
    print("이번 학기 성적은 A 입니다.")
elif grade >= 80 :
    print("이번 학기 성적은 B 입니다.")
elif grade >= 70 :
    print("이번 학기 성적은 C 입니다.")
else :
    print("F 입니다.")

name = input("이름을 입력하세요 :")
height = int(input("키를 입력하시오 :"))
weight = int(input("몸무게를 입력하시오 :"))

bmi = weight/(height/100)**2

if bmi > 30 : a = "고도비만"
elif bmi > 25 : a = "비만"
elif bmi > 23 : a = "과체중"
elif bmi > 18 : a = "정상"
else : a = "저체중"

print()
print(name,"님의 키는",height,"이고 몸무게는",weight,"입니다.")
print("BMI 지수는" ,round(bmi,2),"이고 ,",a,"입니다." )


number = int(input("숫자를 입력하시오 :"))
if number < 10 : a = "한 자릿수"
elif number < 100 : a = "두 자릿수"
elif number < 1000 : a = "세 자릿수"
else : a = "세 자릿수 이상"

print(a)


a = input("[남],[여] 중 하나를 입력하세요 :")
if a == "남" :
    age = int(input("현재 나이를 입력 하세요 :"))
    if age >=20 :
     b = input("[재][휴] 중 하나를 입력하세요 :")
     if b == "휴" : print("영장을 보냅니다.")
else : print("종료합니다.")

'''
print("사이다(700원) 콜라(800원) 물(1200원)")
money = int(input("얼마를 입력하시겠습니까 ?"))
drink = int(input("선택) 1:사이다 2:콜라 3:물 :"))
if drink == 1 and money >=700:
    print("사이다가 나왔습니다. 덜컹")
    money = money - 700
elif drink == 2 and money >=800:
    print("콜라가 나왔습니다 덜컹")
    money = money - 800
elif drink == 3 and money >=1200:
    print("물이 나왔습니다 덜컹")
    money = money - 1200
else : print("음료수를 뽑을 수 없습니다.")
if money >=0 :
    print("잔돈", money ,"원 반환 합니다.")



