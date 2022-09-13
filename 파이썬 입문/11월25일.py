'''
def abc():
    print("함수를 정의할 때는 def(definition)을 이용합니다")
abc()

# say_hello 정의
def say_hello :
    print("어서오세요 ~ 환영합니다.")
    print("지금은 8층ㅡ 스포츠 매장입니다.")
say_hello()

# 함수의 이름 규칙
import keyword
keyword.kwlist


#거북이 도형 만들기
from turtle import *
def penta() :
   for _ in range(5) :
       forward(100)
       left(72)

penta()


# 입력값을 이용하여 출력 값을 변화시키는 함수 x에 값을 넣으면 바뀐다.(인자값 1개)
def triple(x) :
    print(x*x*x)
triple(5)

# 인자값 2개
def multiple(x,y) :
    print(x * y)
multiple(4,5)


#인자가 문자인 경우
def say_hello(name,age) :
    print("{0}님 안녕하세요 ,{0}님의 나이 {1}세에 좋은 상품을 추천합니다".format(name,age))
say_hello("홍길동",15)


#숫자 세 개 입력 시 (a+b)*c의 형태로 출력해주는 함수를 작성하고 실행해보자
def multi(a,b,c):
    print((a+b)*c)
multi(5,6,7)


# 함수의 결과를 반환하기
def multiple(a,b,c):
    print(a*b*c)
    return a*b*c
d = multiple(3,4,5)


# 거북이 도형 (한 변의 길이를 입력 받아 해당 길이만큼 삼각형을 만드는 프로그램)
from turtle import *
def triangle(a) :
    for _ in range(3):
        forward(a)
        left(120)
lenth = int(input("변의 길이를 입력하시오."))
triangle(lenth)


# 반복문을 사용하는 함수 호출
def triple(x) :
    print(x*x*x)

values = [2,3,4,5,6]
for val in values:
    triple(val)

# 반복문 대신 map()함수 사용하기
list(map(triple, values))


#함수의 인수로 리스트 사용하기
values = [2,3,4,5,6]

def triple_list(vals):
    for x in vals:
        print(x*x*x)
triple_list(values)



# 인자를 쓰지 않으면 기본값으로 인자를 받는 함수 작성
def sayhello(name, place = "파이썬월드") :
    print("%s님 안녕하세요. %s에 오신것을 환영합니다." %(name, place))


#매개변수 하나에 여러 인자를 받는 방법 (*)을 이용하여 여러 인자 받기 가
def apark(*calloff):
    print("오늘",calloff,"은(는) 운행하지 않습니다.")
apark("청룡열차","후룸라이드")

#인자에 사람 이름을 넣으면 출력되는 프로그램
def person(*name):
    print("오늘 회의에 참석한 사람은",name,"입니다.")
person("홍길동","이황")

#교대 근무표 작성
def shift(*name) :
    worker = len(name)
    print("교대 근무자의 수는",worker,"입니다.")
    for a in name:
        print(a)

# 좌표상 거리 구하기
def distance(x=0,y=0) :
    if x == 0 and y == 0:
        x = int(input("x 좌표를 입력하세요: "))
        y = int(input("y 좌표를 입력하세요: "))
    dis = (x**2 + y**2) ** 0.5
    print("거리는",c,"입니다.")
# 중심에서 선 그리기
from turtle import *
def draw(x,y):
    goto(x,y)

x = int(input("x좌표: "))
y = int(input("y좌표: "))
draw(x,y)


# 좌표를 그리고 거리 구하기
from turtle import *
def draw(x,y):
    goto(x,y)

def distance(x,y):
    c = (x**2 + y**2) **0.5
    print("거리는",c,"입니다.")
def start():
    x = int(input("x 좌표를 입력하세요: "))
    y = int(input("y 좌표를 입력하세요: "))
    distance(x,y)
    draw(x,y)
start()
'''

# 마우스로 선 그리기


