phone={}

while True:
    print("******************************************")
    print("메뉴 (1.출력 2.추가 3.삭제 4.변경 5.종료")
    print("******************************************")
    menu=int(input("메뉴를 선택하세요. : "))

    if menu ==1:
        for k in phone.keys():
            print('---------------------------')
            print('이름 : %s\n전화번호 : %s'%(k,phone[k]))


    
    elif menu == 2:    
        name=input('이름을 입력하세요 : ')
        num=int(input('번호를 입력하세요 : '))
        phone[name]=num
        print("-------등록 되었습니다-------")

    elif menu == 3:
        name= input("삭제할 이름을 입력하세요 : ")
        num= input("삭제할 번호를 입력하세요  : ")
        del phone[name]
        print("-------삭제 되었습니다-------")
        
    elif menu ==4:
       
        
        name=input("변경하고 싶은 사람의  이름을 입력해주세요")
        change_name=input("무엇으로 수정하시겠습니까? : ")
            
        phone[change_name]=num
        print("이름이 변경되었습니다")
        

               
            
            

    elif menu == 5:
        print("종료 합니다.")
        break;
        
    else:
        print("잘못된 번호 입니다. 다시 입력해주세요 ")
