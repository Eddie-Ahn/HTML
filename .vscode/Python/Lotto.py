# 로또 번호 계산기 tkinter 활용

from cgitb import text
from tkinter import *  #tkinter 모듈 불러오기

'''
로또 번호 생성기 함수 만들기, 
함수는 미리 만들어놔도 됨. 나중에 해당 함수를 쓸 때
미리 수행한 함수를 콜백 (실행을 위하여 불러옴) 함'''
   
def lotto_creator():
    import random
    num_list = []
    for i in range(46):
        num_list.append(i+1)
    
    #random 모듈의 sample 메소드로, 대상 변수와 뽑을 갯수 숫자 정의
    lotto_number_raw = random.sample(num_list, 6)
    # 리스트로 출력시 쉼표가 안나와서, 문자열로 변환 시켜 줌
    lotto_number = str(lotto_number_raw)
    lab_lotto_win_number.config(text = lotto_number) 

# tkinter 가 될 창 Frame 을 win 으로 만들기 
win = Tk()
win.geometry('400x800')
win.title('LOTTO CREATOR')
# 향후 창에 쓰일 모든 텍스트의 기본 폰트 설정
win.option_add("*Font", "맑은고딕 15")

# 라벨 영역에 로또 이미지 넣기
label1_img = Label(win)
# 이미지 변수에 해당 이미지 넣어주기 (master = win 을 해줘야 잘 됨), 상대경로에는 '\' 가 아닌 '/' 로 해줘야 함.
img = PhotoImage(file = 'C:/Users/sukin/OneDrive/Project/HTML/.vscode/Python/Lotto_logo.png', master=win)
# 이미지 크기 줄이기 (1/3 으로)
img = img.subsample(3)
label1_img.config(image = img)
label1_img.pack()

# 로또 번호가 보여질 Label 창 생성
lab_lotto_win_number = Label(win)
lab_lotto_win_number.config(text='"이 곳에 로또 번호가 생성됩니다."')
lab_lotto_win_number.pack()

# 로또 번호 생성을 위한 클릭 버튼
btn_lotto_creator = Button(win)
btn_lotto_creator.config(text = '로또 번호 생성기 (클릭)')
btn_lotto_creator.config(command = lotto_creator)
btn_lotto_creator.pack()


"""
ent = Entry(win) #입력창 만들기
ent.config(show = '*') # 입력문자를 * 표시로 숨기기
ent.insert(0, 'temp@temp.com') # 입력창 문자열 삽입
ent.delete(0, 3) # 0 ~ 2번째 문자열 삭제
ent.bind('<Button-1>', clear) #입력창 클릭시 명령, clear는 미리 만들어논 함수

def clear(event):  #event 는 입력변수
    ent.delete(0, len(ent.get()))
"""

# 당첨번호 조회할 entry 창 라벨 생성
lab_check_win_number = Label(win)
lab_check_win_number.config(text = '당첨번호 조회 대상 회차 입력')
lab_check_win_number.pack()

# 당첨번호 조회 결과 라벨 생성
lab_check_result_win_number = Label(win)
lab_check_result_win_number.config(text='"이 곳에 결과가 조회됩니다."')
lab_check_result_win_number.pack()

# 당첨번호 조회할 entry 창 입력 생성
ent_check_win_number = Entry(win)
ent_check_win_number.config(borderwidth=3, relief=RIDGE)
# insert 메소드는, 디폴트로 보여줄 미리 입력할 값이다. 숫자 '0'은 좌측 정렬
ent_check_win_number.insert(0, '숫자 회차 입력')
# 아래 함수 매개변수에 원래는 생략 '()' 하겠지만, 이번 함수는 마우스 클릭이라는 행위가 있다. 
# 마우스 클릭 이라는 행위를 인식하기 위해, 아무개의 '텍스트' 를 매개 변수 처럼 입력해준다. anything 이든 event 든 아무 글자
# 만약 클릭 행위 없이 바로 수행되게 하려면, 매개변수 생략 '()" 해서 진행하면 된다. 
def ent_check_clear(anything):
    if ent_check_win_number.get() == '숫자 회차 입력':
        ent_check_win_number.delete(0, len(ent_check_win_number.get()))
ent_check_win_number.bind('<Button-1>', ent_check_clear)
ent_check_win_number.pack()

# 동행복권 사이트에서 복권 넘버 가져오기 
def lotto_win_num():
    import requests
    from bs4 import BeautifulSoup
    n = ent_check_win_number.get() # ent 입력창에 들어가는 숫자로 조회 들어가기
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}'.format(n)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    tex = soup.find('div', attrs={'class', 'num win'}).get_text()
    num_list = tex.split('\n')[3:9]
    lab_check_result_win_number.config(text= ent_check_win_number.get()+'회 당첨번호 \n' + str(num_list))
    
btn_check_win_number = Button(win)
btn_check_win_number.config(text = '로또 당첨 번호 확인')
btn_check_win_number.config(width=20)
btn_check_win_number.config(command=lotto_win_num)
btn_check_win_number.pack()

# 로그인 영역 라벨 타이틀 만들기
lab_login_title = Label(win)
lab_login_title.config(text = '동행복권 로그인')
lab_login_title.pack()

# 동행복권 사이트 id 입력창 라벨 
lab_id = Label(win)
lab_id.config(text = 'ID')
lab_id.pack()

# id 입력창
# entry 관련 상세 정보는 https://lcs1245.tistory.com/entry/Python-tkinter-Entry-%EB%A7%8C%EB%93%A4%EA%B8%B0
ent_id = Entry(win)
ent_id.config(borderwidth=3, relief=RIDGE)
ent_id.pack()

# password 라벨
lab_pw = Label(win)
lab_pw.config(text = 'Password')
lab_pw.pack()

# password 입력창
ent_pw = Entry(win)
ent_pw.config(borderwidth=3, relief=RIDGE)
ent_pw.pack()

# 로그인 버튼
btn_login = Button(win)
btn_login.config(text = '로그인')
btn_login.pack()

win.mainloop()

'''
1. 로또 번호 크롤링 + 변수에 저장하기 
2. 
'''