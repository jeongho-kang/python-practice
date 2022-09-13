List = []

while True :
    print("******************************************")
    print("메뉴 (1.출력 2.추가 3.삭제 4.변경 5.종료) ")
    print("******************************************")
    menu = int(input("메뉴를 선택하세요. : "))

    if menu == 5:break

    if menu == 1 :

        for name,number in List:
            print("이름: ",name)
            print("전화번호",number)
            
    elif menu == 2 :

        name = input("이름을 입력하세요: ")
        number = input("번호를 입력하세요: ")
        List.append([name,number])
        print("----등록되었습니다.----")

    elif menu == 3 :

        name = input("삭제할 이름을 입력하세요: ")
        number = input("삭제할 번호를 입력하세요: ")
        List.remove([name,number])
        print("-----삭제되었습니다-----.")
        
        
    elif menu == 4 :

       change_chk = int(input("어떤 정보를 변경하시겠습니까 ?(1.이름 2.번호)"))
       if change_chk == 1 :
           name = input("변경할 이름을 입력 하시오: ")
           change_name = input("바꿀 이름을 입력 하시오: ")
           for i in range(len(List)) :
               if List[i][0] == name :
                   List[i][0] = change_name
                   print(List);break

       elif change_chk == 2:

            number = input("변경할 번호를 입력 하시오: ")
            change_number = input("바꿀 번호를 입력하시오: ")
            for i in range(len(List)):
                if List[i][1] == number :
                    List[i][1] = change_number
                    print(List);break
       else :
            print("입력하신 정보가 없습니다.")    
