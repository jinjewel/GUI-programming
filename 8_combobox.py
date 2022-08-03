import tkinter.ttk as ttk
from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values) # height=5 목록이 5개까지 보임 
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") 
# height=10 : 목록이 10개까지 보임, state="readonly" 쓰지못하고 읽기만 할 수 있도록 함
readonly_combobox.current(0) # 0번째 인덱스 값을 기본값으로 설정
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
