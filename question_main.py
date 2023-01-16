from tkinter import messagebox as mbox

import tkinter as tk
import capture_face as cam
import csv
import pandas as pd
import random



def main(idx):
    # tkinter 클래스 선언
    window = tk.Tk()
    # 프레임 이름
    window.title("QUESTION")
    # 프레임 크기
    window.geometry("350x600")

    camera_image = tk.PhotoImage(file="camera_image.png")

    LFont = ("bold", 15)
    SFont = ("bold", 10)

    # 로그인한 사용자 인덱스
    user_idx = idx

    # 프레임 선언
    mainframe = tk.Frame(window)
    tutorial_frame = tk.Frame(window)
    question_frame1 = tk.Frame(window)
    question_frame2 = tk.Frame(window)
    question_frame3 = tk.Frame(window)
    question_frame4 = tk.Frame(window)
    question_frame5 = tk.Frame(window)
    result_frame = tk.Frame(window)
    return_frame = tk.Frame(window)

    # 모든 프레임 같은 층에 둠
    mainframe.grid(row=0, column=0, sticky="nsew")
    tutorial_frame.grid(row=0, column=0, sticky="nsew")
    question_frame1.grid(row=0, column=0, sticky="nsew")
    question_frame2.grid(row=0, column=0, sticky="nsew")
    question_frame3.grid(row=0, column=0, sticky="nsew")
    question_frame4.grid(row=0, column=0, sticky="nsew")
    question_frame5.grid(row=0, column=0, sticky="nsew")
    result_frame.grid(row=0, column=0, sticky="nsew")
    return_frame.grid(row=0, column=0, sticky="nsew")

    # 감정 결과의 인덱스를 저장하는 리스트
    result_idx = [6, 6, 6, 6, 6]

    # 감정 출력 함수
    def switch(key):
        emotion = {0: "분노", 1: "행복",
                   2: "너무 싫음", 3: "놀람",
                   4: "슬픔", 5: "무표정"}.get(key, "None")
        return emotion

    # 원하는 프레임을 최상단으로 올리는 함수
    def openFrame(frame):
        frame.tkraise()

    # 튜토리얼 함수
    def Tutorial(frame, tutorial_label):
        frame.tkraise()
        face = cam.main(0)
        emotion = switch(face)
        tutorial_label.configure(text=("인식된 감정은 " + emotion + "입니다.\n"
                                                              "다시 해보기 버튼을 누르면 카메라 튜토리얼을 다시 실행합니다.\n"
                                                              "질문 시작 버튼을 눌러 질문을 시작합니다.")
                                 , font=LFont, wraplength=280)
        tutorial_label.place(x=40, y=40)

    # 튜토리얼 라벨 함수
    def TutoLabel(tutorial_label):
        # 튜토리얼 라벨
        tutorial_label.configure(text="화면 중앙에서 표정을 지어주세요.\n"
                                      "1번을 눌러 사진을 찍을 수 있습니다.\n"
                                      "인식 가능한 감정은 무표정, 행복, 분노, 너무 싫음, 놀람, 슬픔입니다."
                                 , font=LFont, wraplength=280)
        tutorial_label.place(x=45, y=40)

    # 얼굴 캡쳐 함수
    def Capture(num, btn):
        face = cam.main(num)
        emotion = switch(face)
        mbox.showinfo("인식 결과", "인식된 감정은 " + emotion + "입니다.")
        btn['state'] = tk.NORMAL
        btn['bg'] = 'blue'
        result_idx[num - 1] = face

    # 질문 출력 함수
    def question1():
        question_frame1.tkraise()

        # 질문 라벨
        question_label = tk.Label(question_frame1, text="질문 1\n"
                                                        "다음과 같은 말을 들으면 어떤 표정을 지을 것 같나요?"
                                  , font=LFont, wraplength=280)
        question_label.place(x=50, y=20)

        # 사진 출력
        picture = tk.PhotoImage(file="question1_re.png")
        picture_label = tk.Label(question_frame1, image=picture)
        picture_label.place(x=70, y=90)
        picture_label.picture = picture

        # 얼굴 캡쳐 버튼
        btnToCapture = tk.Button(question_frame1, image=camera_image,
                                 command=lambda: [Capture(1, btnToNext)])
        btnToCapture.place(x=150, y=450)

        # 다음으로 넘어가기 버튼
        btnToNext = tk.Button(question_frame1, text="다음 질문 >>", width=15, height=3,
                              command=lambda: [question2()], state=tk.DISABLED, fg='white')
        btnToNext.place(x=200, y=530)

        # 뒤로가기 버튼
        btnToPrevious = tk.Button(question_frame1, text="<< 이전으로", width=15, height=3,
                                  command=lambda: [openFrame(mainframe)], bg='gray', fg='white')
        btnToPrevious.place(x=50, y=530)

    def question2():
        question_frame2.tkraise()

        # 질문 라벨
        question_label = tk.Label(question_frame2, text="질문 2\n"
                                                        "다음과 같은 상황에 처한다면 어떤 표정을 지을 것 같나요?"
                                  , font=LFont, wraplength=280)
        question_label.place(x=50, y=20)

        # 사진 출력
        picture = tk.PhotoImage(file="question2_re.png")
        picture_label = tk.Label(question_frame2, image=picture)
        picture_label.place(x=50, y=90)
        picture_label.picture = picture

        # 얼굴 캡쳐 버튼
        btnToCapture = tk.Button(question_frame2, image=camera_image,
                                 command=lambda: [Capture(2, btnToNext)])
        btnToCapture.place(x=150, y=450)

        # 다음으로 넘어가기 버튼
        btnToNext = tk.Button(question_frame2, text="다음 질문 >>", width=15, height=3,
                              command=lambda: [question3()], state=tk.DISABLED, fg='white')
        btnToNext.place(x=200, y=530)

        # 뒤로가기 버튼
        btnToPrevious = tk.Button(question_frame2, text="<< 이전으로", width=15, height=3,
                                  command=lambda: [question1()], bg='gray', fg='white')
        btnToPrevious.place(x=50, y=530)

    def question3():
        question_frame3.tkraise()

        # 질문 라벨
        question_label = tk.Label(question_frame3, text="질문 3\n"
                                                        "이런 농담을 들으면 어떤 표정을 지을 것 같나요?"
                                  , font=LFont, wraplength=280)
        question_label.place(x=60, y=20)

        # 사진 출력
        picture = tk.PhotoImage(file="question3_re.png")
        picture_label = tk.Label(question_frame3, image=picture)
        picture_label.place(x=60, y=130)
        picture_label.picture = picture

        # 얼굴 캡쳐 버튼
        btnToCapture = tk.Button(question_frame3, image=camera_image,
                                 command=lambda: [Capture(3, btnToNext)])
        btnToCapture.place(x=150, y=450)

        # 다음으로 넘어가기 버튼
        btnToNext = tk.Button(question_frame3, text="다음 질문 >>", width=15, height=3,
                              command=lambda: [question4()], state=tk.DISABLED, fg='white')
        btnToNext.place(x=200, y=530)

        # 뒤로가기 버튼
        btnToPrevious = tk.Button(question_frame3, text="<< 이전으로", width=15, height=3,
                                  command=lambda: [question2()], bg='gray', fg='white')
        btnToPrevious.place(x=50, y=530)

    def question4():
        question_frame4.tkraise()

        # 질문 라벨
        question_label = tk.Label(question_frame4, text="질문 4\n"
                                                        "다음과 같은 상황에 어떤 표정을 지을 것 같나요?\n"
                                                        "(열심히 해준 음식이 맛이 없을 때)"
                                  , font=LFont, wraplength=280)
        question_label.place(x=50, y=20)

        # 사진 출력
        picture = tk.PhotoImage(file="question4_re.png")
        picture_label = tk.Label(question_frame4, image=picture)
        picture_label.place(x=60, y=130)
        picture_label.picture = picture

        # 얼굴 캡쳐 버튼
        btnToCapture = tk.Button(question_frame4, image=camera_image,
                                 command=lambda: [Capture(4, btnToNext)])
        btnToCapture.place(x=150, y=450)

        # 다음으로 넘어가기 버튼
        btnToNext = tk.Button(question_frame4, text="다음 질문 >>", width=15, height=3,
                              command=lambda: [question5()], state=tk.DISABLED, fg='white')
        btnToNext.place(x=200, y=530)

        # 뒤로가기 버튼
        btnToPrevious = tk.Button(question_frame4, text="<< 이전으로", width=15, height=3,
                                  command=lambda: [question3()], bg='gray', fg='white')
        btnToPrevious.place(x=50, y=530)

    def question5():
        question_frame5.tkraise()

        # 질문 라벨
        question_label = tk.Label(question_frame5, text="질문 5\n"
                                                        "다음과 같은 상황에 어떤 표정을 지을 것 같나요?"
                                  , font=LFont, wraplength=280)
        question_label.place(x=70, y=20)

        # 사진 출력
        picture = tk.PhotoImage(file="question5_re.png")
        picture_label = tk.Label(question_frame5, image=picture)
        picture_label.place(x=40, y=120)
        picture_label.picture = picture

        # 얼굴 캡쳐 버튼
        btnToCapture = tk.Button(question_frame5, image=camera_image,
                                 command=lambda: [Capture(5, btnToNext)])
        btnToCapture.place(x=150, y=450)

        # 다음으로 넘어가기 버튼
        btnToNext = tk.Button(question_frame5, text="결과 보기", width=15, height=3,
                              command=lambda: [result()], state=tk.DISABLED, fg='white')
        btnToNext.place(x=200, y=530)

        # 뒤로가기 버튼
        btnToPrevious = tk.Button(question_frame5, text="<< 이전으로", width=15, height=3,
                                  command=lambda: [question4()], bg='gray', fg='white')
        btnToPrevious.place(x=50, y=530)

    # 결과 출력 함수
    def result():
        result_frame.tkraise()

        result_label = tk.Label(result_frame, text="나의 결과", font=LFont)
        result_label.place(x=140, y=50)
        indicate_label1 = tk.Label(result_frame, text="질문 1", font=LFont)
        indicate_label1.place(x=75, y=80)
        indicate_label2 = tk.Label(result_frame, text="질문 2", font=LFont)
        indicate_label2.place(x=230, y=80)
        indicate_label3 = tk.Label(result_frame, text="질문 3", font=LFont)
        indicate_label3.place(x=75, y=210)
        indicate_label4 = tk.Label(result_frame, text="질문 4", font=LFont)
        indicate_label4.place(x=230, y=210)
        indicate_label5 = tk.Label(result_frame, text="질문 5", font=LFont)
        indicate_label5.place(x=155, y=340)

        img1 = tk.PhotoImage(file='resized1.PNG')
        img2 = tk.PhotoImage(file='resized2.PNG')
        img3 = tk.PhotoImage(file='resized3.PNG')
        img4 = tk.PhotoImage(file='resized4.PNG')
        img5 = tk.PhotoImage(file='resized5.PNG')

        label1 = tk.Label(result_frame, image=img1)
        label1.img1 = img1
        label2 = tk.Label(result_frame, image=img2)
        label2.img2 = img2
        label3 = tk.Label(result_frame, image=img3)
        label3.img3 = img3
        label4 = tk.Label(result_frame, image=img4)
        label4.img4 = img4
        label5 = tk.Label(result_frame, image=img5)
        label5.img5 = img5

        label1.place(x=40, y=105)
        label2.place(x=195, y=105)
        label3.place(x=40, y=235)
        label4.place(x=195, y=235)
        label5.place(x=120, y=365)

        print(result_idx)

        # 매칭하기 버튼
        btnToMatch = tk.Button(result_frame, text="Match!", width=15, height=3,
                               command=lambda: [return_result()], fg='blue')
        btnToMatch.place(x=130, y=510)

    # 매칭 함수
    def return_result():
        return_frame.tkraise()

        face_match = [0]
        matched = []

        data = pd.read_csv('./Member.csv')

        data.loc[idx, 'Q1'] = result_idx[0]
        data.loc[idx, 'Q2'] = result_idx[1]
        data.loc[idx, 'Q3'] = result_idx[2]
        data.loc[idx, 'Q4'] = result_idx[3]
        data.loc[idx, 'Q5'] = result_idx[4]

        # 데이터 불러오기
        q1 = data['Q1']
        q2 = data['Q2']
        q3 = data['Q3']
        q4 = data['Q4']
        q5 = data['Q5']
        nickname = data['nickname']
        phonenum = data['phonenum']

        df = pd.DataFrame(data)
        df.to_csv("./Member.csv", index=False)


        # 같은 질문에 같은 표정 지은 횟수 집계
        for i in range(len(nickname)):
            face_match.insert(i, 0)
            if result_idx[0] == q1[i]:
                face_match[i] += 1
            if result_idx[1] == q2[i]:
                face_match[i] += 1
            if result_idx[2] == q3[i]:
                face_match[i] += 1
            if result_idx[3] == q4[i]:
                face_match[i] += 1
            if result_idx[4] == q5[i]:
                face_match[i] += 1

        # 매칭할 사람의 인덱스 추출 (많이 일치하는 순으로)
        for j in range(5, 1, -1):
            for k in range(len(face_match)):
                if face_match[k] == j:
                    matched.append(k)

            # 자기 자신 제거
            if idx in matched:
                matched.remove(idx)
            if len(matched) >= 2:
                break

        random_match = random.sample(matched, 2)

        # 추천 라벨
        match_label = tk.Label(return_frame, text="2명의 상대가 매칭되었습니다 !"
                               , font=LFont, wraplength=280)
        match_label.place(x=40, y=40)

        # 매칭 상대 1 라벨
        match1_label = tk.Label(return_frame, text="매칭 상대 1 : ", font=SFont)
        match1_label.place(x=20, y=120)

        match1_nickname_label = tk.Label(return_frame, text="닉네임 : " + nickname[random_match[0]], font=("bold", 12))
        match1_nickname_label.place(x=110, y=160)

        match1_phonenum_label = tk.Label(return_frame, text="연락처 : " + phonenum[random_match[0]], font=("bold", 12))
        match1_phonenum_label.place(x=110, y=200)

        profile1 = tk.PhotoImage(file="profile1.png")
        match1_profile_label = tk.Label(return_frame, image=profile1)
        match1_profile_label.place(x=20, y=150)
        match1_profile_label.profile1 = profile1

        # 매칭 상대 2 라벨
        match2_label = tk.Label(return_frame, text="매칭 상대 2 : ", font=SFont)
        match2_label.place(x=20, y=290)

        match2_nickname_label = tk.Label(return_frame, text="닉네임 : " + nickname[random_match[1]], font=("bold", 12))
        match2_nickname_label.place(x=110, y=330)

        match2_phonenum_label = tk.Label(return_frame, text="연락처 : " + phonenum[random_match[1]], font=("bold", 12))
        match2_phonenum_label.place(x=110, y=370)

        profile2 = tk.PhotoImage(file="profile2.png")
        match2_profile_label = tk.Label(return_frame, image=profile2)
        match2_profile_label.place(x=20, y=320)
        match2_profile_label.profile2 = profile2

        # 메인으로 돌아가기 버튼
        btnToFirst = tk.Button(return_frame, text="처음으로", width=15, height=3,
                               command=lambda: [openFrame(mainframe)], bg='orange', fg='white')
        btnToFirst.place(x=125, y=450)

        # 종료 버튼
        btnToQuit = tk.Button(return_frame, text="종료하기", width=15, height=3,
                              command=btn_to_quit, bg='gray', fg='white')
        btnToQuit.place(x=125, y=510)

    # 종료 함수
    def btn_to_quit():
        return_frame.destroy()
        return_frame.quit()
        exit()

    # 메인프레임 열기
    openFrame(mainframe)

    # 메인 라벨
    question_label = tk.Label(mainframe, text="질문 시작 버튼을 누르면 질문이 순서대로 출력됩니다.\n"
                                              "튜토리얼 실행 버튼을 누르면 카메라 튜토리얼을 실행합니다.\n"
                              , font=LFont, wraplength=280)
    question_label.place(x=45, y=40)

    # 튜토리얼 라벨
    tutorial_label = tk.Label(tutorial_frame, text="화면 중앙에서 표정을 지어주세요.\n"
                                                   "1번을 눌러 사진을 찍을 수 있습니다.\n"
                                                   "인식 가능한 감정은 무표정, 행복, 분노, 너무 싫음, 놀람, 슬픔입니다."
                              , font=LFont, wraplength=280)
    tutorial_label.place(x=45, y=40)

    # 버튼 선언
    btnToQuestion1 = tk.Button(mainframe, text="질문 시작", width=20, height=3, font=SFont,
                               command=lambda: [question1()], bg='blue', fg='white')
    btnToQuestion1.grid(row=1, column=0, padx=95, pady=30)

    btnToTutorial = tk.Button(mainframe, text="튜토리얼 실행", width=20, height=3, font=SFont,
                              command=lambda: [Tutorial(tutorial_frame, tutorial_label)], bg='gray', fg='white')
    btnToTutorial.grid(row=0, column=0, padx=95, pady=330, rowspan=4)

    btnToMain = tk.Button(tutorial_frame, text="뒤로가기", width=20, height=3, font=SFont,
                          command=lambda: [openFrame(mainframe), TutoLabel(tutorial_label)], bg='gray', fg='white')
    btnToMain.place(x=95, y=350)

    btnToRecapture = tk.Button(tutorial_frame, text="다시 해보기", width=20, height=3, font=SFont,
                               command=lambda: [Tutorial(tutorial_frame, tutorial_label)])
    btnToRecapture.place(x=95, y=290)

    btnToQuestion1_1 = tk.Button(tutorial_frame, text="질문 시작", width=20, height=3, font=SFont,
                                 command=lambda: [question1(), TutoLabel(tutorial_label)], bg='blue', fg='white')
    btnToQuestion1_1.place(x=95, y=230)

    # 무한루프 돌림 (return 0같은 느낌)
    mainframe.mainloop()


if __name__ == '__main__':
    main(0)
