from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

label1= Label(root, text="안녕하세요") # 단순히 창에 텍스트를 집어 넣기
label1.pack()

photo = PhotoImage(file = "C:\ohcoding\GUI programming\gui_basic\img.png")
label2 = Label(root, image=photo)
label2.pack()

def change(): # 이미 노출된 텍스트와 이미지를 바꾸는 방법
    label1.config(text="또 만나요")

    global photo2 # 지역 변수로 지정이 되면서 함수 밖으로 나가면 쓰레기 값이 저장되기 때문에 전역 변수로 변환해준다.
    photo2 = PhotoImage(file="C:\ohcoding\GUI programming\gui_basic\img2.png")
    label2.config(image=photo2)

btn = Button(root, text="틀릭", command=change)
btn.pack()    

root.mainloop()
