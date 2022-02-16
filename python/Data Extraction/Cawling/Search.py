import requests
from bs4 import BeautifulSoup
import csv
import datetime 
import re

search = input()    #검색어 입력
start_date = input()   #시작 날짜(ex yyyy.mm.dd)
end_date = input() #종료 날짜 (ex yyyy.mm.dd)

csv_filename = search+start_date+end_date

day = datetime.datetime.now()  # 오늘날짜 저장
days = day.strftime('%Y-%m-%d')  #오늘 날짜 서식

csv_opens = open(csv_filename, "w+", encoding='UTF-8')
csv_writer = csv.writer(csv_opens)

for n in range(1,30000,10):  #() 1,첫페이지 10간격으로 다음페이지 30000은 원하는 양만큼 입력 
    url ="https://search.naver.com/search.naver?where=news&sm=tab_pge&query="+search+"&photo=0&field=0&pd=3&ds="+start_date+"&"+end_date+"&cluster_rank=104&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20220101to20220130,a:all&start="+str(n)


    res = requests.get(url)
    res.raise_for_status() 

    soup= BeautifulSoup(res.text, "lxml")
    title = soup.find_all("a",{"class":"news_tit"})

    for i in title: 
        
        others =""
        i= i.get_text()
        i = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“""\’·]', '', i) # 특수문자 제거
        csv_writer.writerow((i,others)) 
