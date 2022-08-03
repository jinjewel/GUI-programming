from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

txt = Text(root, width=30, height=5) # 단순 입력의 텍스트 위젯을 만듬, 엔터가 가능한 테스트를 입력받을때 사용한다.
txt.pack()

txt.insert(END, "글자를 입력하세요") # 미리 텍스드 위젯에 설명 글처럼 적어 두는 방법

e = Entry(root, width=30) # 엔터가 안되는 한줄의 텍스트를 입력받을때 사용한다. 로그인, 비번 등 입력받을시 사용
e.pack()
e.insert(END, "한줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 첫번째 줄, 왼쪽부터 0번째 위치부터 END까지 가져온다
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END) # 첫번째 줄, 왼쪽부터 0번째 위치부터 END까지 삭제한다.
    e.delete(0, END) # entry는 한줄로 입력되기 때문에 왼쪽부터 0번째 위치부터 END까지 삭제한다.

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
