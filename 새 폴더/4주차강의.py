# 파이썬의 조건문
'''
x = 3
if x > 0:
    print("X는 양수입니다.")
'''
# 성년인지 확인하는 코드
'''
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요; "))
if age >= 19:
    print(name, "님은 성인입니다.\n 입장하세요.")
'''
# 베타적 조건
'''
num = int(input("정수를 입력하세요: "))
if num >0:
    print("양수입니다.")
else :
    print("양수가 아닙니다.")
'''
# 하나 이상의 조건표현
'''
num = int(input("정수를 입력하세요: "))
if num >0:
    print("양수입니다.")
elif num == 0 :
    print("0 입니다.")
else :
    print("음수 입니다..")
'''
# 나이 표현하기
'''
name = input("이름을 입력하시오: ")
age = int(input("나이를 입력하시오: "))
if age < 20 :
    print(name,"님은 10대 이하입니다.")
elif age < 30 :
    print(name, "님은 20대 입니다.")
elif age < 40 :
    print(name, "님은 30대 입니다.")
else :
    print(name, "님은 40대 이상입니다.")
'''
# 조건문 안에 조건이 더 필요한 경우
'''
num = int(input("정수를 입력하세요: "))
if num  > 0 :
    print("양수입니다.")
else :
    if num == 0 :
        print("0 입니다.")
    else :
        print("음수입니다.")
'''
# 과속 단속 프로그램
'''
speed = int(input("속도를 입력하세요: "))
if speed >= 30 :
    print("과속 입니다. 속도를 줄여주세요.")
else :
    print("안전운전 하세요.")
'''
# 짝수 홀수 검사
'''
num = int(input("정수를 입력하세요: "))
if num % 2 == 0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")
'''
# 출입 안내
'''
name = input("이름을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))
if age >= 19 :
    print(name,"님은 성년입니다.\n입장하세요.")
else :
    print(name,"님은 미성년입니다.\n출입할 수 없습니다.")
'''
# 주민번호로 성별 판단하기
'''
number = int(input("주민등록번호 뒷자리 첫 번쨰 숫자를 입력하세요."))
if number == 1 or number == 3 :
    print("남자입니다.")
elif number == 2 or number == 4 :
    print("여자입니다.")
else :
    print("잘못입력하였습니다.")
'''
# 또 다른 주민번호 성별 판단
'''
number = int(input("주민등록번호 뒷자리 첫 번쨰 숫자를 입력하세요."))
if 1 <= numver <= 4:
    if number % 2 == 0 :
        print("여자입니다.")
    else :
        print("남자입니다.")
else :
    print("잘못입력하였습니다.")
'''
# BMI 프로그램
name = input("이름을 입력하시오: ")
height = float(input("키를 입력하세요 : "))
weight = float(input("체중을 입력하세요 : "))
bmi = weight / (height/100) **2
if bmi > 30 : a = "고도비만"
elif bmi > 25 : a = "비만"
elif bmi > 23 : a = "과체중"
elif bmi > 18 : a = "정상"
else : a = "저체중"
print()
print(name,"님의 키는",height,"이고 몸무게는",weight,"입니다.")
print("BMI 지수는" ,round(bmi,2),"이고 ,",a,"입니다." )
