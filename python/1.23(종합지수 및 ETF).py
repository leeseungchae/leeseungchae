from tkinter import *
import matplotlib.pyplot as plt
import FinanceDataReader as fdr

# 2021년 ~ 2022년 1월 23일 
# 종합지수 , 반도체 ,2차전지 , 바이오 ,금융 지수 비교
start_date = ('2022-01-03')
end_date  = ('2022-01-28')

kospi = fdr.DataReader('KS11',start_date,end_date)

#se =반도체
se = fdr.DataReader('091230', start_date,end_date)
#ba =2차전지
ba = fdr.DataReader('364960', start_date,end_date)
#bio =바이오
bio = fdr.DataReader('244580', start_date,end_date)
#inv =금융
inv = fdr.DataReader('139270', start_date,end_date)
#med =미디어
med = fdr.DataReader('098560', start_date,end_date)
#consu =필수소비재
consu = fdr.DataReader('266410', start_date,end_date)
#game = 게임
game = fdr.DataReader('300610', start_date,end_date)
#co = 코스닥
co = fdr.DataReader('229200', start_date,end_date)


#날짜 데이터
date=kospi.index 

#종가 불러오기
kospi=kospi['Close']
se=se['Close']
ba=ba['Close']
bio = bio['Close']
inv = inv['Close']
med = med['Close']
consu = consu['Close']
game = game['Close']
co = co['Close']


# 종가 가격 코스피 기준 조정 함수
def cor(ticker):
    a = fdr.DataReader(ticker, start_date, start_date)
    kospi = fdr.DataReader('KS11', start_date, start_date)
    a = a['Close']
    kospi = kospi['Close']
    div = kospi/a
    return div


# 2022/01/04 코스피 지수  2991

y1 = kospi        
y2 = se * float(cor('091230'))
y3 = ba  * float(cor('364960'))
y4 = bio * float(cor('244580'))
y5 = inv * float(cor('139270'))
y6 = med * float(cor('098560'))
y7 = consu * float(cor('266410')) 
y8 = game *float(cor('300610'))
y9 = co * float(cor('229200'))


x1=date

color_1 = 'tab:blue'  
color_2 = 'tab:orange'
color_3 = 'tab:red'
color_4 = 'tab:green'
color_5 = 'tab:pink'
color_6 = 'tab:brown'
color_7 = 'tab:purple'
color_8 = 'tab:gray'
color_9 = 'tab:olive'


# pearson = np.corrcoef(y1,y2)


plt.xlabel('Date') 

plt.plot(x1, y1,marker='s', color=color_1,label='KOSPI(KS11)') 
plt.plot(x1, y2,marker='s', color=color_2,label='SEMI(091230)') 
plt.plot(x1, y3,marker='s', color=color_3,label='BATTERY(364960)') 
plt.plot(x1, y4,marker='s', color=color_4,label='BIO(244580)') 
plt.plot(x1, y5,marker='s', color=color_5,label='FINANCE(139270)') 
plt.plot(x1, y6,marker='s', color=color_6,label='MEDIA(098560)') 
plt.plot(x1, y7,marker='s', color=color_7,label='CONSUMERS(266410)') 
plt.plot(x1, y7,marker='s', color=color_8,label='GAME(300610)') 
plt.plot(x1, y8,marker='s', color=color_9,label='KOSDAQ(229200)') 

plt.legend()

plt.tick_params(axis='y', labelcolor=color_1)

#print(pearson)
plt.show()
