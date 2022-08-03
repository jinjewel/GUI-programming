from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름
#root.geometry("640x480+100+300") # 크기( 가로 x 세로 + x좌표 + y좌표)
root.geometry("640x480")

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가(창 크기 변경 불가)


root.mainloop()
