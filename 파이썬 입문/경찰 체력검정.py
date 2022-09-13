m100 = float(input("100m 기록을 입력하시오 : "))
m1000 = float(input("1000m 기록을 입력하시오 : "))
situp = int(input("윗몸일으키기 기록을 입력하시오 :"))
power = int(input("좌우 악력 기록을 입력하시오 :"))
pushup = int(input("팔굽혀펴기 기록을 입력하시오 :"))
if m100 >= 13.6 and m1000 >= 237.0 and situp >= 51 and power >= 56 and pushup >= 46 :
    print("합격 가능성이 매우 높습니다.")
else : 
    print("합격 가능성이 낮습니다.")



kor = float(input("국어 점수를 입력하시오: "))
eng = float(input("영어 점수를 입력하시오: "))
his = float(input("한국사 점수를 입력하시오: "))
obj1 = float(input("선택과목1 점수를 입력하시오: "))
obj2 = float(input("선택과목2 점수를 입력하시오: "))
if kor < 40 and eng < 40 and his < 40 and obj1 < 40 and dbj2 < 40 :
 print("과락입니다.")
else :
 print("합격입니다.")

a = int(input("정수를 입력하시오 : "))
if a < 0 :
 print("입력된 정수는 음수 입니다.")
else :
 print("입력된 정수는 양수 입니다.")
