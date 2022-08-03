import time
import tkinter.ttk as ttk
from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") 
# mode="indeterminate" : 짧은 바가 시작하여 끝나는 부분없이 왔다갔다를 반복하는 상태
# mode="determinate" : 바가 처음부터 이어져서 끝까지 이어지는 상태, 끝나면 다시 시작

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") 

# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지, 프로그램 바가 사라진다.


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 실수 단위로 퍼센테이지가 올라가기 위해서
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2) # length=150 : 상대바의 길이를 조절
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progressbar의 값을 설정, 1부터 100까지 올라가는 것
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop()
