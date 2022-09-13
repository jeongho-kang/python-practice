a = input("이름을 입력하세요:")
height = int(input("키(cm)를 입력하세요:"))
weight = int(input("몸무게(kg)를 입력하세요:"))
bmi = weight / (height/ 100)**2

print(a,"님의 키는", height ,"cm이고 몸무게는 ", weight , "kg 입니다.")
print("BMI 지수는", round(bmi,2),"입니다.")
