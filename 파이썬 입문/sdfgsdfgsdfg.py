month = int(input("아이가 태어난 지 몇 개월 입니까 ? "))
if  0 <= month <= 1 :
  print("결핵,B형간염 예방접종 대상자 입니다.")
  
if 0 <= month <= 2 :
  print("B형간염,파상풍,폐렴구균 대상자 입니다.")
  
if month >= 2 and month <= 6 :
  print("파상풍,폐렴구균 대상자 입니다.")
  
if month >= 7 and month <= 15 :
  print("폐렴구균 대상자 입니다.")
