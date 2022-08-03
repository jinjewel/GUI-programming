import tkinter.messagebox as msgbox
from tkinter import * # tkinter 모듈안에 있는 것들을 쓰기 위해 선언

root = Tk()
root.title("Jinseok GUI") # 이름 설정
root.geometry("500x300")

# 기차 예메 시스템이라고 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매가 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당좌석은 매진이 되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생하였습니다.")

def okcancel():
    msgbox.askokcancel("확인/취소", "해당 좌석은 유아동반석 입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시도/ 취소", "일시적인 오류입니다. 다시 시도하시겠습니다.")
    print("응답: ", response) # True, False -> 예 : 1, 아니오 : 0
    if response == 1:
        print("재시도")
    elif response == 0:
        print("취소")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답: ", response) # True, False, None -> 예 : 1, 아니오 : 0, 그 외
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")


Button(root, text="알림", command=info).pack()
Button(root, text="경고", command=warn).pack()
Button(root, text="에러", command=error).pack()

Button(root, text="확인 취소", command=okcancel).pack()
Button(root, text="재시도 취소", command=retrycancel).pack()
Button(root, text="예 아니오", command=yesno).pack()
Button(root, text="예 아니오 취소", command=yesnocancel).pack()


root.mainloop()
