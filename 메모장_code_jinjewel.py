import os
from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

# 메모장 이름, 크기 

root = Tk()
root.title("제목 없음 - Windows 메모장(made jinjewel)") 
root.geometry("600x400+500+300")

# 스크롤 바 (창 y축 전체) 

scrollbar_y = Scrollbar(root)
scrollbar_y.pack(side="right", fill="both")

# 메모 부분만들기.

txt = Text(root, yscrollcommand=scrollbar_y.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar_y.config(command=txt.yview)

# 메뉴 - 파일, 편집, 서식, 보기, 도움말 만들기

menu = Menu(root)

# 메뉴

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file: 
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) 

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file )

# 편집,서식, 보기, 도움말 만들기

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")


root.config(menu=menu)
root.mainloop()