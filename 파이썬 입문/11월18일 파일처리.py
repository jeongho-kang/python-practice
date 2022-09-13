'''
file = open('c:/text/New File.txt', 'w')
file.writelines(["리스트1","리스트2","리스트3"])
file.close()
data = "으로 만들어지는 파이썬 세상"
file = open('c:/text/New File.txt' , 'a')
file.write(data)
file.close()


file = open('c:/text/New File.txt','at')
while a < 10 :
	b = "%d 숫자 \n",a
	file.write(b)
	a = a+1
        file.close()

# 예외처리 try - except 기본 사용
try:
    f = open('python.txt','r')
except:
    print("파일을 읽을 떄 오류가 발생했습니다.")

# try - except 오류 종류 저장하기
try:
    f = open('python.txt','r')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# try에서 오류가 나지 않았을 경우 else에서 계속 실행
try:
    f = open('python.txt','r')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
else :
    a = f.read()
    print(a)
    f.close()

# try에서 오류 여부 상관없이 마지막에 실행 finally
try:
    f = open('python.txt','r')
except FileNotFoundError:
    pass
else:
    a = f.read()
    print(a)
    f.close()
finally:
    print("작업을 마쳤습니다.")

# 3번까지 있는 리스트 a를 만들고 a[4] 리스트를 호출할 경우 에러메시지를 출력하라
a = ["1","2","3"]
try:
    print(a[4])
except IndexError:
    print("잘못된 인덱스를 인덱싱 했습니다.")


# 딕셔너리 생성 후 일므을 입력하면 생년월일을 출력하는 프로그램
# 단 해당 이름이 없는 경우 일므이 없다는 메시지를 출력하라
birth = {"홍길동":"2000년 3월 1일","김춘추":"604년","김유신":"500년"}
answer = ""
while answer != 'q' :
    answer = input("생일을 알고 싶은 사람을 입력하세요: ")
    try:
        print(birth[answer])
    except KeyError:
            print("데이터베이스에 존재하지 않는 이름입니다.")
'''
# 텍스트로 데미지를 입력받아 체력이 낮아짐, save라고 입력시 남은 체력 저장
hp = 280
hit = ""
print("현재 체력은",hp,"입니다.")
while hit != "save" and hp > 0 :
    hit = input("데미지를 몇 입었습니까 ?: ")
    if hit == "save" :
        f = open('file.txt','w')
        f.write(str(hp))
        f.close()
    else :
        hit = int(hit)
        hp = hp - hit
        print("체력이",hp,"남았습니다.")
    

    
    
