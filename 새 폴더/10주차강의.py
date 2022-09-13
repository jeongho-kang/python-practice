# 카이사르 암호 만들기
'''
import string
src = string.ascii_uppercase
dst = src[3:] + src[:3]

sentence = input("문장을 입력하시오 ; ")
sentence = sentence.upper()

print("암호화된 문장 : ", end = "")
for ch in sentence :
    if ch in src :
        print(dts[src.index(ch)], end = "") 
    else:
        print(ch, end = "")
'''
# 단어사전 만들기
'''
dic = []
print("문장을 입력하면 단어를 등록합니다 (종료는0): ")
while True :
    sentence = input("문장 입력: ")
    if sentence == '0' :
        break

    words = sentence.split()
    for x in words :
        if x not in dic :
            dic.append(x)

print("******단어사전******")
for x in sorted(dic) :
    print(x)
'''
# 단어 찾아 바꾸기
'''
try :
    f = open("poem.txt", "r+")
except :
    print("파일을 확인하세요.")
else :
    text = f.read()
    print(text)
    print('-' * 10)

    old = input("찾을 내용 : ")
    new = input("바꿀 내용 : ")

    print(text.count(old), "번을 바꿉니다.")
    text = text.replace(old, new)
    f.seek(0)
    f.write(text)
    f.close
'''
# 워드클라우드
'''
from wordcloud import *
try :
    f = open("frost.txt","r")
except :
    print("파일을 확인하세요.")
else :
    text = f.read()
    f.close()

    wc = WordCloud()
    wc.generate(text)
    wc.to_file('frost.png')
'''
# 워드클라우드
'''
from wordcloud import *
try :
    f = open("poem.txt","r")
except :
    print("파일을 확인하세요.")
else :
    text = f.read()
    f.close()

    wc = WordCloud(font_path = "c:/Windows/Fonts/Hancom Gothic Bold.ttf",
                   background_color = "white", width = 2000, height = 1500)
    wc.generate(text)
    wc.to_file('poem.png')
'''
# 워드클라우드 중지어 추가
from wordcloud import *
try :
    f = open("poem.txt","r")
except :
    print("파일을 확인하세요.")
else :
    text = f.read()
    f.close()

    swords = STOPWORDS.union({'않고','있으랴'})
    wc = WordCloud(font_path = "c:/Windows/Fonts/Hancom Gothic Bold.ttf",
                   background_color = "white", width = 2000, height = 1500,
                   stopwords = swords)
    wc.generate(text)
    wc.to_file('poem.png')
































    
