from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="both")

# scrollbar.set에서 set이 없으면 스크롤을 내리면 바로 다시 올라간다.
# selectmode="extended" : 여러개를 동시에 선택 가능, selectmode="single" : 하나만 선택가능
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")    

scrollbar.config(command=listbox.yview) # 스크롤 바랑 리스트를 매칭시켜준다. 꼭 해야됨

root.mainloop()
