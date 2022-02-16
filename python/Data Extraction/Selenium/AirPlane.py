import time
#구글드라이버 
from selenium import webdriver
#KEY입력에 관한 메소드
from selenium.webdriver.common.keys import Keys
#출력화면이 나타날때까지 대기하는 메소드
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from bs4 import BeautifulSoup



browser = webdriver.Chrome()
url="https://flight.naver.com/"
browser.maximize_window() # 윈도우 창 최대로
browser.get(url)

#출발
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[9]/div[2]/section/section/div/button[1]").click()
time.sleep(1)

#도착
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[9]/div[2]/section/section/div/button[2]").click()
time.sleep(1)

#출발 18일 도착 28일
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[6]/button").click()
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button").click()
time.sleep(1)

# 인원 검색
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[4]/div/div/div[2]/div[3]/button").click()
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[4]/div/div/div[3]/div/div[1]/div[1]/button[2]").click()
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[4]/div/div/button").click()  #빈공간 클릭
time.sleep(1)
elem = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[4]/div/div/button").click()

#항공권 검색시간 지연 필요
time.sleep(10)
#브라우저 화면에 해당 태그가 나타날때가지 대기 , 최대 10초간 대기 탐
WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[1]/div/div[1]/div[5]/div/div[2]/div[2]/div/button")))

#스크롤해서 내리면 데이터 계속 증가되는 형태로 구성되어 있음
# 현재 브라우저 높이값
prev_height = browser.execute_script("return document.body.scrollHeight") #1000
while True:
    # 현재 높이에서 브라우저 최대높이까지 스크롤해서 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #데이터가 나타날때가지 대기하고 있음
    time.sleep(1)
    # 화면을 스크롤해서 내려온 화면높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 현재높이와 이전높이가 같은지 비교해서 같으면 더이상 스크롤이 없으므로 빠져나온다
    if curr_height == prev_height:
        break
    # 현재높이를 이전높이에 적응하고 계속적으로 반복
    prev_height = curr_height

# 스크롤을 내리는 명령어를 넣어야 함.
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")
flights = soup.find_all("div",{"class":"result"})
# start = soup.find_all("button",{"class":"tabContent_option__2y4c6 select_Date__1aF7Y"})[0].get_text()
# end = soup.find_all("button",{"class":"tabContent_option__2y4c6 select_Date__1aF7Y"})[1].get_text()

# for start,end in zip(start,end):
#     pass

for flight in flights:
    # print("항공사:", flight.b.get_text())
    # print(start)
    # print(end)
    print("항공사:", flight.find("b",{"class":"name"}).get_text())
    print("출발시간", flight.find_all("span",{"class":"airport"})[0].b.get_text())
    print("도착시간:", flight.find_all("span",{"class":"airport"})[1].b.get_text())
    print("가격:", flight.find("i",{"class":"domestic_num__2roTW"}).get_text())
    print("-"*20)

    
  
    




