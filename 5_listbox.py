from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

listbox = Listbox(root, selectmode="extended", height=0) 
# selectmode="extended" : 여러개를 동시에 선택 가능, selectmode="single" : 하나만 선택가능
# height= 창에 리스트가 보이는 갯수, 0: 리스트가 포함하고 있는 모든 갯수, 1 : 한줄, 2: 두줄 등등 
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤에 있는 항목을 삭제 
    # listbox.delete(0) # 맨 앞에 있는 항목을 삭제 

    # 갯수 확인
    # print("리스트에는 ", listbox.size(), "개가 있어요")

    # 항목 확인 (시작idx, 끝 idx)
    # print("첫번째부터 세번째까지의 항목 :", listbox.get(0,2))

    # 선택된 항목 확인 (idx값으로 반환)
    print("선택된 항목 : ", listbox.curselection() )

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
