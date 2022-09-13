# 9주차강의
'''
#문자 단위로 읽기
f= open("dream.txt", "r")
contents = f.read()
print(contents)
f.close()
'''
#with문과 함께 open() 함수 사용하기
'''
with open("dream.txt", "r") as f :
    contents = f.read()
    print(contents)
'''
# 라인 단위로 모두 읽기 readlines() 함수
'''
with open("dream.txt", "r") as f :
    contents = f.readlines()
    print(contents)
'''
# 반복문과 함께 라인 단위로 읽기 readline() 함수
'''
with open("dream.txt", "r") as f :
    num = 0
    while True :
        contents = f.readline()
        if contents == "" :
            break
        num = num + 1
        print(num, ":" ,contents, end = "")
'''
# 파일 입력
'''
f= open("guest.txt" ,"w")
f.write("kim\n")
f.write("park\n")
f.close()
'''
# 여러 개 문자열을 파일에 쓰기 writelines()함수
'''
with open("guest.txt","w") as f:
    f.writelines("kim\n" "park\n" "choi\n")
    f.writelines(["park\n", "123"])
'''
# 키보드로 입력한 데이터를 파일에 쓰기
'''
with open("guest.txt","w")as f :
    contents = input("파일에 쓸 내용은 ?: ")
    f.write(contents)
'''
# 키보드로 입력한 점수를 파일에 저장하기
'''
with open("number.txt" , "a") as f :
    print("점수를 입력하세요. 음수를 입력하면 종료됩니다.")
    while True :
        num = int(input("점수 : "))
        if num < 0 :
            print("입력을 종료하고 프로그램을 종료합니다.")
            break
        f.write(str(num) + "\n")
'''
# 예외처리




















