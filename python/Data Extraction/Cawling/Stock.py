import csv
import datetime
import requests
from bs4 import BeautifulSoup


#웹스크래핑 기본형태
url="https://finance.naver.com/sise/sise_market_sum.nhn?&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
now=datetime.date.today()
#파일 이름 선언
filename  ="시가총액_{}.csv".format(now)
#파일 저장
f = open(filename , "w", encoding="utf-8-sig",newline="")
write = csv.writer(f)
write.writerow(title)

data_rows = soup.find("table",{"class":"type_2"}).find("tbody").find_all("tr")
# data_rows = soup.find(class_="type_2") 클래스만 사용가능
# print(data_rows.prettify()) html 소스가 정렬이 되어서  사용가능

for row in data_rows:
    
    columns = row.find_all("td")
    #data list형태로 저장이 되어서 넣어옴. [1, 삼성전자 , 74500...]
    # data = [column.get_text().strip() for column in columns]
    if len(columns) <= 1:
        continue
    #writerow로 저장을 하려면 list형태로 저장이 되어야 함
    data =[]
    for column in columns:
        data.append(column.get_text().strip())
        
            
    write.writerow(data)








