# 옥션 > TV
# 평점 4.5 이상 
# 후기 200개 이상 구매 1000개 이상


import requests
from bs4 import BeautifulSoup
import re

url="http://browse.auction.co.kr/search?keyword=TV&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=TV&acode=SRP_SU_0100&arraycategory=&encKeyword=TV"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
search = soup.find_all("div",{"class":"section--itemcard"})

for search in search:
   
    name = search.find("span",{"class":"text--title"}).get_text()
    price = search.find("strong",{"class":"text--price_seller"}).get_text()
    review = search.find("span",{"class":"text--reviewcnt"})
    buy = search.find("span",{"class":"text--buycnt"})
    url = search.find("a",{"class":"link--itemcard"})["href"]
    
    if review and buy :
        review= int(review.get_text()[3:].replace(",",""))
        buy= int(buy.get_text()[3:].replace(",",""))
        
        if review >=200 and buy>=1000 and url:
            pass        
        else:
            continue
    print("제품명",name)
    print("가격",price)
    print("리뷰개수",review)
    print("구매수",buy)
    print("링크",url)
    print("-"*100)
    
    




