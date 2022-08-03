from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("800x500")

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# # btn1.pack(side="left")
# # btn2.pack(side="left")

# btn1.grid(row=0,column=0)
# btn2.grid(row=0,column=1)

# 맨 윗줄
# padx : 한칸의 너비(가로)를 상대적으로 지정 , pady : 한칸의 높이(세로)를 상대적으로 지정
# width : 한칸의 너비(가로)를 절대적으로 지정 , height : 한칸의 높이(세로)를 절대적으로 지정
btn_f16 = Button(root, text="F16", width=5, height=3)
btn_f17 = Button(root, text="F17", width=5, height=3)
btn_f18 = Button(root, text="F18", width=5, height=3)
btn_f19 = Button(root, text="F19", width=5, height=3)

# grid -> row : x 좌표, column : y좌표 , sticky=N+E+W+S : 동서남북 방향으로 늘려서 칸을 채우라는 뜻 padx : 칸 사이의 너비(가로)를 지정 , pady : 칸 사이의 높이(세로)를 지정
btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 2번째 줄

btn_clear = Button(root, text="clear", width=5, height=3)
btn_equal = Button(root, text="=", width=5, height=3)
btn_div = Button(root, text="/", width=5, height=3)
btn_mul = Button(root, text="*", width=5, height=3)

# grid -> row : x 좌표, column : y좌표 , sticky=N+E+W+S : 동서남북 방향으로 늘려서 칸을 채우라는 뜻
btn_clear.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 3번재 줄

btn_7 = Button(root, text="7", width=5, height=3)
btn_8 = Button(root, text="8", width=5, height=3)
btn_9 = Button(root, text="9", width=5, height=3)
btn_sub = Button(root, text="-", width=5, height=3)

# grid -> row : x 좌표, column : y좌표 , sticky=N+E+W+S : 동서남북 방향으로 늘려서 칸을 채우라는 뜻
btn_7.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4번째 줄

btn_4 = Button(root, text="4", width=5, height=3)
btn_5 = Button(root, text="5", width=5, height=3)
btn_6 = Button(root, text="6", width=5, height=3)
btn_add = Button(root, text="+", width=5, height=3)

# grid -> row : x 좌표, column : y좌표 , sticky=N+E+W+S : 동서남북 방향으로 늘려서 칸을 채우라는 뜻
btn_4.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 5번째 줄

btn_1 = Button(root, text="1", width=5, height=3)
btn_2 = Button(root, text="2", width=5, height=3)
btn_3 = Button(root, text="3", width=5, height=3)
btn_enter = Button(root, text="enter", width=5, height=3)

# grid -> row : x 좌표, column : y좌표 , sticky=N+E+W+S : 동서남북 방향으로 늘려서 칸을 채우라는 뜻
btn_1.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4,column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # 로우(y축)를 2개 합치겠다는 뜻 

# 마지막 줄

btn_0 = Button(root, text="0", width=5, height=3)
btn_jum = Button(root, text=".", width=5, height=3)

# grid -> row : x 좌표, column : y좌표 , sticky=N+E+W+S : 동서남북 방향으로 늘려서 칸을 채우라는 뜻
btn_0.grid(row=5,column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) # 컬럼(x축)을 2개 합치겠다는 뜻
btn_jum.grid(row=5,column=2, sticky=N+E+W+S, padx=3, pady=3)



root.mainloop()
