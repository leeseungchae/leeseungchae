from selenium import webdriver
import time # 시간 지연
import random #지연시간을 랜덤으로 처리
from selenium.webdriver.common.keys import Keys
# 크롬 드라이버 연결
browser = webdriver.Chrome()
#페이지 이동
browser.get("https://www.naver.com")
# class link_login 선택후 클릭
browser.find_element_by_class_name("link_login").click()
#대기
time.sleep(1)
#자바스크립트로 IP,PW를 input에 입력해주는 js명령어
input_js ='\
    document.getElementById("id").value="{id}";\
    document.getElementById("pw").value="{pw}";\
        ' .format(id="ztmdco",pw="1994ghost.")
time.sleep(3)
browser.execute_script(input_js)
time.sleep(2)
browser.find_element_by_id("log.login").click()










