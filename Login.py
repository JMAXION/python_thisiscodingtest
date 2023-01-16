from tkinter import *
from tkinter import messagebox

import os
import csv
import pandas as pd
import question_main


def info_signup_comp():
    messagebox.showinfo("알림", "회원가입이 완료되었습니다.")


def info_warning():
    messagebox.showwarning("경고", "입력 정보를 확인하십시오.")


def info_login_comp():
    messagebox.showinfo("알림", "로그인이 완료되었습니다.")


# 회원가입창
def signup_main():

    signup = Tk()  # tkinter 클래스 선언
    signup.title("SIGN UP")  # 프레임 이름
    signup.geometry('350x600')  # 프레임 사이즈
    # signup.resizable(False, False) # 프레임 사이즈 고정 여부

    def sign_up():
        user_nickname = nickname_entry.get()
        user_name = username_entry.get()
        user_phonenum = phonenum_entry.get()
        user_pw = pw_entry.get()
        user_birth = birth_entry.get()

        if not os.path.isfile('Member.csv'):  # 'Member.csv' 파일이 없다면 파일을 생성
            df = pd.DataFrame(columns=['nickname', 'name', 'phonenum', 'pw', 'birth', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5'])
            df.to_csv("Member.csv", index=False)

        if user_nickname != '' and user_name != '' and user_phonenum != '' and user_pw != '' and user_birth != '':  # 입력받는 칸이 모두 빈칸이 아니라면
            data = pd.read_csv('./Member.csv')  # 'Member.csv' 파일읽기
            find = False

            nickname = data['nickname']
            phonenum = data['phonenum']

            for i in range(len(nickname)):
                if user_nickname == str(nickname[i]) or user_phonenum == str(phonenum[i]):  # 닉네임 혹은 핸드폰번호 중 하나라도 중복된다면
                    messagebox.showerror("알림", "중복된 정보가 존재합니다.")
                    find = True
                    break
            if not find:
                # 회원정보 저장
                f = open('Member.csv', 'a', newline='')
                wr = csv.writer(f)
                wr.writerow([user_nickname, user_name, user_phonenum, user_pw, user_birth])
                f.close()
                info_signup_comp()
                signup.destroy()
        else:
            info_warning()

    label = Label(signup, text="회원가입", width=20, font=("bold", 20))
    label.place(x=10, y=53)

    # 닉네임 입력
    uickname_labl = Label(signup, text="닉네임 :", width=20, font=("bold", 10))
    uickname_labl.place(x=10, y=130)

    nickname_entry = Entry(signup)
    nickname_entry.place(x=150, y=130)

    # 이름 입력
    username_labl = Label(signup, text="이름 :", width=20, font=("bold", 10))
    username_labl.place(x=10, y=180)

    username_entry = Entry(signup)
    username_entry.place(x=150, y=180)

    # 휴대폰번호 입력
    phonenum_labl = Label(signup, text="핸드폰번호 :", width=20, font=("bold", 10))
    phonenum_labl.place(x=10, y=230)

    phonenum_entry = Entry(signup)
    phonenum_entry.place(x=150, y=230)

    # 비밀번호 입력
    pw_labl = Label(signup, text="비밀번호 (4자리) :", width=20, font=("bold", 10))
    pw_labl.place(x=10, y=280)

    pw_entry = Entry(signup)
    pw_entry.place(x=150, y=280)

    # 생년월일 입력
    birth_labl = Label(signup, text="생년월일 (8자리) :", width=20, font=("bold", 10))
    birth_labl.place(x=10, y=330)

    birth_entry = Entry(signup)
    birth_entry.place(x=150, y=330)

    # Submit 버튼
    Button(signup, text='Submit', command=sign_up, width=20, bg='blue', fg='white').place(x=100, y=430)

    signup.mainloop()
    print("Sign Up is created successfully...")


# 로그인창
def signin_main():
    signin = Tk()  # tkinter 클래스 선언
    signin.title("SIGN IN")  # 프레임 이름
    signin.geometry('350x600')  # 프레임 사이즈
    # signin.resizable(False, False)

    def sign_in():
        user_phonenum = phonenum_entry.get()
        user_pw = pw_entry.get()

        if user_phonenum != '' and user_pw != '':
            data = pd.read_csv('./Member.csv')
            find = False

            phonenum = data['phonenum']
            pw = data['pw']

            for i in range(len(pw)):
                if user_phonenum == str(phonenum[i]) and user_pw == str(pw[i]):
                    info_login_comp()
                    signin.destroy()
                    find = True
                    question_main.main(i)
                    break
            if not find:
                info_warning()
        else:
            info_warning()

    label = Label(signin, text="로그인", width=20, font=("bold", 20))
    label.place(x=10, y=53)

    # 휴대폰번호 입력
    phonenum_labl = Label(signin, text="핸드폰번호 :", width=20, font=("bold", 10))
    phonenum_labl.place(x=10, y=200)

    phonenum_entry = Entry(signin)
    phonenum_entry.place(x=150, y=200)

    # 비밀번호 입력
    pw_labl = Label(signin, text="비밀번호 (4자리) :", width=20, font=("bold", 10))
    pw_labl.place(x=10, y=250)

    pw_entry = Entry(signin)
    pw_entry.place(x=150, y=250)

    # 로그인 버튼
    Button(signin, text='sign in', command=sign_in, width=20, bg='blue', fg='white').place(x=100, y=350)

    # 회원가입 버튼
    signup_labl = Label(signin, text="New User :", width=20, font=("bold", 10))
    signup_labl.place(x=30, y=480)
    Button(signin, text='sign up', command=signup_main, width=15, bg='gray', fg='white').place(x=160, y=480)

    signin.mainloop()
    print("Sign In is created successfully...")


if __name__ == '__main__':
    signin_main()
