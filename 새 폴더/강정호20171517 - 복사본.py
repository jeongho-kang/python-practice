#컴퓨터공학과 20171517 강정호 중간고사 대체과제

menu_dic = {"연필":300,"지우개":100,"커피":500,"탄산음료":700}
total = 0

while True :
    print("*******************************************************************************")
    print("메뉴 (0.주문종료 1:연필(300원) 2:지우개(100원) 3:커피(500원) 4:탄산음료(700원))")
    print("*******************************************************************************")
    menu = int(input("메뉴를 입력하세요 : "))
    if menu == 0 :
        print("주문총액은",total,"원 입니다.")
        break
    
    elif menu == 1 :
        total = total + menu_dic.get("연필")

    elif menu == 2 :
        total = total + menu_dic.get("지우개")

    elif menu == 3 :
        total = total + menu_dic.get("커피")

    elif menu == 4 :
        total = total + menu_dic.get("탄산음료")

    else :
        print("번호를 잘못 입력하셨습니다. 다시 입력하세요.")

input()



