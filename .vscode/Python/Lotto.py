# 로또 번호 계산기 tkinter 활용

from tkinter import *  #tkinter 모듈 불러오기

# 로또 번호 생성기 함수 만들기
def lotto_creator():
    import random
    num_list = []
    for i in range(46):
        num_list.append(i+1)
    
    #random 모듈의 sample 메소드로, 대상 변수와 뽑을 갯수 숫자 정의
    lotto_number = random.sample(num_list, 6) 
    btn.config(text = lotto_number)

win = Tk()
win.geometry('300x300')
win.title('LOTTO CREATOR')
# 향후 창에 쓰일 기본 폰트 설정
win.option_add("*Font", "HY엽서M 15")

ent = Entry(win) #입력창 만들기
ent.pack() # 입력창 배치

# 동행복권 사이트에서 복권 넘버 가져오기 
def lotto_win_num():
    import requests
    from bs4 import BeautifulSoup
    n = ent.get() # ent 입력창에 들어가는 숫자로 조회 들어가기
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}'.format(n)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    tex = soup.find('div', attrs={'class', 'num win'}).get_text()
    num_list = tex.split('\n')[3:9]
    print(ent.get()+'회 당첨번호')
    print(num_list)

btn = Button(win)
btn.config(text = '로또 당첨 번호 확인')
btn.config(width=20)
btn.config(command=lotto_win_num)
btn.pack()



win.mainloop