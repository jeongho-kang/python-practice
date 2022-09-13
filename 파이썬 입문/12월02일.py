'''
# 레이블,엔트리,버튼 위젯 만들
from tkinter import *
win = Tk()   # win 에 Tk() 객체 저장

label = Label(win, text="Welcome, Please input your name")  # Label 생성
label.pack()     # pack으로 위치시키기

entry = Entry(win)
entry. pack()

button = Button(win, text="확인")
button.pack()

win.mainloop()  # 이벤트 처리를 위해 대기

#위젯에 옵션 추가하기
from tkinter import *
win = Tk()   # win 에 Tk() 객체 저장

label = Label(win, text="Welcome, Please input your name", bg="black", font="white")
label.pack()     # pack으로 위치시키기

entry = Entry(win,bd=50,cursor="pirate")
entry. pack()

button = Button(win, text="확인",fg="red",height=10)
button.pack()

win.mainloop()  # 이벤트 처리를 위해 대기


# 함수를 이용하여 버튼으로 동작 만들기
from tkinter import *

def buttonclick():
    end_text = entry.get()
    print(ent_text)
    label['fg'] = ent_text
    entry.delete

win = Tk()
win.title("버튼 이벤트 만들기")

label = Label(win,text = "아래 빈칸에 텍스트를 입력하세요",width=40)
entry = Entry(win, width=40)
button = Button(win,text="확인",width=40,bg="pink",command=buttonclick)
label.pack()
entry.pack()
button.pack()

win.mainloop()

#위젯을 격자로 배치 Grid Manager
from tkinter import *
r = Tk()
r.title("ID와 PW 입력창")
lb1 = Label(r, text="아이디")
lb2 = Label(r, text="비밀번호")
ent1 = Entry(r)
ent2 = Entry(r)
btn = Button(r, text = "확인")

lb1.grid(row=0 , collum=0)
ent1.grid(row=0 , column=1)
lb2.grid(row=1 , column=0)
ent2.grid(row=1,column=1)
btn.grid(row=2,column=1)

r.mainloop

#위젲의 위치를 지정하여 배치 place manager

from tkinter import *
r = Tk()
r.title("ID와 PW 입력창")
r.geometry("210*70")
lb1 = Label(r, text="아이디")
lb2 = Label(r, text="비밀번호")
ent1 = Entry(r)
ent2 = Entry(r)
btn = Button(r, text = "확인")
lb1.place(x=0,y=0) 
ent1.place(x=90 , y=0)
lb2.place(x= 0, y=20)
ent2.place(x=60,y=20)
btn.grid(x=60,y=40)

r.mainloop


#이벤트에 다양한 기능 싣기 - 바인딩

from tkinter import *
root = Tk()

def click(key) :
    print("왼쪽 마우스 클릭",key)
def click2(key) :
    print("오른쪽 마우스 클릭", key.x, key.y)
def click3(key) :
    print("키보드 입력", key.char)
    if key char == 'q'
    root.destroy()

root.bind("<Button-1>",click)
root.bind("<Button-3>",click2)
root.bind("<Key>",click3)

root.mainloop()

'''
# BMI 프로그램 만들기

from tkinter import *
root = Tk()
root.title("BMI 계산기")

def ok() :
    m = int(t.get()) / 100 #t.get()을 정수형으로
    bmi = round(int(k.get()) / (m*m),2) #round()로 소수점 이하 두 자리로 계산값 반환

    if bmi > 29.9:
        conclusion.config(bg="pink",fg="red",font="bold")
    elif bmi >= 26:
        conclusion.config(bg="yellow",fg="blue",font="bold")
    elif bmi >= 18.5:
        conclusion.config(bg="beige",fg="black",font="bold")
    else:
        conclusion.config(bg="gray",fg="black")

    conclusion.delete(0,END)
    conclusion.insert(0,"당신의 BMI 지수는 %s"%bmi) #ok 함수의 끝

tl = Label(root, text = "키(cm)")  #위젯 생성
kl = Label(root, text = "몸무게(kg)")
t = Entry(root)
k = Entry(root)
btn = Button(root, text = "결과확인", command =ok)

tl.grid(row=0,column=0)
kl.grid(row=1,column=0)
t.grid(row=0,column=1)
k.grid(row=1,column=1)
btn.grid(row=2,column=0,columnspan=2,ipadx=80)

conclusion = Entry(root, text="결과")
conclusion.grid(row=3,column=0,columnspan=2,ipadx=40)

root.mainloop()
