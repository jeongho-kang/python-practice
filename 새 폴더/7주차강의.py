# 수강 테이블에 있는 정보를 딕셔너리에 저장
'''
person_dic = {'Name':'홍길동', 'Age': 27,'Class':'초급'}
print(person_dic['Name']) ## 홍길동 이름 출력
print(person_dic['Age']) ## 나이 출력
person_dic.keys() ## 가지고 있는 키 항목만 묶어서 보여준다.
person_dic.values() ## value만 묶어서 출력
for x in person_dic.keys() : 
    print(x)
'''
# 모든 항목 출력하는 방법
'''
person_dic = {'Name':'홍길동', 'Age': 27,'Class':'초급'}
person_dic.items
for x in person_dic.items() :
    print(x)
for x, y in person_dic.items():
    print(x, ":", y)
'''
# 편의점 재고 관리 프로그램
'''
items = {"커피음료":7,"펜":3,"종이컵":2,"우유":1,"콜라":4,"책":5}
while True :
    name = input("물건의 이름을 입력하시오: ")
    if name == "" :
        break
    
    print(items.get(name))
print("프로그램을 종료합니다.")
'''
# 파티 동석 참석자 찾기
'''
partyA = set(["Park","Kim","Lee"])
partyB = set(["Park","Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA.intersection(partyB))
'''
