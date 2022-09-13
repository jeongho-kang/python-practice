'''
# 온점 확인기

a = ""
print("문장을 입력해주세요 'q'를 입력시 종료합니다.")
while a != 'q' :
    a = input("")
    if a[-1] == "." :
        print("온점을 잘 입력하셨습니다.")
    else :
            print("온점을 입력 하세요.")
'''
# 줄임말 생성기
a = ""
print("문장을 입력해주세요. 'q' 입력시 종료합니다.")
while a != 'q' :
    a = input()
    print(a[0]) 
    for i in range(len(a)):
        if a[i] == " ":
            print(a[i+1])

a = 'i have a dream'
a.upper()
    # 전부다 대문자
a.capitalize() # 첫글자만 대문자
a.replace(' ','/') # 문자열 바꾸기
a.split('/') # 문자열 분리하기
symbol=='--'
symbol.join(a) # 문자열끼리 연결하기
a.find() # 문자열 위치찾기
a.index() # 문자열 위치찾기
a.strip() # 공백 지우기 ex) '      i have a dream' 출력 : 'i have a dream'
a.isdigit() # 숫자인지 확인
a.isalpha() # 문자인지 확인
a.islower() # 소문자 판별
a.isupper() # 대문자 판별

# 어절 개수 세기
a = ""
print("문장을 입력하시오 'q'를 입력시 종료합니다.")
while a != 'q' :
    a = input()
    b = 1
    for i in range(len(a)) :
        if a[i] == " ":
            b += 1
    if a=='q':
        break
    print("이 문장은", b, "어절입니다.")

#문자열 포맷팅
a = 'apple'
print("I think %s is the best fruit"%a)
weight = 180
print("I will diet until get %d kg"%weight)
print("I will diet until get %f kg"%weight)
print("I will diet until get %.1f kg"%weight)


# 자동 기사 입력
a = input("승리팀: ")
b = input("패배팀: ")
c = input("스코어: ")
d = int(input("경기유형 (1,2,3): "))
e = input("MVP 선수 이름: ")
if d == 1:
    d = '불꽃튀는'
elif d == 2:
    d = '단조로운'
elif d == 3:
    d = '일방적'
print("오늘 {0}팀과 {1}팀의 경기가 있었습니다. 경기는 {0}팀의 {2} 승리로 끝이 났습니다.오늘 승부는 {3} 경기가 펼쳐졌는데요. 양팀 다 더욱 더 분발하여 앞으로 더 좋은 경기력을 보여주겠다는 다짐을 내바쳤습니다.오늘의 MVP는 {4} 선수였습니다. 요즘 {4} 선수의 기세가 만만치 않은데요. 이 상승세가 어디까지 이어질지 귀추가 주목됩니다.".format(a,b,c,d,e))
            
         
    

