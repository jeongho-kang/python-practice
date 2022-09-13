# 두 정수를 입력받고 합계 출력하는 프로그램
'''
num1 = int(input("첫번쨰 정수를 입력하시오: "))
num2 = int(input("두번쨰 정수를 입력하시오: "))
sum = num1 + num2
print("두 정수의 합은 ", sum , "입니다.")
'''
# 몸무게와 키로 bmi 계산
'''
weight = float(input("몸무게를 입력하시오 : "))
height = float(input("키를 입력하시오 ; "))
bmi = weight / (height/100)**2
print("BMI는 ",bmi ,"입니다." )
'''
# 거스름돈 계산
'''
pencil = 400
money = int(input("가지고 있는 돈이 얼마입니까? "))
print("연필은", money // pencil,"자루")
print("거스름돈은", money % pencil,"원 입니다.")
'''
# 시간 계산하기
'''
time = int(input("계산한 시간을 입력하시오: "))
hour = time // 3600
min = (time % 3600) // 60
sec = (time % 3600) % 60
print(hour,"시간", min , "분", sec ,"초입니다.")
'''
# 피타고라스의 정리
'''
a = float(input("밑변의 길이: "))
b = float(input("높이의 길이: "))
c = (a**2 + b**2)**0.5
print("빗변은", c ,"입니다.")
'''
