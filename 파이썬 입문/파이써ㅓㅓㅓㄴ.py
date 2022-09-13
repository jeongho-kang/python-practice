eyes = float(input("시력을 입력하시오.: "))
if eyes >= 1.0 :
    print("지원이 가능 합니다.")
else:
    print("지원이 불가능 합니다.")


grade = float(input("수능 평균 등급을 입력 하시오: "))
if grade <= 2 :
    print("수능 최저 등급을 만족합니다.\n합격 입니다.")
else:
    print("수능 최저 등급을 만족하지 않습니다.\n불합격 입니다.")



name = input("이름을 입력하시오: ")
if name == '강정호' : 
 print("확인되었습니다.")
else :    
 print("다시 한번 입력하여 주십시오.")


age = int(input("나이는?"))
movie = int(input("영화는? (1: 15세 이상 , 2: 전체관람가)"))
if age >= 15 and movie == 1:
 print("영화를 관람하실수 있습니다.")
else :
    print("영화를 관람하실수 없습니다,")
