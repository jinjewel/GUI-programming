from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴 (빈 값)
edit_file = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_file)

# Language 메뉴 추가 (radio 버튼을 통해서 택 1)

lang_file = Menu(menu, tearoff=0)
lang_file.add_radiobutton(label="Python")
lang_file.add_radiobutton(label="Jave")
lang_file.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=lang_file)

# View 메뉴 추가 (체크 박스 사용)

view_file = Menu(menu, tearoff=0)
view_file.add_checkbutton(label="Show Minimap")
view_file.add_separator()
view_file.add_command(label="hahaha")
menu.add_cascade(label="View", menu=view_file)

root.config(menu=menu)
root.mainloop()
