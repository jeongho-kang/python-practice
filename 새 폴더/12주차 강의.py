# 12주차 강의

# 맷플롯립 사용법
'''
import matplotlib,pyplot as plt
'''
# 선형차트 그리기
'''
import matplotlib.pyplot as plt

years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [67.0,80.0,257.0,1686.0,6505,11865.3,22105.3]

plt.plot(years, gdp, marker='o')
plt.title("GDP per capita")
plt.show()

'''
# 막대형 차트 그리기
'''
import matplotlib.pyplot as plt

years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [67.0,80.0,257.0,1686.0,6505,11865.3,22105.3]

plt.bar(years,gdp,width=5 color = "green") # 막대형 그래프
plt.title("GDP per capita")
plt.ylabel("dollars") # y축제목
plt.savefig("gdp.png", dpi = 600)
plt.show()
'''
# 분산형 차트 그리기
'''
import matplotlib.pyplot as plt
x = ['a','b','c','d','e']
y = [95, 69, 80, 73, 90]

plt.title('Scores by Group')
plt.xlabel('Group')
plt.ylabel('Score')
plt.grid()
plt.scatter(x,y, color = 'red')
plt.show()
'''
# 원형 차트 그리기
'''
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
times = [8,14,2]
timelabels = ["잠자기", "공부하기","놀기"]

plt.pie(times, labels=timelabels, autopct="%.2f")

plt.show()
'''
# 히스토그램 그리기
'''
import matplotlib.pyplot as plt

books = [1,6,2,3,1,2,0,2]
plt.hist(books, bins = 6)
plt.xlabel('Books')
plt.ylabel('Frequency')

plt.show()
'''
# 하나의 차트에 여러 데이터 표시하기

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(20)
y = x ** 2
z = x ** 3

plt.plot(x,x ,'ro--',label= 'linear')
plt.plot(x,y, 'g^-',label= 'quadratic')
plt.plot(x,z, 'b*:',label= 'qubic')
plt.legend() # 범례 표시하는 함수
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()

# 하나의 차트에 여러 데이터 표시하기 막대그래프
'''
import matplotlib.pyplot as plt
import numpy as np

years = [1960,1970,1980,1990,2000,2010]
ko = [130,650,2450,11600,17790,27250]
jp = [890,5120,11500,42130,40560,38780]
ch = [100,200,290,540,1760,7940]

xrange = np.arange(len(years))
width = 0.3

plt.bar(xrange-width, ko, width, label = "Korea")
plt.bar(xrange, jp, width, label = "Japan")
plt.bar(xrange+width, ch, width, label = "China")
plt.xticks(range(len(years)), years)
plt.legend()
plt.xlabel('years')
plt.ylabel('GDP')
plt.grid(true)

plt.show()
'''
# 그래프
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,10)
y = x * 2

plt.plot(x,y, 'bo-')
plt.axis([-20,20,-20,20])
plt.show()
'''
# 넘파이 난수로 그래프 그리기
'''
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.arange(1000)
y = np.random.rand(1000) * 3

plt.figure(figsize=(10,3))
plt.title("numbers")
plt.plot(x,y, marker='o' color= 'red')
plt.show()
'''
# 공공데이터의 활용

import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('한국도로공사.csv', delimiter = ',')

x = data[1:,0]
y = data[1:,1]

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(12,5),facecolor="lightyellow")
plt.bar(x,y, width=0.5, color = "darkgreen")
plt.xlabel("Year")
plt.ylabel("Number of accidents")
plt.title("연도별 교통사고통게")

plt.show()
















