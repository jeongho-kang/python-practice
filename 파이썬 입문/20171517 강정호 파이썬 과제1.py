# 도형의 면적 구하기
figure = int(input("도형을 입력하시오(1:사각형,2:삼각형,3:원) :"))
if figure == 1:
    width = int(input("가로 : "))
    height = int(input("세로 : "))
    area = width * height
    print("면적 :",area)
elif figure == 2:
    width = int(input("가로 : "))
    height = int(input("세로 : "))
    area = width * height / 2
    print("면적 :",area)
elif figure == 3:
    r = int(input("반지름을 입력하시오 :"))
    area = r * r *3.14
    print("면적 :",area)
else : print("잘못 입력하셨습니다.")

