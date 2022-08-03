from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

Label(root, text="메뉴를 선택해주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 메뉴

frame_burger = Frame(root, relief="solid", bd=1) # relief="solid" : 테두리 모양? , bd=1 : 외각선 두께 표시
frame_burger.pack(side="left", fill="both", expand=True) 
# side : 위치 설정, fill="both" : 아래로 끝까지 채우는 설정(창을 확대해도 적용), expand=True : 좌우로 창을 채우는 설정, 여러개가 있으면 동일한 비율로 채워짐(창을 확대해도 적용)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료

frame_drink = LabelFrame(root, text="음료") # LabelFrame : 레이블이 들어간 프레임
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()
