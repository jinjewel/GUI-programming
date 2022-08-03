from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정

################## 창 크기 및 변경 설정 ####################################################3

# root.geometry("640x480+100+300") # 크기( 가로 x 세로 + x좌표 + y좌표)
# root.geometry("640x480")
# root.resizable(False, False) # x(너비), y(높이) 값 변경 불가(창 크기 변경 불가)

############################################################################################

################# 버튼 크기, 이름, 색상, 이미지, 동작 등 설정하기 #############################
btn1 = Button(root, text="버튼1") # 버튼 선언(어디창에 저장할건지, 이름은 뭐로 할건지) 
btn1.pack() # 실제로 창에 보이게 해줌/ 없으면 창에 안보임

btn2 = Button(root, padx=5, pady=10, text="버튼2") # 버튼 선언(어디창에 저장할건지, 상대적 버튼의 너비, 상대적 버튼의 높이, 이름은 뭐로 할건지) 
btn2.pack() # 실제로 창에 보이게 해줌

btn3 = Button(root, padx=10, pady=20, text="버튼3") # 버튼 선언(어디창에 저장할건지, 이름기준 상대적 버튼의 너비, 이름기준 상대적 버튼의 높이, 이름은 뭐로 할건지) 
btn3.pack() # 실제로 창에 보이게 해줌

btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼 선언(어디창에 저장할건지, 절대적 버튼의 너비, 절대적 버튼의 높이, 이름은 뭐로 할건지)
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # 버튼 이름과 배경에 색상 집어넣기
btn5.pack()

photo = PhotoImage(file="C:\ohcoding\GUI programming\gui_basic\img.png") # 사용한 사진을 가져오기
btn6 = Button(root, image =photo) # 버튼을 텍스트가 아닌 그림으로 만들기
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd ) # 버튼이 눌렸을때 실행하도록 하는 방법
btn7.pack()

############################################################################################


root.mainloop()
