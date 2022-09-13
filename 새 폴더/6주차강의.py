# 좋아하는 과일 리스트를 만들고 검색하기
'''
fruit = []
for x in range(4) :
     name = input("좋아하는 과일을 입력하세요: ")
     fruit.append(name)
name = input("검색할 과일 이름: ")
if name in fruit :
    print("당신이 좋아하는 과일 입니다.")
else :
    print("당신잊 좋아하는 과일이 아닙니다.")
    '''
# 5명의 점수 합계를 구해 출력
'''
numbers = [92,85,96,70,63]
total = 0
for x in numbers :
    total = total + x
print("합계: ",total)
'''
# 도시 인구 구하기
'''
population = ["서울",9765, "부산",3441,"인천",2954]
print("서울의 인구: ", population[1])
print("인천의 인구: ", population[-1])
print("도시 목록: "population[::2])
print("인구의 합: "sum(population[1::2]))
'''
# 스크린 세이버 만들기
'''
import turtle as t
import random as r

x,y,radius = 0,0,0
color = ['red','blue','yellow','green','orange']
t.setup(1200.800)
t.bgcolor('black')
t.speed(7)

for _ in range(30) :
    x = r.randint(-500,500)
    y = r.randint(-350,300)
    radius = r.randint(80,130)
    
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.color(r.choice(color))
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
'''
# 10명의 점수가 튜플에 저장되어 있을 떄,

numbers = (73,64,98,57,39,79,93,87,57,69)
print("최대값 : ", max(numbers))
print("최소값 : ", min(numbers))
print("평균 : ", sum(numbers) / len(numbers))
n_list = list(numbers)
n_list.sort(reverse=True) ## 큰값부터 작은값으로 내림차순 정렬
print("정렬 : ", tuple(n_list))





